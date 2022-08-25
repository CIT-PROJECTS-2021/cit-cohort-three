---
description: >-
    In this lecture, you'll learn everything about Python tuples. More specifically, what are tuples, how to create them, when to use them and various methods you should be familiar with.
---

A tuple in Python is similar to a [list](../python_lists/README.md). The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas we can change the elements of a list.

***
### Creating a Tuple

A tuple is created by placing all the items (elements) inside parentheses `()`, separated by commas. The parentheses are optional, however, it is a good practice to use them.

A tuple can have any number of items and they may be of different types (integer, float, list, string, etc.).

```python
# Different types of tuples
empty_tuple = ()

tuple_with_ints = (1, 2, 3)

tuple_with_floats = (1.1, 2.2, 3.3)

tuple_with_strings = ("a", "b", "c")

tuple_with_lists = ([1, 2, 3], [4, 5, 6], [7, 8, 9])

tuple_with_tuples = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

mix_tuple = (1, 2.2, "a", [1, 2, 3], (1, 2, 3))
```

A tuple can also be created without using parentheses. This is known as tuple packing.

```python
animals = "cat", "dog", "rabbit"

# tuple unpacking is also possible
cat, dog, rabbit = animals

print(cat) # cat
print(dog) # dog
print(rabbit) # rabbit
```

Creating a tuple with one element is a bit tricky.

Having one element within parentheses is not enough. We will need a trailing comma to indicate that it is, in fact, a tuple.

```python
single_element_tuple = (1)

print(type(single_element_tuple)) # <class 'int'>

# Creating a tuple having one element
single_element_tuple = (1,)

print(type(single_element_tuple)) # <class 'tuple'>

# Parentheses is optional
single_element_tuple = 1,

```
***
### Access Tuple Elements
There are various ways in which we can access the elements of a tuple.

1. **Indexing**

    We can use the index operator `[]` to access an item in a tuple, where the index starts from 0.

    So, a tuple having `6` elements will have indices from `0` to `5`. Trying to access an index outside of the tuple index range(6,7,... in this example) will raise an `IndexError`.

    The index must be an integer, so we cannot use float or other types. This will result in `TypeError`.

    Likewise, nested tuples are accessed using nested indexing, as shown in the example below.

    ```python
    # Accessing tuple elements using indexing
    tuple_with_ints = (1, 2, 3)
    print(tuple_with_ints[0]) # 1
    print(tuple_with_ints[1]) # 2
    print(tuple_with_ints[2]) # 3

    # IndexError: list index out of range
    print(tuple_with_ints[3])

    # Accessing nested tuples
    tuple_with_tuples = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
    print(tuple_with_tuples[0][0]) # 1
    print(tuple_with_tuples[1][1]) # 5
    print(tuple_with_tuples[2][2]) # 9
    
    ```

2. **Negative Indexing**

    Python allows negative indexing for its sequences.

    The index of `-1` refers to the last item, `-2` to the second last item and so on.

    ```python
    # Negative indexing for accessing tuple elements
    tuple_with_ints = (1, 2, 3)
    print(tuple_with_ints[-1]) # 3
    ```

3. **Slicing**

    We can access a range of items in a tuple by using the slicing operator colon `:`.

    The start index is inclusive and the end index is exclusive.

    ```python
    # Accessing a range of items in a tuple
    tuple_with_ints = (1, 2, 3, 4, 5)
    print(tuple_with_ints[1:3]) # (2, 3)
    print(tuple_with_ints[:3]) # (1, 2, 3)
    print(tuple_with_ints[3:]) # (4, 5)
    ```
***
### Changing a Tuple

Unlike lists, tuples are immutable.

This means that elements of a tuple cannot be changed once they have been assigned. But, if the element is itself a mutable data type like a list, its nested items can be changed.

We can also assign a tuple to different values (reassignment).
    
```python
# Changing tuple values
my_tuple = (4, 2, 3, [6, 5])


# TypeError: 'tuple' object does not support item assignment
# my_tuple[1] = 9

# However, item of mutable element can be changed
my_tuple[3][0] = 7
print(my_tuple) # (4, 2, 3, [7, 5])

# Tuples can be reassigned
my_tuple = (4, 2, 3, [6, 5])
my_tuple = (7, 2, 3, [6, 5])
print(my_tuple) # (7, 2, 3, [6, 5])
```

We can use `+` operator to combine two tuples. This is called concatenation.

We can also repeat the elements in a tuple for a given number of times using the `*` operator.

Both `+` and `*` operations result in a new tuple.

```python
# Concatenating two tuples
tuple_1 = (1, 2, 3)
tuple_2 = (4, 5, 6)

print(tuple_1 + tuple_2) # (1, 2, 3, 4, 5, 6)

# Repeating a tuple
tuple_1 = ("Hello",)
print(tuple_1 * 3) # ('Hello', 'Hello', 'Hello')
```

### Deleting a Tuple
As discussed above, we cannot change the elements in a tuple. It means that we cannot delete or remove items from a tuple.

Deleting a tuple entirely, however, is possible using the keyword `del`.

```python
# Deleting tuples
my_tuple = (1, 2, 3)

del my_tuple[1] # TypeError: 'tuple' object doesn't support item deletion

del my_tuple 

print(my_tuple) # NameError: name 'my_tuple' is not defined
```

***
### Tuple Methods

Methods that add items or remove items are not available with tuple. Only the following two methods are available.

Some examples of Python tuple methods:

```python
# Counting the number of times an item occurs in a tuple
my_tuple = ('a', 'p', 'p', 'l', 'e', 'p', 'l', 'e')

print(my_tuple.count('p')) # 3
```

Below is a list of Python tuple methods.

| Method | Description |
| ------ | ----------- |
| `len()` | Returns the length of the tuple |
| `max()` | Returns the largest item in the tuple |
| `min()` | Returns the smallest item in the tuple |
| `sum()` | Returns the sum of all the items in the tuple |
| `index()` | Returns the index of the first occurrence of an item in the tuple |
| `count()` | Returns the number of times an item occurs in the tuple |

***
### Other Tuple Operations
1. **Tuple Membership Test**

    We can test if an item exists in a tuple or not, using the keyword `in`.

    ```python
    # Testing if an item exists in a tuple
    my_tuple = (1, 2, 3)
    print('1' in my_tuple) # True
    print('4' in my_tuple) # False
    ```

2. **Iterating Through a Tuple**

    We can use a for loop to iterate through each item in a tuple.

    ```python
    # Iterating through a tuple
    my_tuple = (1, 2, 3)
    for item in my_tuple:
        print(item) # 1 2 3
    ```

***
### Advantages of Tuple over List

Since tuples are quite similar to lists, both of them are used in similar situations. However, there are certain advantages of implementing a tuple over a list. Below listed are some of the main advantages:

- We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.
- Since tuples are immutable, iterating through a tuple is faster than with list. So there is a slight performance boost.
- Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.
- If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.


