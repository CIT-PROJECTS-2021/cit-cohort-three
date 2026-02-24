---
description: >-
  Learn how exceptions work and how to handle them safely.
---

# Exceptions

Exceptions are runtime errors that stop normal program flow. You can handle
them with `try` and `except`.

## Basic Example
```python
try:
    value = int("abc")
except ValueError:
    print("Not a number")
```

## Catch Multiple Exceptions
```python
try:
    result = 10 / 0
except (ZeroDivisionError, TypeError):
    print("Bad operation")
```

## `else` and `finally`
```python
try:
    num = int("5")
except ValueError:
    print("Invalid")
else:
    print("Valid")
finally:
    print("Always runs")
```

## Raising Exceptions
```python
def positive_only(n: int) -> int:
    if n <= 0:
        raise ValueError("n must be positive")
    return n
```

[Next](/week3/oop/README.md) | [Previous](/week3/functions/python_recursion/README.md)
