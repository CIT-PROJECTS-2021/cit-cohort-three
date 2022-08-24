---
description: >-
  In this Lecture, we'll learn everything about Python lists: creating lists, changing list elements, removing elements, and other list operations with the help of examples.
---

Python lists are one of the most versatile data types that allow us to work with multiple elements at once. For example,

```python
# a list of programming languages
languages = ['Python', 'Java', 'C++', 'C#', 'JavaScript']
```

**Create Python Lists**

In Python, a list is created by placing elements inside square brackets `[]`, separated by commas.

```python
# list of integers
numbers = [1, 2, 3, 4, 5]
```

A list can have any number of items and they may be of different types (integer, float, string, etc.).

```python
mixed_list = ["Apple", 12, "Banana", 45.7, False]
```

A list can also have another list as an item. This is called a nested list.

```python
nested_list = ["Apple", ["Banana", "Cherry"], "Durian"]
```

**Access List Elements**

There are various ways in which we can access the elements of a list.

List Index
We can use the index operator [] to access an item in a list. In Python, indices start at 0. So, a list having 5 elements will have an index from 0 to 4.

Trying to access indexes other than these will raise an IndexError. The index must be an integer. We can't use float or other types, this will result in TypeError.

Nested lists are accessed using nested indexing.

```python
my_list = ["Apple", "Banana", "Cherry"]

# first item in the list
my_list[0] # Apple

# second item in the list
my_list[1] # Banana

# third item in the list
my_list[2] # Cherry

# last item in the list
my_list[-1] # Cherry

nested_list = ["Apple", ["Banana", "Cherry"], "Durian"]

# first item in the list
nested_list[0] # Apple

# second item in the list
nested_list[1] # ["Banana", "Cherry"]

# first item in the nested list
nested_list[1][0] # Banana

# second item in the nested list
nested_list[1][1] # Cherry
```

**Negative indexing**

Python allows negative indexing for its sequences. The index of -1 refers to the last item, -2 to the second last item and so on.

```python
my_list = ["Apple", "Banana", "Cherry"]

# first item in the list
my_list[-3] # Apple

# second item in the list
my_list[-2] # Banana

# third item in the list
my_list[-1] # Cherry
```

<img src="https://cdn.programiz.com/sites/tutorial2program/files/python-list-index.png"><br>


**List Slicing in Python**

We can access a range of items in a list by using the slicing operator `:`.

```python
# list slicing
my_list = ["P", "y", "t", "h", "o", "n"]

# elements from index 2 to index 4
my_list[2:5] # ['t', 'h', 'o']
```

This simply means that Python will start at index 2 and go up to index 4 (but not including index 5).

```python
# list slicing
my_list = ["P", "y", "t", "h", "o", "n"]

# elements from index 2 to the end
my_list[2:] # ['t', 'h', 'o', 'n']
```

This simply means that Python will start at index 2 and go up to the last index.

```python
# list slicing
my_list = ["P", "y", "t", "h", "o", "n"]

# elements from the beginning to the end
my_list[:] # ['P', 'y', 't', 'h', 'o', 'n']
```

> **Note**: When we slice lists, the start index is inclusive but the end index is exclusive. For example, my_list[2: 5] returns a list with elements at index 2, 3 and 4, but not 5.
<br>

### Add/Change List Elements

`Lists` are mutable, meaning their elements can be changed unlike `string` or `tuple`.

We can use the assignment operator `=` to change an item or a range of items.

  
```python
# Correcting mistake values in a list
odd = [2, 4, 6, 8]

# change the value of the first item in the list
odd[0] = 1

print(odd) # [1, 4, 6, 8]

# change 2nd to 4th items
odd[1:4] = [3, 5, 7]

print(odd) # [1, 3, 5, 7, 8]
```

We can add one item to a list using the `append()` method or add several items using the `extend()` method.

```python
fruits = ["Apple", "Banana", "Cherry"]

# add one item to the end of the list
fruits.append("Durian")

print(fruits) # ['Apple', 'Banana', 'Cherry', 'Durian']

# add several items to the end of the list
fruits.extend(["Mango", "Orange"])

print(fruits) # ['Apple', 'Banana', 'Cherry', 'Durian', 'Mango', 'Orange']
```

We can also use `+` operator to combine two lists. This is also called concatenation.

The `*` operator repeats a list for the given number of times.

```python
# repeat a list for 3 times
even = [2, 4, 6, 8]

print(even * 3) # [2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8]

odd = [1, 3, 5, 7]

numbers = even + odd # [2, 4, 6, 8, 1, 3, 5, 7]
```

Furthermore, we can insert one item at a desired location by using the method `insert()` or insert multiple items by squeezing it into an empty slice of a list.

```python
fruits = ["Apple", "Banana", "Cherry"]

# insert one item at index 2
fruits.insert(2, "Durian")

print(fruits) # ['Apple', 'Banana', 'Durian', 'Cherry']

# insert multiple items at index 2
fruits.insert(2, ["Mango", "Orange"])

print(fruits) # ['Apple', 'Banana', 'Mango', 'Orange', 'Durian', 'Cherry']
```

