import asyncio
import time
from queue import Queue
import logging
 
class LeakyBucket:
    logger = logging.getLogger(__name__)

    def __init__(self, leak_rate: float, max_bucket_size: int):
        if leak_rate>=3:
            self.leak_interval = 1/3                                         # Will leak the bucket every one third of Second.
            self.requests_per_leak = int(leak_rate*self.leak_interval)       # Since we are leaking every 333 milli second so refilling should put enough tokens every time.   
        else:
            self.leak_interval = 1/leak_rate
            self.requests_per_leak = 1

        self.user_dict = {}
        self.lock  = asyncio.Lock()
        self.bucket_size = max_bucket_size

    async def start(self):
        try:
            # Bucket refilling loop
            while True:
                async with self.lock:
                    t1 = time.time()
                    for key in self.user_dict:
                        user_request_que  = self.user_dict.get(key)
                        to_remove = user_request_que.qsize() if self.requests_per_leak > user_request_que.qsize() else self.requests_per_leak
                        # Leaking the requests from the bucket
                        while to_remove>0:
                            user_request_que.get()
                            to_remove -= 1
                    t2 = time.time()
                print(f"Leaking the bucket happened at {t2} in {t2-t1} and user dict is {len(self.user_dict)}")
                # Giving control back to the event loop as the bucket refilling is done and sleeping for the time till next refilling turn.
                await asyncio.sleep(self.leak_interval-(t2-t1))
        except asyncio.CancelledError:
            print("Closing the refilling process as the rate limit server is shutting down.")

    async def approve_request(self, user: str):
        if user not in self.user_dict:
            #  Since loop which is refilling the clients' bucket may take longer time than the leak_interval in that case system will 
            #  not be able to respond to this approve_request function as the lock will be applied for all the time.
            if len(self.user_dict) == 100:
                print("Can not add more users for rate limiting system overwhelmed.")
                return False
            
            # Always allowing a user to get their first request approved after registering.
            async with self.lock:
                self.user_dict[user] = Queue(maxsize=self.bucket_size)
                # Just adding a time variable as request for that user into the bucket.
                self.user_dict[user].put(time.time())
                return True
            
        # Acquiring the lock to update the user bucket.
        async with self.lock:
            if self.user_dict[user].full():
                return False
            else:
                self.user_dict[user].put(time.time())
                return True
    