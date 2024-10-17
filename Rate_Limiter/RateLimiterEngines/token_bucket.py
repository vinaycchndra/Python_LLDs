import asyncio
import time 

class TokenBucket:
    def __init__(self, refill_rate: float, max_tokens: int):
        self.refill_interval = 1/3                                      # Will do refill every one third of Second.
        self.tokens_per_refill = refill_rate*self.refill_interval       # Since we are refilling every 333 milli second so refilling should put enough tokens every time   
        self.user_dict = {}
        self.lock  = asyncio.Lock()
        self.max_tokens = max_tokens

    async def start(self):
        try:
            # Bucket refilling loop
            while True: 
                async with self.lock:
                    t1 = time.time()
                    for key in self.user_dict:
                        if self.user_dict[key] < self.max_tokens:
                            self.user_dict[key] = self.user_dict[key]+self.tokens_per_refill
                    t2 = time.time()
                # Giving control back to the event loop as the bucket refilling is done and sleeping for the time till next refilling turn.
                await asyncio.sleep(self.refill_interval-(t2-t1))
        except asyncio.CancelledError:
            print("Closing the refilling process as the rate limit server is shutting down.")

    async def approve_request(self, user: str):
        if user not in self.user_dict:
            #  Since loop which is refilling the clients' bucket may take longer time than the refill_interval in that case system will 
            #  not be able to respond to this approve_request function as the lock will be applied for all the time.
            if len(self.user_dict) == 5000:
                print("Can not add more users for rate limiting system overwhelmed.")
                return False
            
            # Always allowing a user to get their first request approved after registering.
            async with self.lock:
                self.user_dict[user] = 0
                return True
            
        # Acquiring the lock to update the user base dictionary.
        async with self.lock:
            if self.user_dict[user]>1:
                self.user_dict[user] -= 1
                return True
            return False



