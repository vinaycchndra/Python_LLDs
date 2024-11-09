import asyncio
import time 
from collections import deque
class SlidingWindowLog:
    def __init__(self, allowed_requests: float, sliding_window_length: int):
        self.allowed_requests = allowed_requests                                      
        self.sliding_window_length = sliding_window_length      
        self.user_dict = {}

    async def start(self):
        try:
            # This loop not required in this case, just mantaining the dummy start function for managing the consistency with the other rate limiter classes. 
            while True: 
                await asyncio.sleep(10)
        except asyncio.CancelledError:
            print("Closing the start process as the rate limit server is shutting down.")

    async def approve_request(self, user: str):
        request_time = self.get_current_time()
        current_window_start_time = request_time-self.sliding_window_length
        if user not in self.user_dict:
            data_dict  = {
                "user_queue": deque(),  
                "lock": asyncio.Lock()
            }
            self.user_dict[user] = data_dict
        
        async with self.user_dict.get(user).get("lock"):
            user_que = self.user_dict.get(user).get("user_queue")
            while len(user_que)>0 and user_que[0] <= current_window_start_time:
                user_que.popleft()
            if len(user_que) < self.allowed_requests:
                user_que.append(request_time)
                return True
            return False

    def get_current_time(self):
        return int(time.time())
    
