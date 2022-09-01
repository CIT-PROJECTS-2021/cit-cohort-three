# The following code will teach you how to use the built-in modules in Python

import os
import sys
import time
import datetime
import calendar
import random
import math
import statistics
import json

# os module
print(os.getcwd())
print(os.listdir())
print(os.name)
print(os.uname())
print(os.getlogin())

# sys module
print(sys.version)
print(sys.platform)
print(sys.path)

# time module
print(time.time())
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))

# datetime module
print(datetime.datetime.now())
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3])
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3].replace(" ", "T"))

# calendar module
print(calendar.month(2022, 9))

# random module
print(random.random())
print(random.randint(1, 10))
print(random.randrange(1, 10))
print(random.choice([1, 2, 3, 4, 5]))
print(random.sample([1, 2, 3, 4, 5], 3))
print(random.sample(range(1, 10), 3))

# math module
print(math.pi)
print(math.e)
print(math.sin(math.pi / 6))
print(math.cos(math.pi / 3))
print(math.tan(math.pi / 4))
print(math.pow(2, 3))
print(math.sqrt(9))
print(math.ceil(2.1))
print(math.floor(2.9))
print(math.fabs(-2.9))
print(math.factorial(5))

# statistics module
print(statistics.mean([1, 2, 3, 4, 5]))
print(statistics.median([1, 2, 3, 4, 5]))
print(statistics.mode([1, 2, 3, 4, 5, 5]))
print(statistics.stdev([1, 2, 3, 4, 5]))
print(statistics.variance([1, 2, 3, 4, 5]))

# json module
json_str = '{"name": "John", "age": 30, "city": "New York"}'
print(json.loads(json_str))
print(json.dumps(json.loads(json_str)))
