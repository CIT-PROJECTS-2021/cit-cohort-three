# Membership Operators

Membership operators test whether a value is in a sequence or collection.

| Operator | Meaning | Example |
| --- | --- | --- |
| `in` | value is present | `"a" in "cat"` |
| `not in` | value is absent | `4 not in [1, 2, 3]` |

## Example
```python
text = "Hello world"
data = {1: "a", 2: "b"}

print("H" in text)        # True
print("hello" in text)    # False (case-sensitive)
print(1 in data)          # True (checks keys)
print("a" in data)        # False
```

## Note
For dictionaries, `in` checks keys, not values.

[Next](/week2/operators/bitwise/README.md) | [Previous](/week2/operators/identity/README.md)
