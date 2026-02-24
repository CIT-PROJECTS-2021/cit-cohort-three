# Variables

Python is dynamically typed, which means you do not declare variable types.
A variable is created the moment you assign a value to a name.

```python
name = "Grace"
age = 37
```

Every value in Python is an object, and variables are references to those
objects.

## Naming Rules
- Must start with a letter or underscore.
- Cannot start with a number.
- May contain letters, numbers, and underscores.
- Case-sensitive: `age`, `Age`, and `AGE` are different.

## Good Naming
```python
total_volume = 12
user_email = "grace@example.com"
```

## Multiple Assignment
```python
x, y, z = 1, 2, 3
first_name, last_name = "Ada", "Lovelace"
```

## Reassignment and Types
```python
count = 10
count = "ten"  # valid, but try to avoid confusing changes

print(type(count))  # <class 'str'>
```

## Quick Practice
1. Create a variable `city` and assign your city name.
2. Create a variable `temperature` and assign a number.
3. Print both in one sentence using an f-string.

```python
city = "Lagos"
temperature = 28
print(f"The temperature in {city} is {temperature}C.")
```

[Next](/week1/numbers/README.md) | [Previous](/week1/python_syntax.md)
