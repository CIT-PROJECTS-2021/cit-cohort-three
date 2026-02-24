---
description: >-
  Intro to object-oriented programming concepts in Python.
---

# Object-Oriented Programming (OOP)

OOP models real‑world things as objects with data (attributes) and behavior
(methods).

## Core Ideas
- **Class**: blueprint for objects
- **Object**: instance of a class
- **Encapsulation**: keep data and behavior together
- **Inheritance**: reuse behavior from a base class
- **Polymorphism**: same interface, different implementations
- **Abstraction**: hide complex details behind a simple interface

## Quick Example
```python
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says woof"

pet = Dog("Rex")
print(pet.speak())
```

## Topics
- [Classes](/week3/oop/classes/README.md)
- [Inheritance](/week3/oop/inheritance/README.md)
- [Polymorphism](/week3/oop/polymorphism/README.md)
- [Encapsulation](/week3/oop/encapsulation/README.md)
- [Abstraction](/week3/oop/abstraction/README.md)

[Previous](/week3/python_exceptions/README.md)
