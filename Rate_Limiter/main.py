import asyncio
from RateLimit import RateLimiter 
import time


# This function is mimicking the request of the user from a maximum user base of 5000 clients and maximum rate limit possible is 10 and every user is given 
# equal share of requests. 
async def coming_requsts(rl, rate_limiter_loop):
    t1 = time.time()
    a = 1
    b = 5000 # max users
    approved = {i:0 for i in range(a, b+1)}
    total_request = {i:0 for i in range(a, b+1)}
    total_incoming = 10000000
    for k in range(1, total_incoming+1):
        user = k%b
        if user == 0:
            user = b
        total_request[user] += 1
        await asyncio.sleep(0.000000000001)
        approve = await rl.approve_request(user)
        if approve:
            approved[user] = approved[user]+1
        
    
    total_time = time.time()-t1
    
    for i in range(a, b+1):
        print(f"user : {i}--> total_requests: {total_request.get(i)}--> Approved Requests: {approved.get(i)}--> in time: {total_time}--> Approved rate: {approved.get(i)/total_time}")
    
    total_approved = 0
    total_requested = 0
    
    for i in range(a, b+1):    
        total_approved += approved[i]
        total_requested += total_request[i]
    print(f"Total processed requests: {total_approved} out of {total_requested} requests.")

    # Cancelling the refilling bucket background process as no more request will come to the server from this task. 
    rate_limiter_loop.cancel()

async def main():
    rl_config = RateLimiter("token_bucket", 10, perSecond=True)
    rl =  rl_config.get_rate_limiter()
    task1 = asyncio.create_task(rl.start())
    task2 = asyncio.create_task(coming_requsts(rl, task1))
    await asyncio.gather(task1, task2)

asyncio.run(main())