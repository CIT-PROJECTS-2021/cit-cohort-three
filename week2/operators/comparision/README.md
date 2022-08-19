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

# Output: x > y is False
print('x > y is',x>y)

# Output: x < y is True
print('x < y is',x<y)

# Output: x == y is False
print('x == y is',x==y)

# Output: x != y is True
print('x != y is',x!=y)

# Output: x >= y is False
print('x >= y is',x>=y)

# Output: x <= y is True
print('x <= y is',x<=y)
```

### Output:

```python
x > y is False
x < y is True
x == y is False
x != y is True
x >= y is False
x <= y is True
```
