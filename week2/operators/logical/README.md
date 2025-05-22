# Logical operators

In Python, Logical operators are used on conditional statements (either `True` or `False`). They perform Logical `AND`, Logical `OR` and Logical `NOT` operations.

| Operator | Meaning                                      | Example                |
| -------- | -------------------------------------------- | ---------------------- |
| and      | Logical AND - True if both operands are true | 5 > 3 and 3 > 2 = True |
| or       | Logical OR - True if either operand is true  | 5 > 3 or 3 > 2 = True  |
| not      | Logical NOT - True if operand is false       | not 5 > 3 = False      |

#### Example 1: Logical operators in Python

```python
x = True
y = False

print(f'x and y is {x and y}')

print(f'x or y is {x or y}')

print(f'not x is {not x}')
```

**Output:**

```
x and y is False
x or y is True
not x is False
```

`and` will result into `True` only if both the operands are `True`

The truth table for `and` is given below:

| A     | B     | A and B |
| ----- | ----- | ------- |
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

`or` will result into `True` if any of the operands is `True`.

The truth table for or is given below:

| A     | B     | A or B |
| ----- | ----- | ------ |
| True  | True  | True   |
| True  | False | True   |
| False | True  | True   |
| False | False | False  |

`not` operator is used to invert the truth value.

The truth table for `not` is given below:

| A     | not A |
| ----- | ----- |
| True  | False |
| False | True  |

some example of their usage are given below

```python
>>> True and False
False
>>> True or False
True
>>> not False
True
```
