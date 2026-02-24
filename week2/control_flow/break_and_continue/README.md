# `break` and `continue`

Use `break` to exit a loop early. Use `continue` to skip the rest of the current
iteration and move to the next.

## `break`
```python
for letter in "Python":
    if letter == "h":
        break
    print(letter)
```

Output:
```
P
y
t
```

## `continue`
```python
for letter in "Python":
    if letter == "h":
        continue
    print(letter)
```

Output:
```
P
y
t
o
n
```

## Common Pitfalls
- Using `break` when you meant `return` inside a function.
- Using `continue` and accidentally skipping necessary updates.

[Previous](/week2/control_flow/while_loops/README.md)
