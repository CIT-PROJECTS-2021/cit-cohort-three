Python language offers some special types of operators like the identity operator or the membership operator. They are described below with examples.


is and is not are the identity operators in Python. They are used to check if two values (or variables) are located on the same part of the memory. Two variables that are equal does not imply that they are identical.

| Operator	| Meaning |	Example |
| -----------| ------- | ------- |
|is	| True if the operands are identical (refer to the same object) |	x is True |
|is not |	True if the operands are not identical (do not refer to the same object)|	x is |not True |

### Example

```python
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)
```

**Output**

```python
False
True
False
```

Here, we see that `x1` and `y1` are integers of the same values, so they are equal as well as identical. Same is the case with `x2` and `y2` (strings).

But `x3` and `y3` are lists. They are equal but not identical. It is because the interpreter locates them separately in memory although they are equal.