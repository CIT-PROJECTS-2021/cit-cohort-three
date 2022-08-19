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

# **Output:** x + y = 19
print('x + y =',x+y)

# **Output:** x - y = 11
print('x - y =',x-y)

# **Output:** x * y = 60
print('x * y =',x*y)

# **Output:** x / y = 3.75
print('x / y =',x/y)

# **Output:** x // y = 3
print('x // y =',x//y)

# **Output:** x ** y = 50625
print('x ** y =',x**y)
```

### **Output:**

```python
x + y = 19
x - y = 11
x * y = 60
x / y = 3.75
x // y = 3
x ** y = 50625
```

### Addition

This operator is used to add two values present on either side of the operator.

**Input:**

```python
x = 2
y = 3
sum = x + y
print (sum)
```

**Output**

```python:
5
```

### Subtraction

This operator is used to subtract the value present on the right side of the operator from the value present on the left side of the operator.

**Input:**

```python
x = 5
y = 2
sub = x - y
print (sub)
```

**Output:**

```python:
3
```

### Multiplication

This operator is used to find the product of the two values present on either side of the operator.

**Input:**

```python
x = 2
y = 3
mul = x * y
print (mul)
```

**Output:**

```python:
6
```

### Division

This operator is used to find the quotient. The value present on the left side of the operator acts as a Dividend and the one on the right side is Divisor.

**Input:**

```python
x = 5
y = 2
div = x / y
print (div)
```

**Output:**

```python:
2.5
```

A division operation always results in a floating-point number.

### Modulus

This operator is used to find the remainder. The value present on the left side of the operator acts as a Dividend and the one on the right side is Divisor.

**Input:**

```python
x = 8
y = 3
mod = x % y
print (mod)

a = -5
b = 2
res1 = a % b
print (res1)

m = 5
n = -2
res2 = m % n
print (res2)
```

**Output:**

```python:
2
-1
1
```

The remainder will be positive if the Dividend is positive and vice-versa.
Even if the Divisor is negative but the Dividend is positive, the remainder will be positive.

### Exponentiation

This operator is used to raise the first value to the power of the second operator

**Input:**

```python
x = 2
y = 3
exp = x ** y
print (exp)
```

**Output:**

```python:
8
```

### Floor division

The Floor Division operator is used to floor the result to the nearest integer.

**Input:**

```python
x = 5
y = 2
flo = x // y
print (flo)
```

**Output:**

```python:
2.0
```

### Order of precedence of Arithmetic operators in Python

Arithmetic Operators in Python follow a basic order of precedence.
When more than one operator is used, they are executed according to this order:

| Operator     | Purpose                                             |
| ------------ | --------------------------------------------------- |
| ()           | Parentheses                                         |
| \*\*         | Exponentiation                                      |
| %, \*, /, // | Modulus, Multiplication, Division, Integer Division |
| +, -         | Addition, Subtraction                               |

> **Note:** The operator listed at the top of the table will be executed first.

**Input:**

```python
print (((5 + 4) / 3) * 2)
```

**Output:**

```python:
6
```

Here, as you can see according to the order of precedence, Parentheses will be computed first. So inside the innermost parenthesis, there is an addition operator.

Closing Thoughts on Arithmetic Operators in Python
We discussed 7 different types of Arithmetic operators in Python. Make sure you remember the order of precedence because that affects the outcome of all operations performed in Python.
