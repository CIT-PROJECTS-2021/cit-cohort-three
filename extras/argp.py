import argparse
import sys


def add(a, b):
    return a + b

def mul(a, b):
    return a*b

def sub(a, b):
    return a - b

def divide(a, b):
    return a//b

parser = argparse.ArgumentParser('Simple calculator')
parser.add_argument('-a', '--add', help='add two numbers', action='store_true')

args = parser.parse_args()

if args.add:
    print(add(int(input('Enter number one: ')), int(input('Enter number two: '))))
else:
    parser.print_help()
