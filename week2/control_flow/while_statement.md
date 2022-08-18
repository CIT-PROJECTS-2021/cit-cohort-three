# The While Statement

The while statement in Python supports repeated execution of a statement or block of statements that is controlled by a conditional expression. Here’s the syntax for the while statement:
```python
while expression:
    statement(s)
```

A while statement can also include an else clause and break and continue statements, as we’ll discuss shortly.

Here’s a typical while statement:
```python
count = 0
while x > 0:
    x = x // 2            # truncating division
    count += 1
print("The approximate log2 is", count)
```

First, expression, which is known as the loop condition, is evaluated. If the condition is false, the while statement ends. If the loop condition is satisfied, the statement or statements that comprise the loop body are executed. When the loop body finishes executing, the loop condition is evaluated again, to see if another iteration should be performed. This process continues until the loop condition is false, at which point the while statement ends.

The loop body should contain code that eventually makes the loop condition false, or the loop will never end unless an exception is raised or the loop body executes a break statement. A loop that is in a function’s body also ends if a return statement executes in the loop body, as the whole function ends in this case.