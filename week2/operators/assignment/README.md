# Assignment Operators

Assignment operators are used in Python to assign values to variables.

`a = 5` assigns the value `5` to the variable `a`.

Compound operators like `a += 5` update the variable in place and are
equivalent to `a = a + 5`.

| Operator | Example | Equivalent to |
| --- | --- | --- |
| `=` | `a = 5` | `a = 5` |
| `+=` | `a += 5` | `a = a + 5` |
| `-=` | `a -= 5` | `a = a - 5` |
| `*=` | `a *= 5` | `a = a * 5` |
| `/=` | `a /= 5` | `a = a / 5` |
| `%=` | `a %= 5` | `a = a % 5` |
| `//=` | `a //= 5` | `a = a // 5` |
| `**=` | `a **= 5` | `a = a ** 5` |
| `&=` | `a &= 5` | `a = a & 5` |
| `|=` | `a |= 5` | `a = a | 5` |

## Example
```python
x = 10
x += 3
x *= 2
print(x)  # 26
```

[Next](/week2/operators/identity/README.md) | [Previous](/week2/operators/logical/README.md)


