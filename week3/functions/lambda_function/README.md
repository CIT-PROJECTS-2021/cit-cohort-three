---
description: >-
  Learn how to write short anonymous functions using lambda.
---

# Lambda Functions

A `lambda` is a small, anonymous function with a single expression.

## Syntax
```python
lambda arguments: expression
```

## Example
```python
double = lambda x: x * 2
print(double(5))  # 10
```

This is similar to:
```python
def double(x):
    return x * 2
```

## Common Uses
`lambda` is often used with higher‑order functions like `map()` and `filter()`.

```python
nums = [1, 2, 3, 4, 5]

evens = list(filter(lambda x: x % 2 == 0, nums))
doubled = list(map(lambda x: x * 2, nums))

print(evens)    # [2, 4]
print(doubled)  # [2, 4, 6, 8, 10]
```

[Next](/week3/functions/python_recursion/README.md) | [Previous](/week3/functions/function_arguments/README.md)
