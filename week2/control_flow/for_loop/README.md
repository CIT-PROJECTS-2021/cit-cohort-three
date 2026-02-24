# `for` Loops

Use `for` loops to iterate over sequences (lists, tuples, strings) and other
iterables.

## Syntax
```python
for item in sequence:
    print(item)
```

## Basic Example
```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

## Using `range()`
`range()` generates numbers on demand, which is memory-efficient.

```python
for i in range(5):
    print(i)
```

`range(start, stop, step)` is also supported:

```python
print(list(range(2, 10, 2)))  # [2, 4, 6, 8]
```

## Index + Value with `enumerate()`
```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

## `for` ... `else`
The `else` block runs only if the loop completes without a `break`.

```python
targets = ["Ada", "Grace", "Linus"]
name = "Guido"

for target in targets:
    if target == name:
        print("Found")
        break
else:
    print("Not found")
```

## Common Pitfalls
- Modifying a list while iterating over it.
- Using `range(len(...))` when `enumerate()` is clearer.

[Next](/week2/control_flow/while_loops/README.md) | [Previous](/week2/control_flow/if_statements/README.md)
