# Arithmetic operators

Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, etc.

| Operator | Meaning                                                          | Example                    |
| -------- | ---------------------------------------------------------------- | -------------------------- |
| +        | Add two operands or unary plus                                   | 5 + 3 = 8                  |
| -        | Subtract right operand from the left or unary minus              | 5 - 3 = 2                  |
| \*       | Multiply two operands                                            | 5 \* 3 = 15                |
| /        | Divide left operand by the right one (always results into float) | 5 / 3 = 1.6666666666666667 |
| //       | Integer division (results into integer)                          | 5 // 3 = 1                 |
| %        | Modulus - remainder of the division of left operand by the right | 5 % 3 = 2                  |
| \*\*     | Exponentiation - left operand to the power of right operand      | 5 \*\* 3 = 125             |

### Example 1: Arithmetic operators in Python

```python
x = 15
y = 4

# Output: x + y = 19
print('x + y =',x+y)

# Output: x - y = 11
print('x - y =',x-y)

# Output: x * y = 60
print('x * y =',x*y)

# Output: x / y = 3.75
print('x / y =',x/y)

# Output: x // y = 3
print('x // y =',x//y)

# Output: x ** y = 50625
print('x ** y =',x**y)
```

### Output:

```python
x + y = 19
x - y = 11
x * y = 60
x / y = 3.75
x // y = 3
x ** y = 50625
```
