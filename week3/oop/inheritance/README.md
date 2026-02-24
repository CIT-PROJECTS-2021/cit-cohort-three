# Inheritance

Inheritance lets a class reuse and extend another class.

## Example
```python
class Vehicle:
    def move(self):
        print("Moving")

class Car(Vehicle):
    def honk(self):
        print("Beep")

car = Car()
car.move()
car.honk()
```

## `super()`
```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
```

[Next](/week3/oop/polymorphism/README.md) | [Previous](/week3/oop/classes/README.md)
