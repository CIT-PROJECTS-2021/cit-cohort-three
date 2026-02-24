# Bitwise Operators

Bitwise operators act on operands as if they were strings of binary digits. They operate bit by bit, hence the name.

For example, 2 is `10` in binary and 7 is `111`.

In the table below: let `x = 10` (`0000 1010`) and `y = 4` (`0000 0100`).

| Operator | Meaning | Example |
| --- | --- | --- |
| `&` | bitwise AND | `x & y` = 0 |
| `|` | bitwise OR | `x | y` = 14 |
| `^` | bitwise XOR | `x ^ y` = 14 |
| `~` | bitwise NOT | `~x` = -11 |
| `<<` | shift left | `x << 2` = 40 |
| `>>` | shift right | `x >> 2` = 2 |

## Example
```python
x = 10  # 1010
y = 4   # 0100

print(x & y)   # 0
print(x | y)   # 14
print(x ^ y)   # 14
print(~x)      # -11
print(x << 2)  # 40
print(x >> 2)  # 2
```

## Note
Python does not have the `>>>` operator (unsigned right shift).

[Previous](/week2/operators/membership/README.md)
