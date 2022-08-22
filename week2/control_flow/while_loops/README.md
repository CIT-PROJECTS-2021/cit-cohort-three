Loops are used in programming to repeat a specific block of code. In this lecture, you will learn to create a while loop in Python.

**What is while loop in Python?**

The `while loop` in Python is used to iterate over a block of code as long as the test expression `(condition)` is `true`.

We generally use this loop when we don't know the number of times to iterate beforehand.

Syntax of while Loop in Python:

```python
while condition:
    # code block to be executed
    # condition is evaluated again at the end of the loop
```

In the while loop, `condition` is checked first. The body of the loop is entered only if the `condition` evaluates to True. After one iteration, the test expression is checked again. This process continues until the `condition` evaluates to False.

In Python, the body of the while loop is determined through indentation.

The body starts with indentation and the first unindented line marks the end.

Python interprets any non-zero value as True. None and 0 are interpreted as False.

**Flow chart for while loop**

<img src="https://cdn.programiz.com/sites/tutorial2program/files/whileLoopFlowchart.jpg" alt="while loop flowchart" style="width: 50%;">


**Example: Python while Loop**

```python
# Program to add natural
# numbers up to nth term

# sequence: sum = 1 + 2 + 3 + ... + n

# initialize sum and counter
sum = 0
counter = 1

n = int(input("Enter the value of n: "))

# calculate sum of first n natural numbers
while counter <= n:
    sum = sum + counter
    counter = counter + 1

# display the sum
print("The sum is", sum)
```

When you run the program, the output will be:

```
Enter the value of n: 5
The sum is 15
```

In the above program, the test expression will be `True` as long as our counter variable `counter` is less than or equal to n (5 in our program).

We need to increase the value of the counter variable in the body of the loop. This is very important (and mostly forgotten). Failing to do so will result in an infinite loop (never-ending loop).

Finally, the result is displayed.


**While loop with else**

Same as with for loops, `while` loops can also have an optional `else` block.

The `else` part is executed if the condition in the while loop evaluates to `False`.

The while loop can be terminated with a break statement. In such cases, the else part is ignored. Hence, a while loop's else part runs if no break occurs and the condition is false.

Here is an example to illustrate this.

```python
'''Example to demonstrate the use of else in while loop'''

counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")
```

Output:

```
Inside loop
Inside loop
Inside loop
Inside else
```

Here, we use a counter variable to print the string Inside loop three times.

On the fourth iteration, the condition in while becomes False. Hence, the else part is executed.