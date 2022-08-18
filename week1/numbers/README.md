---
description: >-
  Numbers are the foundation of every programming language. In this module, we will learn how to use numbers in Python.
---
# Numbers / Integers
There are three numeric types in Python:
- int (e.g. 2, 4, 20)
    - bool (e.g. False and True, acting like 0 and 1)
- float (e.g. 5.0, 1.6)
- complex (e.g. 5+6j, 4-3j)

### Integers (int)
- int is a whole number, without decimals, of unlimited length.
 e.g. 2, -2, 0, -0, 2147483647, -2147483648
 ```python
 positive_int = 2
 negative_int = -2
 zero = 0
 ```

### Boolean (bool)
Booleans represent the truth values False and True. 
The two objects representing the values False and True are the only Boolean objects. 

The Boolean type is a subtype of the integer type, and Boolean values behave like the values 0 and 1, respectively, in almost all contexts, the exception being that when converted to a string, the strings `"False"` or `"True"` are returned, respectively.
example:
```python
is_raining = True
is_cloudy = False
```

### Float (float)
Float, or "floating point number" is a number, positive or negative containing one or more decimals.
Example:
```python
  float_number = 7.0
  # Another way of declaring float is using float() function.
  float_number_via_function = float(7)
  float_negative = -35.59
```




### References
[Python Documentation](https://docs.python.org/3/tutorial/introduction.html)

[W3Schools](https://www.w3schools.com/python/python_numbers.asp)