### Delete List Elements

We can delete one or more items from a list using the Python `del statement`. It can even delete the list entirely.

```python
# delete one item from a list
fruits = ["Apple", "Banana", "Cherry"]

del fruits[1]

print(fruits) # ['Apple', 'Cherry']

# delete multiple items from a list
fruits = ["Apple", "Banana", "Cherry", "Durian", "Mango", "Orange"]

del fruits[2:4]

print(fruits) # ['Apple', 'Banana', 'Mango', 'Orange']

# delete the list entirely
del fruits

print(fruits) # NameError: name 'fruits' is not defined
```

We can use `remove()` to remove the given item or `pop()` to remove an item at the given index.

The `pop()` method removes and returns the last item if the index is not provided. This helps us implement `lists` as `stacks` (first in, last out data structure).

And, if we have to empty the whole list, we can use the `clear()` method.

```python
fruits = ["Apple", "Banana", "Cherry", "Durian", "Mango", "Orange"]

# remove the last item
fruits.pop()

print(fruits) # ['Apple', 'Banana', 'Cherry', 'Durian', 'Mango']

# remove the item at index 2
fruits.pop(2)

print(fruits) # ['Apple', 'Banana', 'Mango']

# empty the list
fruits.clear()

print(fruits) # []
```
Finally, we can also delete items in a list by assigning an empty list to a slice of elements.

```python
fruits = ["Apple", "Banana", "Cherry", "Durian", "Mango", "Orange"]

fruits = []

print(fruits) # []
```

### List Methods
Python has many useful list methods that makes it really easy to work with lists. Here are some of the commonly used list methods.

|Methods	| Descriptions|
|----------|-------------|
|`append()`|	adds an element to the end of the list|
|`extend()`|	adds all elements of a list to another list|
|`insert()`|	inserts an item at the defined index|
|`remove()`|	removes an item from the list|
|`pop()`|	returns and removes an element at the given index|
|`clear()`|	removes all items from the list|
|`index()`|	returns the index of the first matched item|
|`count()`|	returns the count of the number of items passed as an argument|
|`sort()`|	sort items in a list in ascending order|
|`reverse()`|	reverse the order of items in the list|
|`copy()`| 	returns a shallow copy of the list|

> **NOTE**: The above methods are not exaustive. There are many more methods available in the `list` module.

```python
# Example on Python list methods
fruits = ["Apple", "Banana", "Cherry", "Durian", "Mango", "Orange"]

print(fruits.count("Apple")) # 1

# Add fruit to the end
fruits.append("Kiwi")

print(fruits) # ['Apple', 'Banana', 'Cherry', 'Durian', 'Mango', 'Orange', 'Kiwi']

# Index of first occurrence of "Orange"
print(fruits.index("Orange")) # 5
```
***
### List Comprehension: Elegant way to create Lists

List comprehension is an elegant and concise way to create a new list from an existing list in Python.

A list comprehension consists of an expression followed by [for statement](../../control_flow/for_loop/README.md) inside square brackets.

Here is an example to make a list with each item being increasing power of 2.

```python
# make a list with each item being increasing power of 2
powers = [2 ** x for x in range(10)]

print(powers) # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
```

This code is equivalent to:

```python
powers = []

for x in range(10):
    powers.append(2 ** x)

print(powers) # [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
```

A list comprehension can optionally contain more for or if statements. An optional if statement can filter out items for the new list. Here are some examples.

```python
# make a list with each item being increasing power of 2 if divisible by 4
powers = [2 ** x for x in range(10) if x % 4 == 0]

print(powers) # [16, 32, 64, 128]

# a list of odd numbers
odds = [x for x in range(10) if x % 2 == 1]

# nested list comprehension
matrix = [[x for x in range(y)] for y in range(3)]

print(matrix) # [[], [0], [0, 1]]
```
***
### Other List Operations in Python
**List Membership Test**

We can test if an item exists in a list or not, using the keyword in.

```python
fruits = ["Apple", "Banana", "Cherry", "Durian", "Mango", "Orange"]

# check if "Durian" exists in the list
if "Durian" in fruits:
    print("Durian is in the list")
else:
    print("Durian is not in the list")
```

***
### Iterating Through a List
Using a for loop we can iterate through each item in a list.

```python
fruits = ["Apple", "Banana", "Cherry", "Durian", "Mango", "Orange"]

for fruit in fruits:
    print(f"I love {fruit}")
```

We can use while loop to iterate through a list as well.

```python
fruits = ["Apple", "Banana", "Cherry", "Durian", "Mango", "Orange"]

while fruits:
    fruit = fruits.pop()
    print(f"I love {fruit}")
```












Resources:

[Datastructures](https://docs.python.org/3/tutorial/datastructures.html)