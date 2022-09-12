"""
Author: IDEN
"""

# # CIT Python Quiz Week 4 solutions

# 1. Create a 2-D array and slice out the second number in the second column
# 2. Write a python program to sort array element in the ascending/descending order
# 3. Write a python program to find the maximum and minimum value in a given 2-D array
# 4.  Write a python program to input 5 subject marks and calculate total marks, percentage and grade based on following criteria
#     - percentage less than `50` (Grade C)
#     - percentage equal to `50` and less than `80` (Grade B)
#     - percentage equal to `80` and more than `80` (Grade A)
# 5. Write a python program to fetch only Email ID from text file  which include following fields -:
#     - Name
#     - Mobile Number
#     - Roll Number
#     - Email ID
# 6. Write a function for checking the speed of drivers. This function should have one parameter: speed.
#     - If speed is less than 70, it should print “Ok”.
#     - Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
#     - If the driver gets more than 12 points, the function should print: “`License suspended`”
# 7. Write a function called `show_stars(rows)`. If rows is 5, it should print the following:
# ```bash
# *
# **
# ***
# ****
# *****
# ```
# 8. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5 between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# 9. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:

# ```bash
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
# ```

# 10. Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# `100,150,180`
# The output of the program should be:
# `18,22,24`

# 11. Write a function to compute 5/0 and use try/except to catch the exceptions.

# 12. Create a nesting list that prints out the color and the car brand.

# 13. Bonus Question: Algorithm challenge: Create your own sorting algorithm.

# 1. Create a 2-D array and slice out the second number in the second column

import math
import numpy as np
import sys

def slice_array(list: list) -> list:
    """Slices the second number in the second column of a 2D array

    Args:
        list (list): A 2D array

    Returns:
        list: The sliced array
    """
    return list[:, 1]


print(slice_array(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])))


# 2. Write a python program to sort array element in the ascending/descending order
def sort_array(list: list, order: str) -> list:
    """Sorts an array in ascending or descending order

    Args:
        list (list): The array to be sorted
        order (str): The order to sort the array in

    Returns:
        list: The sorted array
    """
    if order == "ascending":
        return np.sort(list)
    elif order == "descending":
        return np.sort(list)[::-1]
    else:
        return "Invalid order"

print(sort_array(np.array([np.random.randint(1, 100) for _ in range(10)]), "ascending"))
print(sort_array(np.array([np.random.randint(1, 100) for _ in range(10)]), "descending"))

# 3. Write a python program to find the maximum and minimum value in a given 2-D array
def find_max_min(list: list) -> list:
    """Finds the maximum and minimum value in a 2D array

    Args:
        list (list): The 2D array

    Returns:
        list: The maximum and minimum value
    """
    return [np.max(list), np.min(list)]

print(find_max_min(np.array([[np.random.randint(1, 100) for _ in range(10)] for _ in range(10)])))

# 4.  Write a python program to input 5 subject marks and calculate total marks, percentage and grade based on following criteria
#     - percentage less than `50` (Grade C)
#     - percentage equal to `50` and less than `80` (Grade B)
#     - percentage equal to `80` and more than `80` (Grade A)
def calculate_grade(marks: list) -> str:
    """Calculates the grade of a student based on their marks

    Args:
        marks (list): The marks of the student

    Returns:
        str: The grade of the student
    """
    total = sum(marks)
    percentage = total / len(marks)
    if percentage < 50:
        return "Grade C"
    elif percentage >= 50 and percentage < 80:
        return "Grade B"
    elif percentage >= 80:
        return "Grade A"
    else:
        return "Invalid marks"

print(calculate_grade([np.random.randint(1, 100) for _ in range(5)]))

