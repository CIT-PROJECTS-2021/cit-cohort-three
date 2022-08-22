Often, you need to execute some statements only if some condition holds, or choose statements to execute depending on several mutually exclusive conditions. 

The Python compound statement if, which uses if, elif, and else clauses, lets you conditionally execute blocks of statements. Here’s the syntax for the if statement:

```python
if expression:
    statement(s)
elif expression:
    statement(s)
elif expression:
    statement(s)
...
else:
    statement(s)
```
<br>

Below is a flowchart that shows the execution of the if statement:

<img src="https://www.guru99.com/images/2013/04/if_then_flowchart.png" alt="python if statement">

<br>

The elif and else clauses are optional. Note that unlike some languages, Python does not have a switch statement, so you must use if, elif, and else for all conditional processing.

Here’s a typical if statement:

```python
if x < 0: print "x is negative"
elif x % 2: print "x is positive and odd"
else: print "x is even and non-negative"
```
<br>
When there are multiple statements in a clause (i.e., the clause controls a block of statements), the statements are placed on separate logical lines after the line containing the clause’s keyword (known as the header line of the clause) and indented rightward from the header line. 

The block terminates when the indentation returns to that of the clause header (or further left from there). 

When there is just a single simple statement, as here, it can follow the `:` on the same logical line as the header, but it can also be placed on a separate logical line, immediately after the header line and indented rightward from it. 

Many Python practitioners consider the separate-line style more readable:

```python
if x < 0:
    print "x is negative"
elif x % 2:
    print "x is positive and odd"
else:
    print "x is even and non-negative"
```
<br>
You can use any Python expression as the condition in an if or elif clause. 

When you use an expression this way, you are using it in a Boolean context. In a Boolean context, any value is taken as either true or false. 

As we discussed earlier, any non-zero number or non-empty string, tuple, list, or dictionary evaluates as true. 

Zero (of any numeric type), None, and empty strings, tuples, lists, and dictionaries evaluate as false. When you want to test a value x in a Boolean context, use the following coding style:

```python
if x:
```
<br>
This is the clearest and most Pythonic form. Don’t use:

```python
if x is True:
if x =  = True:
if bool(x):
```
<br>
There is a crucial difference between saying that an expression “returns True" (meaning the expression returns the value 1 intended as a Boolean result) and saying that an expression “evaluates as true” (meaning the expression returns any result that is true in a Boolean context). 

When testing an expression, you care about the latter condition, not the former.

If the expression for the if clause evaluates as true, the statements following the if clause execute, and the entire if statement ends.

Otherwise, the expressions for any elif clauses are evaluated in order. The statements following the first elif clause whose condition is true, if any, are executed, and the entire if statement ends. Otherwise, if an else clause exists, the statements following it are executed.