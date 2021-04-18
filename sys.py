from datetime import datetime
import time
import random

 
odd = range(1,60,2)

for i in range(2):
    realtime = datetime.today().minute
    if realtime in odd:
        print("The present minute is odd.")
    else:
        print("The present minute is even.")
        
    wait_time = random.randint(1,60)
    time.sleep(wait_time) 