# Comparison Operators

Comparison operators compare values and return `True` or `False`.

| Operator | Meaning | Example |
| --- | --- | --- |
| `==` | equal to | `5 == 3` |
| `!=` | not equal to | `5 != 3` |
| `>` | greater than | `5 > 3` |
| `<` | less than | `5 < 3` |
| `>=` | greater than or equal | `5 >= 3` |
| `<=` | less than or equal | `5 <= 3` |

## Example
```python
x = 10
y = 12

print(x > y)   # False
print(x < y)   # True
print(x == y)  # False
print(x != y)  # True
print(x >= y)  # False
print(x <= y)  # True
```

## Notes
- Numbers of different numeric types can be compared (`5` and `5.0`).
- Strings are compared lexicographically (dictionary order).
- Tuples are compared element by element from left to right.

```python
print((1, 2, 3) > (1, 2))   # True
print((1, 2, 3) > (1, 5))   # False
```

[Next](/week2/operators/logical/README.md) | [Previous](/week2/operators/arithmetic/README.md)
