

import time 
import redis 

cache = redis.Redis(host='redis', port=6379)

while True:
    print("Worker is running...")
    cache.set('worker_status', 'running')
    time.sleep(5)
    
    