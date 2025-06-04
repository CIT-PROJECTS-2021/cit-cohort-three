# Abstraction in Python

## What is Abstraction?

**Abstraction** means hiding complex implementation details and showing only the necessary features of an object.

In Python, abstraction is often achieved using abstract base classes (from the `abc` module). These classes define methods that must be created in any subclass.

## Basic Example

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started!")

bike = Motorcycle()
bike.start_engine()  # Output: Motorcycle engine started!
```

## Real World Use Cases

- **Payment Gateways**: An abstract `Payment` class with a `pay()` method. Each payment type (credit card, PayPal) implements their own `pay()` logic.
- **Messaging Apps**: An abstract `MessageSender` class with a `send()` method. Subclasses like `EmailSender` and `SMSSender` implement sending for different channels.
- **Hardware Control**: Abstract classes for `Printer`, `Scanner` ensure all devices have certain required methods, regardless of how they work internally.

## Key Points

- Helps you design systems where you only care about what an object does, not how it does it.
- Abstract classes can't be instantiated directly; they define a contract for subclasses.

---
