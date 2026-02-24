---
description: >-
  Learn positional, keyword, default, and variable-length function arguments.
---

# Function Arguments

## Positional Arguments
```python
def add(x, y):
    return x + y

print(add(1, 2))  # 3
```

## Default Arguments
```python
def add(x, y=5):
    return x + y

print(add(1))    # 6
print(add(1, 2)) # 3
```

## Keyword Arguments
```python
def login(username, password):
    print(username, password)

login(username="admin", password="1234")
login(password="1234", username="admin")
```

Keyword arguments must come after positional ones.

## Variable-Length Arguments
```python
def total(*args):
    return sum(args)

print(total(1, 2, 3))  # 6
```

## Keyword Variable-Length Arguments
```python
def profile(**kwargs):
    return kwargs

print(profile(name="Ada", age=28))
```

[Next](/week3/functions/lambda_function/README.md) | [Previous](/week3/functions/README.md)
