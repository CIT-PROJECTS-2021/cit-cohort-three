# Bitwise operators

Bitwise operators act on operands as if they were strings of binary digits. They operate bit by bit, hence the name.

For example, 2 is `10` in binary and 7 is `111`.

In the table below: Let `x` = 10 (`0000 1010` in binary) and y = 4 (`0000 0100` in binary)

| Operator | Meaning | Example |
| -------- | ------- | ------- |
| &        | Bitwise AND | x & y = 0 (`0000 0000` in binary) |
| |        | Bitwise OR | x | y = 14 (`0000 1110` in binary) |
| ^        | Bitwise XOR | x ^ y = 14 (`0000 1110` in binary) |
| ~        | Bitwise NOT | ~x = -11 (`1111 0101` in binary) |
| <<       | Shift left | x << 2 = 40 (`0010 1000` in binary) |
| >>       | Shift right | x >> 2 = 2 (`0000 0010` in binary) |
| >>>      | Shift right with zero fill | x >>> 2 = 2 (`0000 0010` in binary) |

