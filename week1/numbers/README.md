---
description: >-
  Numbers are the foundation of every programming language. In this module, we will learn how to use numbers in Python.
---
# Numbers

Python has three main numeric types:
- `int` for whole numbers (e.g. `2`, `-5`)
- `float` for decimal numbers (e.g. `3.14`, `-0.5`)
- `complex` for complex numbers (e.g. `2+3j`)

`bool` is a subtype of `int` where `False` behaves like `0` and `True` behaves
like `1`.

## Integers (`int`)
Integers are whole numbers of unlimited length.

```python
positive_int = 2
negative_int = -2
zero = 0
```

## Booleans (`bool`)
Booleans represent truth values: `True` and `False`.

```python
is_raining = True
is_cloudy = False
```

## Floats (`float`)
Floats are numbers with decimals.

```python
float_number = 7.0
float_number_via_function = float(7)
float_negative = -35.59
```

## Complex Numbers (`complex`)
Complex numbers have a real and imaginary part.

```python
z = 2 + 3j
print(z.real)  # 2.0
print(z.imag)  # 3.0
```

## Common Operations
```python
a = 10
b = 3

print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.333...
```

## Useful Built-ins
```python
print(type(5))        # <class 'int'>
print(isinstance(5, int))  # True
print(round(3.14159, 2))   # 3.14
```

## Common Pitfalls
- `0.1 + 0.2` is not exactly `0.3` because of floating-point precision.
- Dividing two integers with `/` always returns a float.

### References
[Python Documentation](https://docs.python.org/3/tutorial/introduction.html)

[W3Schools](https://www.w3schools.com/python/python_numbers.asp)

[Next](/week1/numbers/numbers-integers.md) | [Previous](/week1/variables.md)
