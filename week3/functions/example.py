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


# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

def two_sum(nums: list, target: int) -> list:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

print(two_sum([2, 7, 11, 15], 9))


# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         if l1 is None:
#             return l2
#         if l2 is None:
#             return l1
#         carry = 0
#         result = ListNode(0)
#         current = result
#         while l1 or l2 or carry:
#             val1 = (l1.val if l1 else 0)
#             val2 = (l2.val if l2 else 0)
#             carry, val = divmod(val1 + val2 + carry, 10)
#             current.next = ListNode(val)
#             current = current.next
#             l1 = (l1.next if l1 else None)
#             l2 = (l2.next if l2 else None)
#         return result.next


#Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        max_length = 1
        current_length = 1
        for i in range(1, len(s)):
            if s[i] in s[:i]:
                if current_length > max_length:
                    max_length = current_length
                current_length = 1
            else:
                current_length += 1
        if current_length > max_length:
            max_length = current_length
        return max_length

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    nums = nums1 + nums2
    nums.sort()
    if len(nums) % 2 == 0:
        return (nums[len(nums)//2] + nums[len(nums)//2 - 1]) / 2
    else:
        return nums[len(nums)//2]

print(findMedianSortedArrays([1,3], [2]))

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

def reverse(x: int) -> int:
    if x > 2**31 - 1 or x < -2**31:
        return 0
    else:
        if x < 0:
            x = -x
            x = int(str(x)[::-1])
            x = -x
            return x
        else:
            return int(str(x)[::-1])

print(reverse(1534236469))


def shuffle_list(lst: list) -> list:
    if len(lst) == 0:
        return lst
    else:
        shuffle_list(lst[1:]) + [lst[0]] + shuffle_list(lst[2:])

