a = 50 

if a > 30:
    print(a*80)
    print("a is greater than 30")
    if a/30==2:
        print("a is divided by 30 is 2")
    else:
        print("a is divided by 30 is not 2")
elif a < 50:
    print("timepass")
else:
    print(a*20)
    print("a is less than 30")

import datetime 
currenttime = datetime.datetime.now()
print(currenttime)

import calendar
print(calendar.calendar(2025))