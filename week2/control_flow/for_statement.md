# The for Statement

The for statement in Python supports repeated execution of a statement or block of statements that is controlled by an iterable expression. Here’s the syntax for the for statement:
```python
for <variable> in <iterable>:
    <statements>
```
The for statement is used to iterate over an iterable object, such as a list or a string. The for statement can be used to iterate over a sequence of numbers, or over a sequence of characters in a string.

Note that the in keyword is part of the syntax of the for statement and is functionally unrelated to the in operator used for membership testing. A for statement can also include an else clause and break and continue statements, as we’ll discuss shortly.

Here’s a typical for statement:
```python
for letter in "ciao":
    print(letter)
```