# 5. Write a python program to fetch only Email ID from text file  which include following fields -:
#     - Name
#     - Mobile Number
#     - Roll Number
#     - Email ID
def fetch_email(file: str) -> list:
    """Fetches the email from a text file

    Args:
        file (str): The text file

    Returns:
        list: The emails
    """
    import re

    emails = []
    with open(file, "r") as f:
        for line in f:
            emails.append(re.search(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", line).group())

print(fetch_email("data.txt"))

# 6. Write a function for checking the speed of drivers. This function should have one parameter: speed.
#     - If speed is less than 70, it should print “Ok”.
#     - Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
#     - If the driver gets more than 12 points, the function should print: “`License suspended`”
def check_speed(speed: int) -> str:
    """Checks the speed of a driver

    Args:
        speed (int): The speed of the driver

    Returns:
        str: The demerit points or license suspension
    """
    if speed < 70:
        return "Ok"
    elif speed >= 70:
        points = (speed - 70) // 5
        if points > 12:
            return "License suspended"
        else:
            return f"Points: {points}"

print(check_speed(80))

# 7. Write a function called `show_stars(rows)`. If rows is 5, it should print the following:
# ```bash
# *
# **
# ***
# ****
# *****
# ```
def show_stars(rows: int) -> None:
    """Prints out a pattern of stars

    Args:
        rows (int): The number of rows
    """
    for i in range(rows):
        print("*" * (i + 1))

print(show_stars(5))

# 8. Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5 between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
def find_numbers() -> list:
    """Finds the numbers between 2000 and 3200 that are divisible by 7 but not a multiple of 5

    Returns:
        list: The numbers
    """
    numbers = []
    for i in range(2000, 3201):
        if i % 7 == 0 and i % 5 != 0:
            numbers.append(i)
    return numbers

print(find_numbers())

# 9. Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# `without,hello,bag,world`
# Then, the output should be:
# `bag,hello,without,world`
def sort_words(words: str) -> str:
    """Sorts the words in a string alphabetically

    Args:
        words (str): The words

    Returns:
        str: The sorted words
    """
    words = words.split(",")
    words.sort()
    return ",".join(words)

print(sort_words("without,hello,bag,world"))

# 10. Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# `Hello world`
# `Practice makes perfect`
# Then, the output should be:
# `HELLO WORLD`
# `PRACTICE MAKES PERFECT`
def capitalize_lines(lines: str) -> str:
    """Capitalizes the lines

    Args:
        lines (str): The lines

    Returns:
        str: The capitalized lines
    """
    lines = lines.split(" ")
    capitalized_lines = []
    for line in lines:
        capitalized_lines.append(line.upper())
    return " ".join(capitalized_lines)

print(capitalize_lines("Hello world Practice makes perfect"))

# 11. Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# `hello world and practice makes perfect and hello world again`
# Then, the output should be:
# `again and hello makes perfect practice world`
def remove_duplicate_words(words: str) -> str:
    """Removes duplicate words and sorts them alphabetically

    Args:
        words (str): The words

    Returns:
        str: The sorted words
    """
    words = words.split(" ")
    words = list(set(words))
    words.sort()
    return " ".join(words)

print(remove_duplicate_words("hello world and practice makes perfect and hello world again"))

# 12. Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# `hello world! 123`
# Then, the output should be:
# `LETTERS 10`
# `DIGITS 3`
def count_letters_digits(sentence: str) -> str:
    """Counts the number of letters and digits in a sentence

    Args:
        sentence (str): The sentence

    Returns:
        str: The number of letters and digits
    """
    letters = 0
    digits = 0
    for char in sentence:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
    return f"LETTERS {letters} \n DIGITS {digits}"

print(count_letters_digits("hello world! 123"))

# 13. Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# `Hello world!`
# Then, the output should be:
# `UPPER CASE 1`
# `LOWER CASE 9`
def count_upper_lower(sentence: str) -> str:
    """Counts the number of upper and lower case letters in a sentence

    Args:
        sentence (str): The sentence

    Returns:
        str: The number of upper and lower case letters
    """
    upper = 0
    lower = 0
    for char in sentence:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    return f"UPPER CASE {upper} \n LOWER CASE {lower}"

print(count_upper_lower("Hello WorlD!"))

# 9. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:

# ```bash
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
# 
def generate_list_tuple(numbers: str) -> tuple:
    """Generates a list and a tuple from a string of numbers

    Args:
        numbers (str): The numbers

    Returns:
        tuple: The list and tuple
    """
    numbers = numbers.split(",")
    return numbers, tuple(numbers)

print(generate_list_tuple("34,67,55,33,12,98"))

# 10. Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# `100,150,180`
# The output of the program should be:
# `18,22,24`

def calculate_value(numbers: str) -> list:
    """Calculates the value of Q

    Args:
        numbers (str): The numbers

    Returns:
        list: The values of Q
    """
    C = 50
    H = 30
    values = []
    numbers = numbers.split(",")
    for number in numbers:
        Q = round(math.sqrt((2 * C * int(number)) / H))
        values.append(Q)
    return values

print(calculate_value("100,150,180"))


# 11. Write a function to compute 5/0 and use try/except to catch the exceptions.

def divide_by_zero() -> float:
    """Divides by zero

    Returns:
        float: The result
    """
    try:
        return 5 / 0
    except ZeroDivisionError:
        return "Cannot divide by zero"

print(divide_by_zero())

# 12. Create a nesting list that prints out the color and the car brand.

def print_color_brand() -> None:
    """Prints the color and the car brand
    """
                      # 0                         1
    cars_colors = [["red", "blue", "green"], ["BMW", "Audi", "VW"]]
    for car in cars_colors[1]:
        for color in cars_colors[0]:
            print(f"{color} {car}")

print_color_brand()

# 13. Write a function that takes a list of numbers and returns a new list with unique elements of the first list.

def unique_list(numbers: list) -> list:
    """Returns a list with unique elements

    Args:
        numbers (list): The numbers

    Returns:
        list: The unique numbers
    """
    return list(set(numbers))

print(unique_list([1, 2, 3, 3, 3, 3, 4, 5]))

# 13. Bonus Question: Algorithm challenge: Create your own sorting algorithm.

def split_list(numbers: list) -> tuple:
    """Splits a list into two

    Args:
        numbers (list): The numbers

    Returns:
        tuple: The two lists
    """
    half = len(numbers) // 2
    
    return numbers[:half], numbers[half:]

def merge_lists(list1: list, list2: list) -> list:
    """Merges two lists

    Args:
        list1 (list): The first list
        list2 (list): The second list

    Returns:
        list: The merged list
    """
    merged_list = []
    while list1 and list2:
        if list1[0] < list2[0]:
            merged_list.append(list1.pop(0))
        else:
            merged_list.append(list2.pop(0))
    merged_list.extend(list1)
    merged_list.extend(list2)
    return merged_list

def merge_sort(numbers: list) -> list:
    """Sorts a list using merge sort

    Args:
        numbers (list): The numbers

    Returns:
        list: The sorted list
    """
    if len(numbers) <= 1:
        return numbers
    list1, list2 = split_list(numbers)
    list1 = merge_sort(list1)
    list2 = merge_sort(list2)
    return merge_lists(list1, list2)

print(merge_sort([1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20][::-1]))

# END OF SOLUTIONS

#BONUS 2. Binary Search

def binary_search(numbers: list, number: int) -> int:
    """Searches for a number in a list using binary search

    Args:
        numbers (list): The numbers
        number (int): The number to search for

    Returns:
        int: The index of the number
    """
    left = 0
    right = len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == number:
            return mid
        elif numbers[mid] < number:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))

