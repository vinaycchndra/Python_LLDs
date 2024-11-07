from RateLimiterEngines.token_bucket import TokenBucket
from RateLimiterEngines.leaky_bucket import LeakyBucket
from RateLimiterEngines.fixed_window_counter import FixedWindowCounter
class RateLimiter:
    def __init__(self, algo: str = None, permitted_rate: float = None):
        self.algo = algo
        self.permitted_rate = permitted_rate
        
        # permitted rate should not be zero or None
        assert self.permitted_rate

        if self.permitted_rate> 600:
            raise Exception("Per minute config does not allow more than the 600 requests per minute to fill max number of client's bucket.")
        
        if self.algo ==  "token_bucket":
            self.__rate_limiter = TokenBucket(refill_rate = self.permitted_rate/60, max_tokens = 5)
        elif self.algo == "leaky_bucket":
            self.__rate_limiter = LeakyBucket(leak_rate = self.permitted_rate/60, max_bucket_size= 5)    
        elif self.algo == "fixed_window_counter":
            self.__rate_limiter = FixedWindowCounter(allowed_requests = int(self.permitted_rate/60*5),fixed_window_length=5)
        else:
            raise Exception(
                            """Please provide the valid rate limiting algorithm from 
                            1.  'token_bucket' 
                            2.  'leaky_bucket'.
                            """
                        )
        
    def get_rate_limiter(self):
        return self.__rate_limiter
