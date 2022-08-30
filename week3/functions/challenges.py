# 1. Write a function that takes an integer minutes and converts it to seconds.

def convert_min_to_sec(minutes: int) -> int:
    return minutes * 60

print(convert_min_to_sec(5))

# 2. Write a function that takes the base and height of a triangle and return its area.

def tri_area(base, height):
    return base * height / 2

print(tri_area(5, 6))

# 3. Write a function that takes a list of numbers and returns a list with two elements:
# The first element should be the sum of all even numbers in the list.
# The second element should be the sum of all odd numbers in the list.

def sum_even_odd(numbers: list) -> list:
    if not isinstance(numbers, list):
        raise ValueError("Please provide a valid list")

    even_sum = 0
    odd_sum = 0

    for number in numbers:
        if number % 2 == 0:
            even_sum += number
        else:
            odd_sum += number

    return [even_sum, odd_sum]

print(sum_even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 4. In cricket, an over consists of six deliveries a bowler bowls from one end. Create a function that takes the number of balls bowled by a bowler and calculates the number of overs and balls bowled by him/her. Return the value as a float, in the format overs.balls.

def overs_balls(balls: int) -> float:
    if not isinstance(balls, int):
        raise ValueError("Please provide a valid number")

    return balls / 6

print(overs_balls(2400))


# 5. Create a function that takes two numbers as arguments (num, length) and returns a list of multiples of num until the list length reaches length.

def multiples(num: int, length: int) -> list:
    if not isinstance(num, int) or not isinstance(length, int):
        raise ValueError("Please provide a valid number")

    return [num * i for i in range(1, length + 1)]

print(multiples(7, 5))


# 6. Given a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.

def pluralize(words: list) -> set:
    if not isinstance(words, list):
        raise ValueError("Please provide a valid list")

    return set([word + "s" for word in words if words.count(word) > 1])

print(pluralize(["cat", "dog", "cat", "mouse", "dog"]))

# 7. Create a function that takes a string's characters as ASCII and returns each character's hexadecimal value as a string.

def hex_values(string: str) -> list:
    if not isinstance(string, str):
        raise ValueError("Please provide a valid string")

    return [hex(ord(char)) for char in string]

print(hex_values("hello world"))

"""
8. Create a function that takes a dictionary of objects like { "name": "John", "notes": [3, 5, 4] } and returns a dictionary of objects like { "name": "John", "top_note": 5 }.
"""

def top_note(dictionary: dict) -> dict:
    if not isinstance(dictionary, dict):
        raise ValueError("Please provide a valid dictionary")

    for key, value in dictionary.items():
        if isinstance(value, list):
            dictionary[key] = max(value)

    # change note key
    dictionary["top_note"] = dictionary.pop("notes")
    return dictionary


print(top_note({ "name": "John", "notes": [3, 5, 4] }))


"""
9. Make a function that encrypts a given input with these steps:

Input: "apple"

Step 1: Reverse the input: "elppa"

Step 2: Replace all vowels using the following chart:

a => 0
e => 1
i => 2
o => 2
u => 3

# "1lpp0"
Step 3: Add "aca" to the end of the word: "1lpp0aca"

Output: "1lpp0aca"
"""

def encrypt(string: str) -> str:
    if not isinstance(string, str):
        raise ValueError("Please provide a valid string")

    return string[::-1].translate(str.maketrans("aeiou", "01223")) + "aca"

print(encrypt("banana"))
print(encrypt("burak"))


# create a function to reverse a string

def reverse_string(string: str) -> str:
    return string[::-1]

print(reverse_string("Hello World"))    