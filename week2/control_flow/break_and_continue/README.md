In this section, you will learn to use break and continue statements to alter the flow of a loop.

**What is the use of break and continue in Python?**

In Python, `break` and `continue` statements can alter the flow of a normal loop.

Loops iterate over a block of code until the test expression is false, but sometimes we wish to terminate the current iteration or even the whole loop without checking test expression.

The `break` and `continue` statements are used in these cases.

**Python break statement**

The `break` statement terminates the loop containing it. Control of the program flows to the statement immediately after the body of the loop.

If the `break` statement is inside a nested loop (loop inside another loop), the `break` statement will terminate the innermost loop.

Syntax of break

```python
break
```

**Flow chart of break statement**

<img src="https://cdn.programiz.com/sites/tutorial2program/files/flowchart-break-statement.jpg" alt="Flow chart of break statement" style="width: 50%">


**The working of break statement in for loop and while loop is shown below.**

<img src="https://cdn.programiz.com/sites/tutorial2program/files/how-break-statement-works.jpg " alt="How break statement works" style="width: 50%">


**Example of break statement in for loop**

```python
# Use of break statement inside the loop

for val in "Python":
    if val == "h":
        break
    print(val)
```

**Output**

```
P
y
t
```

In this program, we iterate through the `"Python"` sequence. We check if the letter is `h`, upon which we break from the loop. Hence, we see in our output that all the letters up till `h` gets printed. After that, the loop terminates.


### Python continue statement

The `continue` statement is used to skip the rest of the code inside a loop for the current iteration only. Loop does not terminate but continues on with the next iteration.

**Syntax of Continue**

```python
continue
```


**Flowchart of continue**

<img src="https://cdn.programiz.com/sites/tutorial2program/files/continue-statement-flowchart.jpg" alt="Flowchart of continue statement" style="width: 50%">

The working of the continue statement in for and while loop is shown below.

<img src="https://cdn.programiz.com/sites/tutorial2program/files/how-continue-statment-works.jpg" alt="How continue statement works" style="width: 50%">


**Example: Python continue statement in for loop**

```python
# Use of continue statement inside the loop

for val in "Python":
    if val == "h":
        continue
    print(val)
```


**Output**

```
P
y
t
o
n
```

This program is same as the above example except the `break` statement has been replaced with `continue`.

We continue with the loop, if the string is `h`, not executing the rest of the block. Hence, we see in our output that all the letters except `h` gets printed.