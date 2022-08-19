# Comparison operators

Comparison operators are used to compare values.
It returns either `True` or `False` according to the condition.

| Operator | Meaning                                                                               | Example        |
| -------- | ------------------------------------------------------------------------------------- | -------------- |
| ==       | Equal to - True if both operands are equal                                            | 5 == 3 = False |
| !=       | Not equal to - True if operands are not equal                                         | 5 != 3 = True  |
| >        | Greater than - True if left operand is greater than the right                         | 5 > 3 = False  |
| <        | Less than - True if left operand is less than the right                               | 5 < 3 = True   |
| >=       | Greater than or equal to - True if left operand is greater than or equal to the right | 5 >= 3 = False |
| <=       | Less than or equal to - True if left operand is less than or equal to the right       | 5 <= 3 = True  |

### Example 1: Comparison operators in Python

```python
x = 10
y = 12

# **Output:** x > y is False
print('x > y is',x>y)

# **Output:** x < y is True
print('x < y is',x<y)

# **Output:** x == y is False
print('x == y is',x==y)

# **Output:** x != y is True
print('x != y is',x!=y)

# **Output:** x >= y is False
print('x >= y is',x>=y)

# **Output:** x <= y is True
print('x <= y is',x<=y)
```

### **Output:**

```python
x > y is False
x < y is True
x == y is False
x != y is True
x >= y is False
x <= y is True
```

### Greater than

Denoted by `>`, the greater than operator checks if the value on the left side is greater than the value on the right side. It returns True if the condition is satisfied, otherwise returns False.

**Intput:**

```python
x = 5
y = 10
res = x > y
res1 = y > x
print (res)
print (res1)
```

**Output:**

```python
FALSE
TRUE
```

### Less than

The less than operator is denoted by `<` sign and compares the values present on either side. If the value present on the left side is smaller than the value on the right side, it returns True otherwise it returns False.

**Intput:**

```python
x = 5
y = 10
res = x < y
res1 = y < x
print (res)
print (res1)
```

**Output:**

```python
TRUE
FALSE
```

If you compare two different data types, for example, `int (5)` and `float (5.0)`, both greater than and less than operator will return `False` as both values are equal.
And when comparing strings like, “Nick” and “nick”, the operators compare their ASCII values. Since the ASCII value of `“A”` is `65` and `“a”` is `97`, `“nick”` is greater than `“Nick”`.

### Equal to

This operator is denoted by `==` and it returns `True` if both the values present on either side are equal.

**Intput:**

```python
x = 5
y = 5
z = ‘5’
res = x == y
res2 = x == z
print (res)
print (res2)
```

**Output:**

```python
TRUE
FALSE
```

This operator returns `False` when `x` and `z` are compared and that is because `x` is an integer and `z` is a string. Hence, they are unequal.

### Not equal to

Symbolic representation of Not equal to operator is `!=` and it returns `True` if one value is not equal to the other present in the condition.

**Intput:**

```python
x = 5
y = 10
res = x != y
print (res)
```

**Output:**

```python
FALSE
```

### Greater than or equal to

This operator `(>=)` only returns `True` if the value on the left side is greater or equal to the value on the right side.

**Intput:**

```python
x = 5
y = 5
z = 10
res = x >= y
res2 = x >= z
print (res)
print (res2)
```

**Output:**

```python
TRUE
FALSE
```

### Less than or equal to

The last operator in the list is less than or equal to `(<=)`. It compares the values and returns True if the value on the left side is smaller than or equal to the value to the value on the right side.

**Intput:**

```python
x = 5
y = 5
z = 10
res = x <= y
res1 = x <= z
print (res)
print (res1)
```

**Output:**

```python
TRUE
TRUE
```

We can also compare Tuples with these operators. The Tuple with more elements will be greater and if both have the same number of elements then the operator compares elements with each other.

**Intput:**

```python
tup1 = (1,2,3)
tup2 = (1,2,3)
tup3 = (1,2)
tup4 = (1,5,3)
print (tup1 == tup2)
print (tup3 <= tup1)
print (tup1 >= tup4)
```

**Output:**

```python
TRUE
TRUE
FALSE
```

In the 3rd case, the `tup1` and `tup4` have the same number of elements. Then, the operator compares elements. It compares the first element (1 and 1). Since both are equal, it moves to the second element (2 and 5). Now that 5 is greater than 2, it stops here and returns `False`.

Closing Thoughts
We discussed 6 different types of Comparison operators in Python. The comparison operators compare the value and return a boolean value.
