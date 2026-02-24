# Integers in Depth

Integers (`int`) are whole numbers with no decimal part. Python integers have
unlimited precision, which means they can grow very large.

## Examples
```python
small = 42
big = 10**30
negative = -100
```

## Converting to int
```python
age = int("21")   # 21
rounded = int(3.9)  # 3 (truncates toward zero)
```

## Integer Division and Modulo
```python
quotient = 10 // 3  # 3
remainder = 10 % 3  # 1
```

## Booleans Are Integers
```python
print(True + True)   # 2
print(False + 10)    # 10
```

## Practice
1. Compute how many full weeks are in 365 days.
2. Compute the remainder days after full weeks.

```python
days = 365
weeks = days // 7
leftover_days = days % 7
print(weeks, leftover_days)
```

[Previous](/week1/numbers/README.md)
