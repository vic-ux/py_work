from datetime import datetime
odd = range(1,60,2)
realtime = datetime.today().minute
if realtime in odd:
    print("The present minute is odd.")
else:
    print("The present minute is even.")
