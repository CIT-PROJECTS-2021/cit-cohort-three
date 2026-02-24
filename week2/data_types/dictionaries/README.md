# Dictionaries

Dictionaries store key/value pairs. Keys must be unique and immutable.

## Creating Dictionaries
```python
empty = {}
person = {"name": "Jack", "age": 26}
mixed = {1: "apple", "colors": ["red", "green"]}

from_pairs = dict([(1, "a"), (2, "b")])
```

## Accessing Values
```python
print(person["name"])      # Jack
print(person.get("age"))   # 26
print(person.get("city"))  # None
```

## Adding and Updating
```python
person["age"] = 27
person["city"] = "Downtown"
```

## Removing
```python
scores = {1: 1, 2: 4, 3: 9}
scores.pop(2)     # removes key 2
scores.popitem()  # removes last inserted item (Python 3.7+)
del scores[1]
scores.clear()
```

## Common Methods
```python
person = {"name": "Jack", "age": 26}

print(person.keys())
print(person.values())
print(person.items())
```

## Dictionary Comprehension
```python
squares = {x: x * x for x in range(6)}
odd_squares = {x: x * x for x in range(11) if x % 2 == 1}
```

## Membership and Iteration
```python
print("name" in person)  # True

for key, value in person.items():
    print(key, value)
```

[Previous](/week2/data_types/sets/README.md)
