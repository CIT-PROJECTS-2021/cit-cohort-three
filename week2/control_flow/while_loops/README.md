# `while` Loops

Use a `while` loop to repeat a block of code as long as a condition is true.
This is useful when you do not know in advance how many iterations you need.

## Syntax
```python
while condition:
    # code block
```

## Example
```python
total = 0
counter = 1
n = 5

while counter <= n:
    total += counter
    counter += 1

print(total)  # 15
```

## `while` ... `else`
The `else` block runs only if the loop finishes without a `break`.

```python
counter = 0

while counter < 3:
    print("Loop")
    counter += 1
else:
    print("Done")
```

## Common Pitfalls
- Forgetting to update the loop variable (infinite loop).
- Using a `while` loop where a `for` loop is clearer.

[Next](/week2/control_flow/break_and_continue/README.md) | [Previous](/week2/control_flow/for_loop/README.md)
