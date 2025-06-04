# Introduction to Classes in Python

## What is a Class?

A **class** in Python is a blueprint for creating objects. Objects represent real-world entities with properties (attributes) and actions (methods). Using classes, you can organize and reuse code efficiently.

---

## Why Use Classes?

- To group related data and functions together.
- To create multiple objects with similar structure but different data.
- To model real-world things (like students, cars, animals) in code.

---

## Defining a Simple Class

Here is how you define a basic class in Python:

```python
class Person:
    pass
```

The `pass` statement means "do nothing". This class doesn't do anything yet.

---

## Adding Attributes

Attributes are variables that belong to the object. You define them using a special method called `__init__`.

```python
class Person:
    def __init__(self, name, age):
        self.name = name  # attribute
        self.age = age    # attribute
```

- `__init__`: This is called the constructor. It runs when you create a new object.
- `self`: Refers to the current object being created.

---

## Creating Objects (Instances) from a Class

You can create objects by calling the class like a function:

```python
person1 = Person("Alice", 22)
person2 = Person("Bob", 30)

print(person1.name)  # Output: Alice
print(person2.age)   # Output: 30
```

---

## Adding Methods

Methods are functions defined inside a class. They describe what objects can do.

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, my name is", self.name)

person1 = Person("Alice")
person1.greet()  # Output: Hello, my name is Alice
```

---

## Example: A Simple Student Class

```python
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def show_info(self):
        print(f"Name: {self.name}, ID: {self.student_id}")

student1 = Student("John", 12345)
student1.show_info()  # Output: Name: John, ID: 12345
```

---

## Summary

- **Class**: A blueprint for objects.
- **Object**: An instance of a class.
- **Attributes**: Variables that belong to an object.
- **Methods**: Functions that belong to an object.
- Use `__init__` to set up initial values.

---

## Practice

Try writing your own class, for example, a `Car` class with attributes like `make` and `year`, and a method to display information.

```
