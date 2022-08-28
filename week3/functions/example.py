# Programs that will help you to understand functions in Python.

# Program to find the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

# Explanation:
# The above program will find the factorial of a number which is passed as an argument n.
# The program will return the factorial of n.
# The program will return 1 if n is 0.
# The program will return n * factorial(n-1) if n is not 0.
# The program will keep on calling the function factorial(n-1) until n is 0.
# This program is an example of a recursive function.

# Program to find the factorial of a number using a while loop
def factorial_while(n):
    fact = 1
    while n > 0:
        fact = fact * n
        n = n - 1
    return fact

print(factorial_while(5))

# Explanation:
# In the above program, we used a while loop to find the factorial of a number which is passed as an argument n.

# Program that calls another function
def call_function(n):
    return factorial(n)

print(call_function(5))

# Explanation:
# In the above example, call_function() is a function that calls factorial() and passes 5 as an argument.
# The function factorial() will return the factorial of 5.
# The function call_function() will return the factorial of 5.
# This is an example of a function that calls another function.


# A function to reverse a string
def reverse_string(s: str) -> str:
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

print(reverse_string('hello'))

# Explanation:
# The reverse_string() function will reverse a string given string s, and return the reversed string.
# The function will return the reversed string if the length of s is 0.
# Until the length of s is 0, the program will keep on calling the function reverse_string(s[1:]) and add the first character of s to the end of the returned string.


# A function that calls itself is called recursive function.


# A function that returns a function
def outer_function():
    def inner_function():
        print('Hello')
    return inner_function

outer_function()()


# a function that finds the maximum number in a list
def find_max(lst: list) -> int:
    max_num = lst[0]
    for num in lst:
        if num > max_num:
            max_num = num
    
    return max_num


print(find_max([3, 56, -78, 34, 2]))