#BONUS 3. Bubble Sort

def bubble_sort(numbers: list) -> list:
    """Sorts a list using bubble sort

    Args:
        numbers (list): The numbers

    Returns:
        list: The sorted list
    """
    for i in range(len(numbers) - 1):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

print(bubble_sort([1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20][::-1]))

#BONUS 4. Insertion Sort

def insertion_sort(numbers: list) -> list:
    """Sorts a list using insertion sort

    Args:
        numbers (list): The numbers

    Returns:
        list: The sorted list
    """
    for i in range(1, len(numbers)):
        j = i - 1
        key = numbers[i]
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers

print(insertion_sort([1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20][::-1]))

#BONUS 5. Selection Sort

def selection_sort(numbers: list) -> list:
    """Sorts a list using selection sort

    Args:
        numbers (list): The numbers

    Returns:
        list: The sorted list
    """
    for i in range(len(numbers) - 1):
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers

print(selection_sort([1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20][::-1]))

#BONUS 6. Quick Sort

def quick_sort(numbers: list) -> list:
    """Sorts a list using quick sort

    Args:
        numbers (list): The numbers

    Returns:
        list: The sorted list
    """
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[0]
    left = [number for number in numbers[1:] if number < pivot]
    right = [number for number in numbers[1:] if number >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort([1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20][::-1]))

#BONUS 7. Heap Sort

