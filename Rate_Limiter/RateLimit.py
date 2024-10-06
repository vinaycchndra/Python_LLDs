from RateLimiterEngines.token_bucket import TokenBucket

class RateLimiter:
    def __init__(self, algo: str = None, permitted_rate: float = None, perHour: bool = False, perSecond: bool = False, perMinute: bool = False):
        self.algo = algo
        self.permitted_rate = permitted_rate
        
        # permitted rate can not be zero or None
        assert self.permitted_rate
        # only one parameter should be true
        assert perMinute+perHour+perSecond == 1

        # Fixing a minimum window limit for the normal system to handle bulk refilling of the clients tokens 
        # for example in a token bucket class: If running a loop to refilling the buckets of the users with a single for loop. if there are more clients accessing
        # then a loop may take more 100 milli second to complete the refilling of all the users.  
        if perSecond:
            if self.permitted_rate> 10:
                raise Exception("Per second config does not allow more than the 10 requests per second to avoid complexity")
            self.time_limit = 1/self.permitted_rate

        if perMinute:
            if self.permitted_rate> 600:
                raise Exception("Per minute config does not allow more than the 600 requests per minute to avoid complexity")
            self.time_limit = 60/self.permitted_rate
        
        if perHour:
            if self.permitted_rate> 24000:
                raise Exception("Per hour config does not allow more than the 24000 requests per hour to avoid complexity")
            self.time_limit = 2400/self.permitted_rate

        if self.algo ==  "token_bucket":
            self.algo = TokenBucket(time_limit = self.time_limit)
        else:
            raise Exception("Please provide the valid rate limiting algorithm to use.")
        