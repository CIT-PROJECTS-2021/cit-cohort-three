# Polymorphism in Python

## What is Polymorphism?

**Polymorphism** means "many forms." In Python, this allows different classes to have methods with the same name, and you can use these objects interchangeably.

## Basic Example

```python
class Bird:
    def make_sound(self):
        print("Chirp")

class Dog:
    def make_sound(self):
        print("Woof")

def animal_sound(animal):
    animal.make_sound()

bird = Bird()
dog = Dog()
animal_sound(bird)  # Output: Chirp
animal_sound(dog)   # Output: Woof
```

## Real World Use Cases

- **Payment Processing**: A function can process `CreditCard`, `PayPal`, or `BankTransfer` objects, as long as they implement a `pay()` method.
- **Drawing Software**: Different shapes (`Circle`, `Rectangle`, `Triangle`) have a `draw()` method, so a loop can call draw on all shapes without knowing their specific types.
- **File Handling**: Different file readers (`PDFReader`, `WordReader`) can have a `read()` method, making it easy to process files of various types with the same interface.

## Key Points

- Write code that works with objects of different types, as long as they have the required method.
- Makes code flexible and extensible.

---