def heapify(numbers: list, n: int, i: int) -> None:
    """Heapifies a list

    Args:
        numbers (list): The numbers
        n (int): The length of the list
        i (int): The index
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and numbers[i] < numbers[left]:
        largest = left
    if right < n and numbers[largest] < numbers[right]:
        largest = right
    if largest != i:
        numbers[i], numbers[largest] = numbers[largest], numbers[i]
        heapify(numbers, n, largest)

def heap_sort(numbers: list) -> list:
    """Sorts a list using heap sort

    Args:
        numbers (list): The numbers

    Returns:
        list: The sorted list
    """
    n = len(numbers)
    for i in range(n // 2 - 1, -1, -1):
        heapify(numbers, n, i)
    for i in range(n - 1, 0, -1):
        numbers[i], numbers[0] = numbers[0], numbers[i]
        heapify(numbers, i, 0)
    return numbers

print(heap_sort([1, 3, 2, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20][::-1]))

#BONUS 8. Counting Sort

def counting_sort(numbers: list) -> list:
    """Sorts a list using counting sort

    Args:
        numbers (list): The numbers

    Returns:
        list: The sorted list
    """
    max_number = max(numbers)
    count = [0] * (max_number + 1)
    for number in numbers:
        count[number] += 1
    i = 0
    for number in range(max_number + 1):
        for j in range(count[number]):
            numbers[i] = number
            i += 1
    return numbers

#BONUS 9. Radix Sort

def counting_sort_radix(numbers: list, exp: int) -> list:
    """Sorts a list using counting sort(for radix sort)

    Args:
        numbers (list): The numbers
        exp (int): The exponent

    Returns:
        list: The sorted list
    """
    n = len(numbers)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = numbers[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = numbers[i] // exp
        output[count[index % 10] - 1] = numbers[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(n):
        numbers[i] = output[i]
    return numbers

def radix_sort(numbers: list) -> list:
    """Sorts a list using radix sort

    Args:
        numbers (list): The numbers

    Returns:
        list: The sorted list
    """
    max_number = max(numbers)
    exp = 1
    while max_number // exp > 0:
        counting_sort_radix(numbers, exp)
        exp *= 10
    return numbers

#BONUS 10. Bucket Sort

def bucket_sort(numbers: list) -> list:
    """Sorts a list using bucket sort

    Args:
        numbers (list): The numbers

    Returns:
        list: The sorted list
    """
    max_number = max(numbers)
    size = max_number // len(numbers)
    buckets = [[] for _ in range(len(numbers) + 1)]
    for number in numbers:
        i = min(number // size, len(numbers))
        buckets[i].append(number)
    numbers = []
    for bucket in buckets:
        insertion_sort(bucket)
        numbers.extend(bucket)
    return numbers

#BONUS 11. Shell Sort

def shell_sort(numbers: list) -> list:
    """Sorts a list using shell sort

    Args:
        numbers (list): The numbers

    Returns:
        list: The sorted list
    """
    n = len(numbers)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = numbers[i]
            j = i
            while j >= gap and numbers[j - gap] > temp:
                numbers[j] = numbers[j - gap]
                j -= gap
            numbers[j] = temp
        gap //= 2
    return numbers

#BONUS 12. Comb Sort

def comb_sort(numbers: list) -> list:
    """Sorts a list using comb sort

    Args:
        numbers (list): The numbers

    Returns:
        list: The sorted list
    """
    gap = len(numbers)
    shrink = 1.3
    sorted = False
    while not sorted:
        gap = int(gap / shrink)
        if gap > 1:
            sorted = False
        else:
            gap = 1
            sorted = True
        i = 0
        while i + gap < len(numbers):
            if numbers[i] > numbers[i + gap]:
                numbers[i], numbers[i + gap] = numbers[i + gap], numbers[i]
                sorted = False
            i += 1
    return numbers

#BONUS 13. Cycle Sort

def cycle_sort(numbers: list) -> list:
    """Sorts a list using cycle sort

    Args:
        numbers (list): The numbers

    Returns:
        list: The sorted list
    """
    writes = 0
    for cycle_start in range(len(numbers) - 1):
        item = numbers[cycle_start]
        pos = cycle_start
        for i in range(cycle_start + 1, len(numbers)):
            if numbers[i] < item:
                pos += 1
        if pos == cycle_start:
            continue
        while item == numbers[pos]:
            pos += 1
        numbers[pos], item = item, numbers[pos]
        writes += 1
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, len(numbers)):
                if numbers[i] < item:
                    pos += 1
            while item == numbers[pos]:
                pos += 1
            numbers[pos], item = item, numbers[pos]
            writes += 1
    return numbers

# BONUS 14. Linear search

def linear_search(numbers: list, number: int) -> int:
    """Searches for a number in a list using linear search

    Args:
        numbers (list): The numbers
        number (int): The number to search for

    Returns:
        int: The index of the number
    """
    for i in range(len(numbers)):
        if numbers[i] == number:
            return i
    return -1

