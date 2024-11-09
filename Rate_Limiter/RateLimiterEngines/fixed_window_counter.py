import asyncio
import time 

class FixedWindowCounter:
    def __init__(self, allowed_requests: float, fixed_window_length: int):
        self.allowed_requests = allowed_requests                                      
        self.fixed_window_length = fixed_window_length      
        self.user_dict = {}

    async def start(self):
        try:
            # Count reset loop not required in this case, just mantaining the dummy start function for managing the consistency with the other rate limiter classes. 
            while True: 
                await asyncio.sleep(10)
        except asyncio.CancelledError:
            print("Closing the start process as the rate limit server is shutting down.")

    async def approve_request(self, user: str):
        if user not in self.user_dict:
            data_dict  = {
                "current_window": self.get_current_time(), 
                "request_counter": 0, 
                "lock": asyncio.Lock()
            }
            self.user_dict[user] = data_dict
        
        async with self.user_dict.get(user).get("lock"):
            self.update_current_user_window(self.user_dict.get(user))
            if self.user_dict.get(user).get("request_counter") < self.allowed_requests:
                self.user_dict[user]["request_counter"] += 1
                return True
            return False

    #  A user dict can have the  following characterstics: 
        # Current time window 
        # Request counter
        # A lock obj specific to every user as we can have concurrent request of same user which are trying to update the time window and request counters.
    def update_current_user_window(self, user_data):
        old_window_time = user_data.get("current_window")
        current_time = self.get_current_time()
        time_passed = current_time-old_window_time

        if time_passed>=self.fixed_window_length:
            user_data["current_window"] = current_time-(time_passed%self.fixed_window_length)
            user_data["request_counter"] = 0
        
    def get_current_time(self):
        return int(time.time())
    
