# Encapsulation

Encapsulation groups data and behavior together and hides internal details.
In Python, a leading underscore is a convention for “internal” attributes.

## Example
```python
class User:
    def __init__(self, username, password):
        self.username = username
        self._password = password  # internal use

    def check_password(self, candidate):
        return candidate == self._password
```

## Notes
- `_name` is a convention (not enforced).
- `__name` triggers name‑mangling for stronger privacy.

[Next](/week3/oop/abstraction/README.md) | [Previous](/week3/oop/polymorphism/README.md)
