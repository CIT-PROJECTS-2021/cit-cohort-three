---
description: >-
  Learn what functions are, how to define them, and how return values work.
---

# Functions

Functions group reusable logic into a named block.

## Defining a Function
```python
def greet(name: str) -> None:
    """Print a friendly greeting."""
    print(f"Hello, {name}!")
```

## Calling a Function
```python
greet("Paul")
```

## Return Values
```python
def absolute_value(n: int) -> int:
    if n >= 0:
        return n
    return -n

print(absolute_value(-4))  # 4
```

If you omit `return`, Python returns `None`.

## Scope (Local vs Global)
```python
x = 10

def show() -> None:
    x = 5
    print(x)  # 5

show()
print(x)      # 10
```

## Types of Functions
- Built-in functions (e.g., `print`, `len`)
- User-defined functions (your own)

[Next](/week3/functions/function_arguments/README.md) | [Previous](/week3/README.md)
