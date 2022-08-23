In this chapter you will learn to create, format, modify and delete strings in Python. Also, you will be introduced to various string operations and functions and methods.

**What is String in Python?**

A string is a sequence of characters.

A character is simply a symbol. For example, the English language has 26 characters.

Computers do not deal with characters, they deal with numbers (binary). Even though you may see characters on your screen, internally it is stored and manipulated as a combination of 0s and 1s.

This conversion of character to a number is called encoding, and the reverse process is decoding. ASCII and Unicode are some of the popular encodings used.

In Python, a string is a sequence of Unicode characters. Unicode was introduced to include every character in all languages and bring uniformity in encoding. You can learn about Unicode from Python Unicode.

### **How to create a string in Python?**

Strings can be created by enclosing characters inside a single quote or double-quotes. Even triple quotes can be used in Python but generally used to represent multiline strings and docstrings.

```python
# defining strings in Python
# all of the following are equivalent
my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)
```

When you run the program, the output will be:

```python
Hello
Hello
Hello
Hello, welcome to
the world of Python
```

### **How to access characters in a string?**

We can access individual characters using `indexing` and a range of characters using `slicing`. Index starts from `0`. 

Trying to access a character out of index range will raise an `IndexError`. The index must be an integer. We can't use floats or other types, this will result into `TypeError`.

Python allows negative indexing for its sequences.

The index of `-1` refers to the last item, `-2` to the second last item and so on. We can access a range of items in a string by using the slicing operator `:`(colon).

```python
# accessing characters in a string
my_string = 'Hello'
print(my_string[0]) # prints H
print(my_string[1]) # prints e
print(my_string[2]) # prints l
print(my_string[3]) # prints l
print(my_string[4]) # prints o
print(my_string[-1]) # prints o
print(my_string[-2]) # prints l
print(my_string[-3]) # prints l
print(my_string[-4]) # prints e
print(my_string[-5]) # prints H

# slicing a string
# first character
print(my_string[0:1]) # prints H

# last character
print(my_string[-1:]) # prints o

# first two characters
print(my_string[0:2]) # prints He
```


Slicing in lay terms means to extract a part of a sequence.

Example:

```python
my_string = 'I love Python'
print(my_string[0:5]) # prints I love
print(my_string[6:]) # prints Python
```

This means that we can extract a part of a string starting from index `0` to index `5` and from index `6` to the end.

If we try to access an index out of the range or use numbers other than an integer, we will get errors.

Example:

```python
my_string = 'I love Python'
print(my_string[15]) # IndexError: string index out of range

print(my_string[1.5]) # TypeError: string indices must be integers
```

Slicing can be best visualized by considering the index to be between the elements as shown below.

If we want to access a range, we need the index that will slice the portion from the string.

Example:

```python
my_string = 'Python'
```

| Index | Element | Negative Index |
|-------|---------|---------------|
| 0     | P       | -6            |
| 1     | y       | -5            |
| 2     | t       | -4            |
| 3     | h       | -3            |
| 4     | o       | -2            |
| 5     | n       | -1            |


### **How to change or delete a string?**

Strings are immutable. We can't change a string by assigning a new value to it. 

```python
# changing a string
my_string = 'Hello'
my_string[0] = 'P' # TypeError: 'str' object does not support item assignment
```

We cannot delete or remove characters from a string. But deleting the string entirely is possible using the `del` keyword.

```python
# deleting a string
my_string = 'Hello'
del my_string # NameError: name 'my_string' is not defined

del my_string[0] # TypeError: 'str' object doesn't support item deletion
```

The reason for this is that strings are immutable.

### Python String Operations

There are many operations that can be performed with strings which makes it one of the most used data types in Python.


**Concatenation of Two or More Strings**

Joining of two or more strings into a single one is called concatenation.

The `+` operator does this in Python. Simply writing two string literals together also concatenates them.

The `*` operator can be used to repeat the string for a given number of times.

```python
# concatenating two strings
my_string = 'Hello' + ' ' + 'World'
print(my_string) # prints Hello World

# repeating a string
my_string = 'Hello' * 3
print(my_string) # prints HelloHelloHello
```

Writing two string literals together also concatenates them like `+` operator.

If we want to concatenate strings in different lines, we can use parentheses.

```python
# concatenating two strings
my_string = ('Hello'  
            'World') # parentheses are used to concatenate strings in different lines
print(my_string) # prints Hello World
```

**Iterating Through a string**

We can iterate through a string using a for loop. Here is an example to count the number of 'l's in a string.

```python
# counting the number of 'l's in a string
my_string = 'Hello World'
count = 0
for letter in my_string:
    if letter == 'l':
        count += 1
print(count) # prints 2
```

**String Membership Test**

We can test if a substring exists within a string or not, using the keyword in.

```python
# testing if a substring exists within a string
my_string = 'Hello World'
if 'World' in my_string:
    print('Yes') # prints Yes if World exists in the string
else:
    print('No') # prints No if World doesn't exist in the string
```

**Built-in functions to Work with Python**

Various built-in functions that work with sequence work with strings as well.

Some of the commonly used ones are `enumerate()` and `len()`. The `enumerate()` function returns an enumerate object. It contains the index and value of all the items in the string as pairs. This can be useful for iteration.

Similarly, `len()` returns the length (number of characters) of the string.

```python
# enumerating a string
my_string = 'Hello World'
print(list(enumerate(my_string))) # prints [(0, 'H'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o'), (5, ' '), (6, 'W'), (7, 'o'), (8, 'r'), (9, 'l'), (10, 'd')]

# getting the length of a string
print(len(my_string)) # prints 11
```

