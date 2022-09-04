---
description: >-
  This module introduces the concept of third-party modules and how to install
  them.
---

# Python Third Party Modules

## What is a Third Party Module?
This refers to a module that is not part of the Python Standard Library. These modules are developed by third-party developers and are available for use in your Python programs. They are usually installed using the Python Package Manager, `pip`.

## Installing Third Party Modules
To install a third-party module, you need to know the name of the module and use the following syntax:

```python
pip install <module_name>
```

For example, to install the `requests` module, you would use the following command:

```python
pip install requests
```

> **Note:** You may need to use `pip3` instead of `pip` depending on your system configuration as well as need to use `sudo` before the `pip` command depending on your system configuration.

> **Note:** You need to create a virtual environment before installing third-party modules. You can learn more about virtual environments in the [Python Virtual Environments](../python_virtual_environments/README.md) module.

## Using Third Party Modules
Once you have installed a third-party module, you can use it in your Python programs. For example, to use the `requests` module, you would use the following syntax:

```python
import requests
```

## Additional Resources
- [Python Package Index](https://pypi.org/)
- [Python Requests Module](https://requests.readthedocs.io/en/master/)
- [Python Requests Module Tutorial](https://realpython.com/python-requests/)
- [Python Requests Module Quickstart](https://docs.python-requests.org/en/master/user/quickstart/)
- [Python Requests Module API Reference](https://docs.python-requests.org/en/master/api/)