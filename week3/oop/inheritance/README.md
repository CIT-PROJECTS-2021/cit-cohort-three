# Inheritance in Python

## What is Inheritance?

**Inheritance** is when a class (child/subclass) takes on properties and behaviors (attributes and methods) from another class (parent/superclass). This helps you reuse code and organize programs efficiently.

## Basic Example

```python
class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):  # Car inherits from Vehicle
    def honk(self):
        print("Car honks: Beep beep!")

my_car = Car()
my_car.move()  # Output: Vehicle is moving  (inherited)
my_car.honk()  # Output: Car honks: Beep beep!
```

## Real World Use Cases

- **Banking Applications**: A `BankAccount` base class can be inherited by `SavingsAccount` and `CheckingAccount` subclasses, each with specific features.
- **E-commerce Systems**: A general `Product` class can be the parent for `Electronics`, `Clothing`, and `Books`, each with additional properties.
- **Game Development**: A generic `Character` class can be inherited by `Hero` and `Enemy`, sharing some behaviors but also having unique ones.

## Key Points

- Reduces code duplication.
- Easier to extend and maintain code.
- "is-a" relationship: a Car "is a" Vehicle.

---
