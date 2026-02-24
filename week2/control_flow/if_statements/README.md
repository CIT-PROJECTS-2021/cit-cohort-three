# `if` Statements

Use `if` statements to run code only when a condition is true. The `elif` and
`else` clauses are optional.

## Syntax
```python
if condition:
    # run if condition is true
elif another_condition:
    # run if previous conditions were false
else:
    # run if all conditions were false
```

## Example
```python
x = 10

if x < 0:
    print("Negative")
elif x % 2 != 0:
    print("Positive and odd")
else:
    print("Even or zero")
```

## Truthiness
In a boolean context, these values are considered false:
- `0`, `0.0`
- `None`
- empty strings, lists, tuples, dicts, and sets

Everything else is considered true. The most Pythonic way to test a value is:

```python
if x:
    print("x is truthy")
```

Avoid:
```python
if x is True:
    ...
```

## Common Pitfalls
- Forgetting the colon `:` after the condition.
- Missing indentation inside the block.
- Comparing directly to `True` or `False` unnecessarily.

## Practice
1. Write a program that prints `"adult"` if `age >= 18`, otherwise `"minor"`.
2. Extend it to print `"senior"` if `age >= 65`.

[Next](/week2/control_flow/for_loop/README.md) | [Previous](/week2/control_flow/README.md)
