from calendar import month
import random
import datetime

print(random.randint(1,80))
print(random.randint(1,80))
print(random.randint(1,80))
print(random.randint(1,80))
print(random.randint(1,80))

now = datetime.datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
future_time = datetime.timedelta(days =10)
print(now + future_time)
