# Logical Operators

Logical operators combine boolean expressions.

| Operator | Meaning | Example |
| --- | --- | --- |
| `and` | true if both operands are true | `x > 0 and y > 0` |
| `or` | true if either operand is true | `x > 0 or y > 0` |
| `not` | inverts truth value | `not is_valid` |

## Example
```python
x = True
y = False

print(x and y)  # False
print(x or y)   # True
print(not x)    # False
```

## Truth Tables
`and`
| A | B | A and B |
| --- | --- | --- |
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

`or`
| A | B | A or B |
| --- | --- | --- |
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

`not`
| A | not A |
| --- | --- |
| True | False |
| False | True |

[Next](/week2/operators/assignment/README.md) | [Previous](/week2/operators/comparison/README.md)
