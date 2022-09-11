# import example
# from example import add, subtract, multiply
from example import *

# print(example.add(1, 2))
# print(example.subtract(1, 2))
# print(example.multiply(1, 2))

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))

import math

print(math.sqrt(4))
print(math.pi)
print(math.sin(math.pi / 2))

import os
import sys

print(os.getcwd())
print(sys.platform)

user_name = input("What is your name? ")

if not user_name:
    print("You did not enter a name.")
    sys.exit(1)

print(f"Hello, {user_name}!")

# Your audio is not connected

# external modules
# pip install <module_name>