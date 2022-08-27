---
description: >-
    In Python, you can define a function that takes variable number of arguments. In this article, you will learn to define such functions using default, keyword and arbitrary arguments.
---

### Arguments

In the previous lecture, we learned about defining a function and calling it. Otherwise, the function call will result in an error. Here is an example.

```python
def add(x, y):
    """This function adds two numbers"""
    print(x + y)

add(1, 2)
```

In the above example, the function add is defined with two arguments. When we call the function, we need to pass two arguments.

```python
print(add(1, 2))

# 3
```

If we call it with a different number of arguments, the interpreter will show an error message. Below is a call to this function with one and no arguments along with their respective error messages.
    
```python
print(add(1))

# TypeError: add() missing 1 required positional argument: 'y'

print(add())

# TypeError: add() missing 2 required positional arguments: 'x' and 'y'
```

### Variable Function Arguments

Up until now, functions had a fixed number of arguments. In Python, there are other ways to define a function that can take variable number of arguments.

Three different forms of this type are described below.

**Python Default Arguments** 

Function arguments can have default values in Python.

We can provide a default value to an argument by using the assignment operator (=). Here is an example.

```python
def add(x, y=5):
    """This function adds two numbers"""
    print(x + y)

print(add(1))

# 6
```

In this function, the parameter y has a default value of 5. If we call the function without passing the value for y, the default value will be used wheras if we pass the value for y, the value for y will be used.

### Python Keyword Arguments

When we call a function with some values, these values get assigned to the arguments according to their position.

Python allows functions to be called using keyword arguments. When we call functions in this way, the order (position) of the arguments can be changed.

```python
def login(username, password):
    """This function logs in a user"""
    print(username, password)

login(username='admin', password='1234')
# admin 1234

login(password='1234', username='admin')
# admin 1234

```

As we can see, we can mix positional arguments with keyword arguments during a function call. But we must keep in mind that keyword arguments must follow positional arguments.

Having a positional argument after keyword arguments will result in errors. For example, the function call as follows:

```python
login(username='admin', '1234')
# TypeError: login() got an unexpected keyword argument '1234'
```

### Python Arbitrary Arguments

Sometimes, we do not know in advance the number of arguments that will be passed into a function. Python allows us to handle this kind of situation through function calls with an arbitrary number of arguments.

In the function definition, we use an asterisk `(*)` before the parameter name to denote this kind of argument. Here is an example.

```python
def add(*args):
    """This function adds unlimited number of arguments"""
    print(sum(args))

print(add(1, 2, 3, 4, 5))
# 15
```

Here, we have called the function with multiple arguments. These arguments get wrapped up into a tuple before being passed into the function.



