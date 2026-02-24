---
description: >-
  Learn how Python packages organize modules into folders.
---

# Packages

A package is a folder that contains Python modules. Packages help you organize
larger projects.

## Example Structure
```
game/
  __init__.py
  level/
    __init__.py
    start.py
```

## Importing from a Package
```python
import game.level.start

game.level.start.select_difficulty("easy")
```

You can also import the module directly:
```python
from game.level import start
start.select_difficulty("easy")
```

## Notes
- `__init__.py` marks a folder as a package.
- Python searches for packages using `sys.path`.

[Previous](/week3/modules/python_third_party_modules/README.md)
