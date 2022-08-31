---
description: >-
    In this lecture, you’ll learn about Object-Oriented Programming (OOP) in Python and its fundamental concept with the help of examples.
---

### Object Oriented Programming (OOP)
Python is a multi-paradigm programming language. It supports different programming approaches.

One of the popular approaches to solve a programming problem is by creating objects. This is known as Object-Oriented Programming (OOP).

An object has two characteristics:

- attributes
- behavior

**Let's take an example:**

A parrot is an object, as it has the following properties:

- name, age, color as attributes
- singing, dancing as behavior

The concept of OOP in Python focuses on creating reusable code. This concept is also known as DRY (Don't Repeat Yourself).

Put another way, object-oriented programming is an approach for modeling concrete, real-world things, like cars, as well as relations between things, like companies and employees, students and teachers, and so on. OOP models real-world entities as software objects that have some data associated with them and can perform certain functions.

In Python, the concept of OOP follows some basic principles:

### Class
A class is a blueprint for the object.

We can think of class as a sketch of a parrot with labels. It contains all the details about the name, colors, size etc. Based on these descriptions, we can study about the parrot. Here, a parrot is an object.

The example for class of parrot can be :

```python
class Parrot:
    pass
```

Here, we use the class keyword to define an empty `class Parrot`. From class, we construct instances. An instance is a specific object created from a particular class.

### Object
An object (instance) is an instantiation of a class. When class is defined, only the description for the object is defined. Therefore, no memory or storage is allocated.

The example for object of parrot class can be:

```python
parrot = Parrot()
```

Here, `parrot` is an object of class `Parrot`.

Suppose we have details of parrots. Now, we are going to show how to build the class and objects of parrots.

**Creating Class and Object in Python**

```python
class Parrot:
    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the object
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))

# access the instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))
```
Output:

```python
Blu is a bird
Woo is also a bird
Blu is 10 years old
Woo is 15 years old
```

In the above program, we created a `class` with the name `Parrot`. Then, we define attributes. The attributes are a characteristic of an object.

These attributes are defined inside the `__init__` method of the class. It is the initializer method that is first run as soon as the object is created.

Then, we create instances of the `Parrot` class. Here, blu and woo are references (value) to our new objects.

We can access the class attribute using `__class__.species`. Class attributes are the same for all instances of a class. Similarly, we access the instance attributes using `blu.name` and `blu.age`. However, instance attributes are different for every instance of a class.

### Methods
Methods are functions defined inside the class. They are used to perform operations on the objects.

**Creating Methods in Python**

```python
class Parrot:
    # class attribute
    species = "bird"
    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    # instance method
    def dance(self):
        return "{} is now dancing".format(self.name)

# instantiate the object
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the instance methods
print(blu.sing("Happy"))
print(woo.dance())
```
Output:

```python
Blu sings Happy
Woo is now dancing
```

In the above program, we define two methods i.e `sing()` and `dance()`. These are called instance methods because they are called on an instance object i.e blu.

### Inheritance
Inheritance is the process by which one class acquires the properties of another class.
nheritance is a way of creating a new class for using details of an existing class without modifying it. The newly formed class is a derived class (or child class). Similarly, the existing class is a base class (or parent class).

**Use of Inheritance in Python**

```python
class Bird:
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")


class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")


peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()
```
Output:

```python
Bird is ready
Penguin is ready
Penguin
Swim faster
Run faster
```

In the above program, we created two classes i.e. `Bird `(parent class) and Penguin (child class). The child class inherits the functions of parent class. We can see this from the `swim()` method.

Again, the child class modified the behavior of the parent class. We can see this from the `whoisThis()` method. Furthermore, we extend the functions of the parent class, by creating a new `run()` method.

Additionally, we use the `super()` function inside the `__init__()` method. This allows us to run the `__init__()` method of the parent class inside the child class.

### Encapsulation
Encapsulation is the process of wrapping up the data (variables) and code (methods) that together form an object. Using OOP in Python, we can restrict access to methods and variables. This prevents data from direct modification which is called encapsulation. In Python, we denote private attributes using underscore as the prefix i.e single `_` or double `__`.

**Encapsulation in Python**

```python
class Computer:
    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

    def getMaxPrice(self):
        return self.__maxprice


c = Computer()
c.__maxprice = 1000
c.sell()
c.setMaxPrice(1000)
c.sell()
```

Output:

```python
Selling Price: 900
Selling Price: 1000
```

In the above program, we defined a `Computer` class.

We used `__init__()` method to store the maximum selling price of Computer. Here, notice the code

```python
self.__maxprice = 1000
```

Here, we have tried to modify the value of `__maxprice` outside of the class. However, since `__maxprice` is a private variable, this modification is not seen on the output.

As shown, to change the value, we have to use a setter function i.e `setMaxPrice()` which takes price as a parameter.

### Polymorphism
Polymorphism is the ability of an object to take on many forms. The most common use of polymorphism in OOP occurs when a parent class reference is used to refer to a child class object.

Suppose, we need to color a shape, there are multiple shape options (rectangle, square, circle). However we could use the same method to color any shape. This concept is called Polymorphism.

**Using Polymorphism in Python**

```python
class Shape:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def calculate_area(self):
        return 0


class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def calculate_area(self):
        return self.side * self.side


class Rectangle(Shape):
    def __init__(self, name, length, breadth):
        super().__init__(name)
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        return self.length * self.breadth


# common method to print the area of the shape
def print_area(shape):
    print("{}'s area is {}".format(shape.get_name(), shape.calculate_area()))

# instantiate the objects
s = Square("Square", 10)
r = Rectangle("Rectangle", 20, 10)

# call the common method
print_area(s)
print_area(r)
```
Output:

```python
Square's area is 100
Rectangle's area is 200
```

In the above program, we defined two classes i.e. `Square` and `Rectangle`. Each of them have a common method `calculate_area()` which returns the area of the shape. However, we can use the same method to calculate the area of any shape because we are using the `Polymorphism` concept. In other words, for each class, the implementation of the `calculate_area()` method is different.

### Abstraction
Abstraction is the process of hiding the implementation details and showing only the essential features of the object.

### Key Points to Remember:

- Object-Oriented Programming makes the program easy to understand as well as efficient.
- Since the class is sharable, the code can be reused.
- Data is safe and secure with data abstraction.
- Polymorphism allows the same interface for different objects, so programmers can write efficient code.
