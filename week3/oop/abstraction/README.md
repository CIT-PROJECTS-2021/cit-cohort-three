# Abstraction

Abstraction hides implementation details and exposes only the required
interface.

## Example with `abc`
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

class Motorcycle(Vehicle):
    def start_engine(self):
        print("Engine started")
```

## Key Idea
Abstract classes define a contract that subclasses must implement.

[Previous](/week3/oop/encapsulation/README.md)
