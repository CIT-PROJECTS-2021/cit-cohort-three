# Classes

A class is a blueprint for creating objects with attributes and methods.

## Example
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I'm {self.name}")

person = Person("Ada", 28)
person.greet()
```

## Key Ideas
- `__init__` initializes a new object.
- `self` refers to the current instance.

[Next](/week3/oop/inheritance/README.md) | [Previous](/week3/oop/README.md)
