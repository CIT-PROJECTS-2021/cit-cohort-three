# Polymorphism

Polymorphism lets different classes provide the same interface.

## Example
```python
class Bird:
    def make_sound(self):
        print("Chirp")

class Dog:
    def make_sound(self):
        print("Woof")

def animal_sound(animal):
    animal.make_sound()

animal_sound(Bird())
animal_sound(Dog())
```

## Key Idea
If objects share a method name, you can treat them the same way.

[Next](/week3/oop/encapsulation/README.md) | [Previous](/week3/oop/inheritance/README.md)
