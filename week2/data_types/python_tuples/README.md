# Tuples

Tuples are ordered and immutable collections. They are similar to lists, but
you cannot change their contents after creation.

## Creating Tuples
```python
empty = ()
numbers = (1, 2, 3)
mixed = (1, "a", 2.5)

packed = "cat", "dog", "rabbit"
cat, dog, rabbit = packed
```

Single-item tuples need a trailing comma:
```python
single = (1,)
```

## Accessing Items
```python
t = (10, 20, 30, 40)

print(t[0])   # 10
print(t[-1])  # 40
print(t[1:3]) # (20, 30)
```

## Immutability
```python
t = (1, 2, 3)
# t[0] = 9  # TypeError
```

If a tuple contains a mutable object (like a list), that inner object can be
changed:

```python
t = (1, [2, 3])
t[1][0] = 99
print(t)  # (1, [99, 3])
```

## Common Methods
```python
t = ("a", "p", "p", "l", "e")
print(t.count("p"))  # 2
print(t.index("l"))  # 3
```

## Membership and Iteration
```python
t = (1, 2, 3)
print(2 in t)  # True

for item in t:
    print(item)
```

## When to Use Tuples
- Fixed collections that should not change.
- Keys in dictionaries (tuples are hashable if they contain only immutable items).

[Next](/week2/data_types/sets/README.md) | [Previous](/week2/data_types/python_lists/README.md)
