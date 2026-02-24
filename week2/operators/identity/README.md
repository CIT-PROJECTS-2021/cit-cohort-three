# Identity Operators

Identity operators check whether two variables point to the same object in
memory.

| Operator | Meaning | Example |
| --- | --- | --- |
| `is` | same object | `x is y` |
| `is not` | different objects | `x is not y` |

## Example
```python
x1 = 5
y1 = 5
x2 = "Hello"
y2 = "Hello"
x3 = [1, 2, 3]
y3 = [1, 2, 3]

print(x1 is y1)   # True (small ints may be cached)
print(x2 is y2)   # True (strings may be interned)
print(x3 is y3)   # False (different list objects)
print(x3 == y3)   # True (same contents)
```

## Note
Use `==` to compare values. Use `is` to check identity (e.g., `x is None`).

[Next](/week2/operators/membership/README.md) | [Previous](/week2/operators/assignment/README.md)
