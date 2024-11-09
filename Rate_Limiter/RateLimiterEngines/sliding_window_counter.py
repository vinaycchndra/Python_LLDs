import asyncio
import time 
import math

class SlidingWindowCounter:
    def __init__(self, allowed_requests: float, window_length: int):
        self.allowed_requests = allowed_requests                                      
        self.window_length = window_length      
        self.user_dict = {}

    async def start(self):
        try:
            # Count reset loop not required in this case, just mantaining the dummy start function for managing the consistency with the other rate limiter classes. 
            while True: 
                await asyncio.sleep(10)
        except asyncio.CancelledError:
            print("Closing the start process as the rate limit server is shutting down.")

    async def approve_request(self, user: str):
        current_time = self.get_current_time()
        if user not in self.user_dict:
            data_dict  = {
                "current_window": self.get_current_time(), 
                "curr_window_request_counts": 0,
                "previous_window_request_counts": 0, 
                "lock": asyncio.Lock()
            }
            self.user_dict[user] = data_dict
        
        async with self.user_dict.get(user).get("lock"):
            self.update_current_user_window(self.user_dict.get(user), current_time)
            request_count = self.calculate_request_count(self.user_dict.get(user), current_time)
            if request_count < self.allowed_requests:
                self.user_dict[user]["curr_window_request_counts"] += 1
                return True
            return False

    #  A user dict can have the  following characterstics: 
        # Current time window 
        # Request counter for the current window 
        # Request counter for the previous window
        # A lock obj specific to every user as we can have concurrent request of same user which are trying to update the time window and request counters.
    def update_current_user_window(self, user_data, current_time):
        old_window_time = user_data.get("current_window")
        time_passed = current_time-old_window_time
        no_of_windows_passed = time_passed//self.window_length
        # if the window gap is more than equal to 2 in this case we had no previous window requests. 
        if no_of_windows_passed>=2:
            user_data["previous_window_request_counts"]  = 0
            user_data["curr_window_request_counts"] = 0
        elif no_of_windows_passed>=1:
            user_data["previous_window_request_counts"] = user_data.get("curr_window_request_counts")
            user_data["curr_window_request_counts"] = 0
        user_data["current_window"] = current_time-(time_passed%self.window_length)

    def calculate_request_count(self, user_data, current_time):
        delta_current = current_time-user_data.get("current_window")
        delta_prev = self.window_length-delta_current
        return math.ceil((delta_prev/self.window_length)*user_data.get("previous_window_request_counts", 0)+user_data.get("curr_window_request_counts", 0))

    def get_current_time(self):
        return int(time.time())
    
