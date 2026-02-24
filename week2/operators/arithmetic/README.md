# Arithmetic Operators

Arithmetic operators perform mathematical operations.

| Operator | Meaning | Example |
| --- | --- | --- |
| `+` | addition | `5 + 3` |
| `-` | subtraction | `5 - 3` |
| `*` | multiplication | `5 * 3` |
| `/` | division (float) | `5 / 2` |
| `//` | floor division | `5 // 2` |
| `%` | remainder | `5 % 2` |
| `**` | exponentiation | `5 ** 2` |

## Example
```python
x = 15
y = 4

print(x + y)   # 19
print(x - y)   # 11
print(x * y)   # 60
print(x / y)   # 3.75
print(x // y)  # 3
print(x % y)   # 3
print(x ** y)  # 50625
```

## Notes
- `/` always returns a float.
- `%` has the same sign as the divisor.
- `**` has higher precedence than `*`, `/`, and `+`.

## Precedence (Highest to Lowest)
1. Parentheses `()`
2. Exponentiation `**`
3. Multiplication, division, floor division, modulo `* / // %`
4. Addition, subtraction `+ -`

```python
print(((5 + 4) / 3) * 2)  # 6.0
```

[Next](/week2/operators/comparison/README.md) | [Previous](/week2/operators/README.md)
