Regex or Regular Expressions are an important part of Python Programming or any other Programming Language. It is used for searching and even replacing the specified text pattern. In the regular expression, a set of characters together form the search pattern. It is also known as reg-ex pattern. 

Tough thing about Regex is not learning or understanding it but remembering syntax and how to form pattern according to our requirements. So here we have provided a regex cheat sheet containing all the different character classes, special characters, modifiers, sets etc. which are used in regular expression.

## Character Classes

|Character Class|Description|
|:-|:-|
|.|Any Character Except New Line|
|\d|Digit (0-9)|
|\D|Not a Digit (0-9)|
|\w|Word Character (a-z, A-Z, 0-9, _)|
|\W|Not a Word Character|
|\s|Whitespace (space, tab, newline)|
|\S|Not Whitespace (space, tab, newline)|
|\b|Word Boundary|
|\B|Not a Word Boundary|
|^|Beginning of a String|
|$|End of a String|


### Basic Characters:

|Expression 	| Explanations |
|:-|:-|
|`^` | Matches the expression to its right, at the start of a string before it experiences a line break
|`$` | Matches the expression to its left, at the end of a string before it experiences a line break
|`.` | Matches any character except newline
|`a` | Matches the character a
|`xy` | Matches the string xy
|`a|b` | Matches expression a or b. If a is matched first, b is left untried.
|`[abc]` | Matches a single character from the set a, b, or c

Example:

```python
import re

print(re.search(r"^x","regex"))
print(re.search(r"s$","pythonista"))
```

Output:

```python
None
<re.Match object; span=(8, 9), match='s'>
```

### Quantifiers:

|Expression 	| Explanations |
|:-|:-|
|`*` | Matches the preceding expression 0 or more times
|`+` | Matches the preceding expression 1 or more times
|`?` | Matches the preceding expression 0 or 1 time
|`{n}` | Matches the preceding expression exactly n times
|`{n,}` | Matches the preceding expression at least n times
|`{,n}` | Matches the preceding expression at most n times
|`{m,n}` | Matches the preceding expression at least m and at most n times

Their default searching method is Greedy. But if ? is added to qualifiers (+, *, and ? itself) it will perform matches in a non-greedy manner.

Examples:

```python
import re

print(re.search(r"Py.*n","Pygmalion"))
print(re.search(r"Py.*?n","Pygmalion"))
```

Output:

```python
<re.Match object; span=(0, 9), match='Pygmalion'>
<re.Match object; span=(0, 3), match='Pyg'>
```

### Sets:

|Expression 	| Explanations |
|:-|:-|
|`[abc]` | Matches a single character from the set a, b, or c
|`[^abc]` | Matches a single character that is not a, b, or c
|`[a-z]` | Matches a single character from the range a-z
|`[a-zA-Z0-9]` | Matches a single character from the range a-z, A-Z, or 0-9

Examples:

```python
import re

print(re.search(r"[aeiou]","regex"))
print(re.search(r"[^aeiou]","regex"))
```

Output:

```python
<re.Match object; span=(1, 2), match='e'>
<re.Match object; span=(0, 1), match='r'>
```