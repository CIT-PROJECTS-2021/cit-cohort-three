# Encapsulation in Python

## What is Encapsulation?

**Encapsulation** is about restricting access to parts of your code (data or methods), exposing only what is necessary. This keeps your code safe and easier to manage.

In Python, we use underscores (`_` or `__`) to indicate that attributes or methods are private (should not be accessed directly).

## Basic Example

```python
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  # private attribute

    def check_password(self, password):
        return self.__password == password

user = User("alice", "secret123")
print(user.username)          # Output: alice
print(user.check_password("wrong"))  # Output: False
# print(user.__password)     # Error: attribute is private
```

## Real World Use Cases

- **Banking Apps**: User account balance is kept private; access is only via methods like `deposit()` or `withdraw()`.
- **Medical Systems**: Patient details are hidden and only accessible through secure methods.
- **APIs**: You hide internal logic and only expose certain functions to users.

## Key Points

- Use underscores to indicate private variables or methods.
- Protects data and reduces bugs by preventing unauthorized access.

---