### Python String Formatting

**Escape Sequence**

If we want to print a text like `He said, "What's there?"`, we can neither use single quotes nor double quotes. This will result in a `SyntaxError` as the text itself contains both single and double quotes.

```python
print("He said, "What's there?"") # SyntaxError: invalid syntax
```

One way to get around this problem is to use triple quotes. Alternatively, we can use escape sequences.

An escape sequence starts with a backslash and is interpreted differently. 

If we use a single quote to represent a string, all the single quotes inside the string must be escaped. Similar is the case with double quotes. 

Here is how it can be done to represent the above text.

```python
print('''He said, "What's there?"''') # prints He said, "What's there?"

print("He said, \"What's there?\"") # prints He said, "What's there?"

print('He said, "What\'s there?"') # prints He said, "What's there?"
```

Here is a list of all the escape sequences supported by Python.

| Escape Sequence | Description |
|-----------------|-------------|
| \\n              | Newline    |
| \\t              | Tab        |
| \\b              | Backspace  |
| \\f              | Formfeed   |
| \\r              | Carriage Return |
| \\'               | Single Quote |
| \\"               | Double Quote |
| \\              | Backslash   |
|                 |              |

Examples:

```python
print('Hello\nWorld') # prints Hello
                          # World

print('Hello\tWorld') # prints Hello
                            # World

print('Hello\bWorld') # prints HellWorld
```


**The `format()` Method for Formatting Strings**

The `format()` method that is available with the string object is very versatile and powerful in formatting strings. Format strings contain curly braces `{}` as placeholders or replacement fields which get replaced.

We can use positional arguments or keyword arguments to specify the order.

```python
# Python string format() method

# default(implicit) order
print('{} {} {}'.format('Hello', 'World', '!')) # prints Hello World !

# positional arguments
print('{2} {0} {1}'.format('Hello', 'World', '!')) # prints ! Hello World

# keyword arguments
print('{greeting} {name}'.format(greeting='Hello', name='World')) # prints Hello World
```

The `format()` method can have optional format specifications. They are separated from the field name using colon. For example, we can left-justify `<`, right-justify `>` or center ^ a string in the given space.

We can also format integers as binary, hexadecimal, etc. and floats can be rounded or displayed in the exponent format. There are tons of formatting you can use. 

```python
# formatting integers
print('{:d}'.format(10)) # prints 10

# formatting binary
print('{:b}'.format(10)) # prints 1010

# formatting hexadecimal
print('{:x}'.format(10)) # prints a

# formatting floating point numbers
print('{:.2f}'.format(10.12345)) # prints 10.12

# formatting exponent
print('{:e}'.format(10.12345)) # prints 1.012345e+01

# string alignment
print('{:<30}'.format('Hello')) # prints Hello               (left-justified)
print('{:>30}'.format('Hello')) # prints                 Hello (right-justified)
print('{:^30}'.format('Hello')) # prints    Hello          (center-aligned)
```

**Old style formatting**

We can even format strings like the old `sprintf()` style used in C programming language. We use the `%` operator to accomplish this.

```python
# old style formatting
print('%s %s' % ('Hello', 'World')) # prints Hello World
```

**Common Python String Methods**

There are numerous methods available with the string object. The `format()` method that we mentioned above is one of them. Some of the commonly used methods are `lower()`, `upper()`, `join()`, `split()`, `find()`, `replace()` etc

```python
# lower()
print('Hello'.lower()) # prints hello

# upper()
print('Hello'.upper()) # prints HELLO

# join()
print(' '.join(['Hello', 'World'])) # prints Hello World

# split()
print('Hello World'.split()) # prints ['Hello', 'World']

# find()
print('Hello World'.find('World')) # prints 6

# replace()
print('Hello World'.replace('World', 'Universe')) # prints Hello Universe
```

Here is a table of all the string methods.

| Method | Description |
|--------|-------------|
| `lower()` | Converts a string to lowercase |
| `upper()` | Converts a string to uppercase |
| `join()` | Joins the elements of a sequence to the string |
| `split()` | Splits the string into a list of substrings |
| `find()` | Searches the string for a specified value and returns the index of the first occurrence |
| `replace()` | Replaces a specified value with another value in a string |
| `format()` | Formats specified values into a string |
| `strip()` | Removes whitespace from both ends of a string |
| `lstrip()` | Removes whitespace from the left end of a string |
| `rstrip()` | Removes whitespace from the right end of a string |
| `startswith()` | Returns true if the string starts with the specified value |
| `endswith()` | Returns true if the string ends with the specified value |
| `isdigit()` | Returns true if the string contains only digits |
| `isalpha()` | Returns true if the string contains only alphabetic characters |
| `isalnum()` | Returns true if the string contains only alphanumeric characters |
| `isspace()` | Returns true if the string contains only whitespace |
| `islower()` | Returns true if the string contains only lowercase characters |
| `isupper()` | Returns true if the string contains only uppercase characters |
| `istitle()` | Returns true if the string contains only titlecase characters |
| `isdecimal()` | Returns true if the string contains only decimal characters |
| `isnumeric()` | Returns true if the string contains only numeric characters |
| `isidentifier()` | Returns true if the string is a valid identifier |
| `isprintable()` | Returns true if the string contains only printable characters |
| `isascii()` | Returns true if the string contains only ASCII characters |
| `isunicode()` | Returns true if the string contains only Unicode characters |
| `isnumeric()` | Returns true if the string contains only numeric characters |

> Note: The above table is not exhaustive.

