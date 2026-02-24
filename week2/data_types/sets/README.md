# Sets

Sets are unordered collections of unique, immutable items. The set itself is
mutable, so you can add or remove elements.

## Creating Sets
```python
numbers = {1, 2, 3}
mixed = {1.0, "Hello", (1, 2, 3)}

from_list = set([1, 2, 2, 3])  # {1, 2, 3}
```

An empty set must be created with `set()`:
```python
empty = set()
```

## Adding and Removing
```python
s = {1, 3}
s.add(2)
s.update([2, 4, 5])

s.remove(4)   # raises KeyError if missing
s.discard(10) # no error if missing
```

## Set Operations
```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)  # union
print(a & b)  # intersection
print(a - b)  # difference
print(a ^ b)  # symmetric difference
```

## Membership and Iteration
```python
print(2 in a)  # True

for item in a:
    print(item)
```

## Frozenset (Immutable Set)
```python
f = frozenset([1, 2, 3])
# f.add(4)  # AttributeError
```

[Next](/week2/data_types/dictionaries/README.md) | [Previous](/week2/data_types/python_tuples/README.md)
