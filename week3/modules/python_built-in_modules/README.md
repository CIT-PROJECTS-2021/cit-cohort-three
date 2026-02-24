---
description: >-
  Overview of common built-in modules in Python's standard library.
---

# Built-in Modules

Python ships with a large standard library. You import these modules just like
your own files.

## Common Examples
```python
import math
import random
import os
```

### `math`
```python
import math
print(math.sqrt(81))  # 9.0
print(math.pi)        # 3.14159...
```

### `random`
```python
import random
print(random.randint(1, 6))
print(random.choice(["a", "b", "c"]))
```

### `os`
```python
import os
print(os.getcwd())
print(os.listdir("."))
```

### `datetime`
```python
from datetime import datetime
print(datetime.now())
```

## Tip
Use `help("modules")` in the Python REPL to list available modules.

[Next](/week3/modules/python_third_party_modules/README.md) | [Previous](/week3/modules/README.md)
