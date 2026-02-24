---
description: >-
  Learn how recursion works and how to write a safe recursive function.
---

# Recursion

Recursion is when a function calls itself. Every recursive function needs a
**base case** to stop.

## Example: Factorial
```python
def factorial(n: int) -> int:
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(3))  # 6
```

## Base Case vs Recursive Case
```python
def countdown(n: int) -> None:
    if n == 0:        # base case
        print("Done")
        return
    print(n)
    countdown(n - 1)  # recursive case
```

## Common Pitfalls
- Missing base case (infinite recursion).
- Very deep recursion causing `RecursionError`.

[Previous](/week3/functions/lambda_function/README.md)
