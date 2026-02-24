# Lists

Lists are ordered, mutable collections. They can hold mixed types and be
resized as needed.

## Creating Lists
```python
numbers = [1, 2, 3]
mixed = ["Apple", 12, 45.7, False]
nested = ["Apple", ["Banana", "Cherry"], "Durian"]
```

## Accessing Items
```python
fruits = ["Apple", "Banana", "Cherry"]

print(fruits[0])   # Apple
print(fruits[-1])  # Cherry
```

## Slicing
```python
letters = ["P", "y", "t", "h", "o", "n"]
print(letters[2:5])  # ['t', 'h', 'o']
print(letters[:3])   # ['P', 'y', 't']
print(letters[3:])   # ['h', 'o', 'n']
```

## Updating Items
```python
odd = [2, 4, 6, 8]
odd[0] = 1
odd[1:4] = [3, 5, 7]
print(odd)  # [1, 3, 5, 7]
```

## Adding Items
```python
fruits = ["Apple", "Banana"]
fruits.append("Cherry")
fruits.extend(["Durian", "Mango"])
fruits.insert(1, "Grape")
```

## Removing Items
```python
fruits = ["Apple", "Banana", "Cherry", "Durian"]
fruits.remove("Banana")
last = fruits.pop()
del fruits[0]
fruits.clear()
```

## Common Methods
| Method | Purpose |
| --- | --- |
| `append()` | add one item to end |
| `extend()` | add many items |
| `insert()` | insert at index |
| `remove()` | remove by value |
| `pop()` | remove by index (default last) |
| `clear()` | remove all items |
| `index()` | find first index |
| `count()` | count occurrences |
| `sort()` | sort list in place |
| `reverse()` | reverse in place |
| `copy()` | shallow copy |

## List Comprehensions
```python
powers = [2 ** x for x in range(5)]
odds = [x for x in range(10) if x % 2 == 1]
```

## Iteration
```python
for fruit in ["Apple", "Banana"]:
    print(fruit)
```

[Next](/week2/data_types/python_tuples/README.md) | [Previous](/week2/data_types/strings/README.md)
