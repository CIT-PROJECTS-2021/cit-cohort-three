Python language offers some special types of operators like the identity operator or the membership operator. They are described below with examples.


`in` and `not in` are the membership operators in Python. They are used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary).

In a dictionary we can only test for presence of key, not the value.

|Operator	| Meaning	| Example |
|-----------|-----------|---------|
|in | 	True if value/variable is found in the sequence	| 5 in x |
|not in	 | True if value/variable is not found in the sequence	| 5 not in x |

### Example

```python
x = 'Hello world'
y = {1:'a',2:'b'}

# Output: True
print('H' in x)

# Output: True
print('hello' not in x)

# Output: True
print(1 in y)

# Output: False
print('a' in y)
```

**Output:**

```python
True
False
True
False
```

Here, `'H'` is in `x` but `'hello'` is not present in `x` (remember, Python is case sensitive). Similarly, `1` is key and `'a'` is the value in dictionary `y`. Hence, `'a'` in `y` returns `False`.