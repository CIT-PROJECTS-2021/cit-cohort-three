# Strings

Strings are sequences of characters. In Python, strings are Unicode by default,
so they can represent text from many languages.

### Creating Strings
```python
single = 'Hello'
double = "Hello"
multi = """Hello,
world"""
```

### Indexing and Slicing
```python
text = "Python"

print(text[0])    # P
print(text[-1])   # n
print(text[1:4])  # yth
```

Slicing is `start` inclusive and `end` exclusive.

### Immutability
Strings are immutable, so you cannot change a character in place.

```python
text = "Hello"
# text[0] = "J"  # TypeError
```

### Common Operations
```python
greeting = "Hello" + " " + "World"
echo = "Hi" * 3
```

### Membership and Iteration
```python
if "World" in greeting:
    print("Found")

for ch in "Hi":
    print(ch)
```

### Formatting
Use f-strings for most cases:

```python
name = "Ada"
age = 28
print(f"{name} is {age} years old.")
```

`str.format()` is also common:
```python
print("{} {}".format("Hello", "World"))
```

### Useful Methods
```python
text = "  Hello World  "

print(text.lower())
print(text.upper())
print(text.strip())
print(text.replace("World", "Python"))
print(text.split())
```

[Next](/week2/data_types/python_lists/README.md) | [Previous](/week2/operators/bitwise/README.md)
