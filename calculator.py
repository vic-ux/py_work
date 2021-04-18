#my_range = [10*i for i in (range(1,21))]
#print (my_range)

#my = range (1,21)
#for i in my:
#    print(i*10)


#my_range = range(1,21)
#print (list(map(str,my_range)))

import random
from random import randint
import time
def gen():
       Account_num = []
       Account_num.sort()
       acct_numGen = randint (1234567890,9999999999)
       Account_num.append(acct_numGen)
       wait_time = random.randint(1,30)
       time.sleep(wait_time)
       print(Account_num)
   

gen()




"""
for i in range(10):
       acct = random.randint(1,10)
       print(acct)

       

"""














#if value > 1:
 #   if value % prime != 0:
  #      val = list(range(prime -1 ,value + 1,2))
   #     val.pop(0)
    #    print(val)
     #   for valu in val:
      #      if value % valu == 0:
       #         print ("")
    #elif prime % 2 == 0:
     #   print ("Value is a prime number.")
    #else:
        
     #   print ("Value is not a prime number.")
#else:
 #   print ("invalid entry")
    