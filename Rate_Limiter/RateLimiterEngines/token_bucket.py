import asyncio
import time 

class TokenBucket:
    def __init__(self, timelimit: float):
        self.timelimit = timelimit
        self.user_dict = {}
        self.lock  = asyncio.Lock()
        self.max_tokens = int(1/self.timelimit)

    async def start(self):
        try:
            while True: 
                async with self.lock:
                    t1 = time.time()
                    for key in self.user_dict:
                        if self.user_dict[key] != self.max_tokens:
                            self.user_dict[key] = self.user_dict[key]+1
                    t2 = time.time()
                    
                await asyncio.sleep(self.timelimit-(t2-t1))
        except asyncio.CancelledError:
            print("Closing the refilling process as the rate limit server is shutting down.")

    async def approve_request(self, user: str):
        if user not in self.user_dict:
            #  Since loop which is refilling the clients' bucket may take longer time than the timelimit in that case system will 
            #  not be able to respond to this approve_request function as the lock will be applied for all the time.
            if len(self.user_dict) == 5000:
                print("Can not add more users for rate limiting system overwhelmed.")
                return False
            
            async with self.lock:
                self.user_dict[user] = 0
                return True
        
        async with self.lock:
            if self.user_dict[user]>1:
                self.user_dict[user] -= 1
                return True
            return False



