import sys
import os


def add(a, b):
    return a + b

def mul(a, b):
    return a*b

def sub(a, b):
    return a - b

def divide(a, b):
    return a//b


if len(sys.argv) == 1:
    print('usage: python args.py add 1 2')
    sys.exit(-1)


print(sys.argv)

if sys.argv[1] == 'add':
    print(add(int(sys.argv[2]), int(sys.argv[3])))

elif sys.argv[1] == 'mul':
    pass

else:
    print('Invalid operation')

