---
description: >-
  Learn how to organize code using modules and understand different ways to import them.
---

# Modules

A module is a Python file that contains code you can reuse (functions, classes,
variables). Modules help you split large programs into manageable pieces.

## Creating a Module
`example.py`
```python
def add(a, b):
    return a + b
```

## Importing a Module
```python
import example

print(example.add(2, 3))  # 5
```

## Import Variations
```python
import math as m
from math import pi, e
```

Avoid `from module import *` because it pollutes the namespace.

## Module Search Path
Python looks in:
- the current directory
- `PYTHONPATH`
- the standard library and site-packages

You can inspect this with:
```python
import sys
print(sys.path)
```

[Next](/week3/modules/python_built-in_modules/README.md) | [Previous](/week3/README.md)
