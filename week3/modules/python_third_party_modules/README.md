---
description: >-
  Learn how to install and use third-party packages from PyPI.
---

# Third-Party Modules

Third-party modules are not included in the standard library. You install them
with `pip`, then import them like any other module.

## Install
```bash
pip install requests
```

## Use
```python
import requests

response = requests.get("https://example.com")
print(response.status_code)
```

## Best Practice
Use a virtual environment to isolate project dependencies.

[Next](/week3/modules/python_packages/README.md) | [Previous](/week3/modules/python_built-in_modules/README.md)
