---
description: >-
  This lecture will introduce you to some of the built-in modules in Python. You
  will learn how to use these modules to perform common tasks in Python.
---
In programming terminology, function is a separate, complete and reusable software component. Long and complex logic in a program is broken into smaller, independent and reusable blocks of instructions usually called a module, a subroutine or function. It is designed to perform a specific task that is a part of entire process. This approach towards software development is called modular programming.

Such a program has a main routine through which smaller independent modules (functions) are called upon. Each When called, a function performs a specified task and returns the control back to the calling routine, optionally along with result of its process.

Python interpreter has a number of built-in functions. They are always available for use in every interpreter session. Many of them have been discussed in previously. For example `print()` and `input()` for I/O, number conversion functions (`int()`, `float()`, `complex()`), data type conversions (`list()`, `tuple()`, `set()`) etc. Here is complete list of Python's built-in functions:

Built-in Functions
***


|<!-- --> |<!-- --> | <!-- --> |<!-- --> | <!-- --> |
|:---:|:---:|:---:|:---:|:---:|
|abs()|dict()|help()|min()|setattr()|
|all()|dir()|hex()|next()|slice()|
|any()|divmod()|id()|object()|sorted()|
|ascii()|enumerate()|input()|oct()|staticmethod()|
|bin()|eval()|int()|open()|str()|
|bool()|exec()|isinstance()|ord()|sum()|
|bytearray()|filter()|issubclass()|pow()|super()|
|bytes()|float()|iter()|print()|tuple()|
|callable()|format()|len()|property()|type()|
|chr()|frozenset()|list()|range()|vars()|
|classmethod()|getattr()|locals()|repr()|zip()|
|compile()|globals()|map()|reversed()|\_\_import\_\_()|
|complex()|hasattr()|max()|round()| |

In addition to built-in functions, a large number of pre-defined functions are also available as a part of libraries bundled with Python distributions. However they are not available for use automatically. These functions are defined in modules. A module is a file containing definition of functions, classes, variables, constants or any other Python object. Standard distribution of Python contains a large number of modules, generally known as built-in modules. Each built-in module contains resources for certain specific functionalities such as OS management, disk IO, networking, database connectivity etc.

Most of the times, built-in modules are written in C and integrated with Python interpreter.

A built-in module may be a Python script (with .py extension) containing useful utilities.

To display list of all available modules, use following command in Python console:
```python
>>> help('modules')
```

Resources from other modules are loaded by import statement. The general format of using a function in any module is like this:

```python
import module

module.function([arguments if any])
```


The `sqrt()` function in math module returns square root of a number.

```python
>>> import math
>>> math.sqrt(100)
10.0
```

In this chapter we shall discuss some of the frequently used functions from certain built-in modules.

- os module
- random module
- math module
- time module
- sys module
- collections module
- statistics module
- os module

This module has functions to perform many tasks of operating system.

### `mkdir()` function:
We can create a new directory using `mkdir()` function from os module.

```python
>>> import os
>>> os.mkdir("d:\\tempdir")
```

A new directory corresponding to path in string argument in the function will be created. If we open D drive in Windows explorer we should notice tempdir folder created.

### `chdir()` function:
To change current working directory to use `chdir()` function.

```python
>>> import os
>>> os.chdir("d:\\temp")
```

### `getcwd()` function:

This function in returns name off current working directory.

```python
>>> os.getcwd()
'd:\\temp'
```

Directory paths can also be relative. If current directory is set to D drive and then to temp without mentioning preceding path, then also current working directory will be changed to `d:\temp`

```python
>>> os.chdir("d:\\")
>>> os.getcwd()
'd:\\'
>>> os.chdir("temp")
>>> os.getcwd()
'd:\\temp'
```

In order to set current directory to parent directory use `".."` as the argument to `chdir()` function.

```python
>>> os.chdir("d:\\temp")
>>> os.getcwd()
'd:\\temp'
>>> os.chdir("..")
>>> os.getcwd()
'd:\\'
```

### `rmdir()` function:

The `rmdir()` function in os module removes a specified directory either with absolute or relative path. However it should not be the current working directory and it should be empty.

```python
>>> os.chdir("tempdir")
>>> os.getcwd()
'd:\\tempdir'
>>> os.rmdir("d:\\temp")
PermissionError: [WinError 32] The process cannot access the file because it is being used by another process: 'd:\\temp'
>>> os.chdir("..")
>>> os.rmdir("temp")
```

### `listdir()` function:

The os module has `listdir()` function which returns list of all files in specified directory.

```python
>>> os.listdir("c:\\Users")

['acer', 'All Users', 'Default', 'Default User', 'desktop.ini', 'Public']
```

### random module

Python’s standard library contains random module which defines various functions for handling randomization. Python uses a pseudo-random generator based upon Mersenne Twister algorithm that produces 53-bit precision floats. Functions in this module depend on pseudo-random number generator function `random()` which generates a random float number between `0.0` and `1.0`.

### `random.random()` function: 
Returns a random float number between `0.0` to `1.0`. The function doesn’t need any arguments

```python
>>> import random
>>> random.random()
0.755173688207591
```

Other functions in random module are described here:

### `random.randint()` function:
 Returns a random integer between the specified integers

```python
>>> import random
>>> random.randint(1,100)
58
>>> random.randint(1,100)
91
```

### `random.randrange()` function:
 Returns a random element from the range created by `start`, `stop` and `step` arguments. The `start` , `stop` and `step` parameters behave similar to `range()` function.

```python
>>> random.randrange(1,10)
2
>>> random.randrange(1,10,2)
3
>>> random.randrange(0,101,10)
40
```

### `random.choice()` function:
 Returns a randomly selected element from a sequence object such as string, list or tuple. An empty sequence as argument raises `IndexError`

```python
>>> import random
>>> random.choice('computer')
'o'
>>> random.choice([12,23,45,67,65,43])
65
>>> random.choice((12,23,45,67,65,43))
23
```

### `random.shuffle()` function: 
This functions randomly reorders elements in a list.

```python
>>> numbers=[12,23,45,67,65,43]
>>> random.shuffle(numbers)
>>> numbers
[23, 12, 43, 65, 67, 45]
>>> random.shuffle(numbers)
>>> numbers
[23, 43, 65, 45, 12, 67]
```

### math module
This module presents commonly required mathematical functions.

- trigonometric functions
- representation functions
- logarithmic functions
- angle conversion functions
- statistical functions
- hyperbolic functions
- special functions

In addition, two mathematical constants are also defined in this module.

`Pie π` which is defined as ratio of circumference to diameter of a circle and its value is `3.141592653589793`, is available in math module.

```python
>>> import math
>>> math.pi
3.141592653589793
```

Another mathematical constant in this module is `e`. It is called Euler’s number and is a base of natural logarithm. Its value is `2.718281828459045`

```python
>>> math.e
2.718281828459045
```

This module contains functions for calculating various trigonometric ratios for a given angle. The functions (`sin`, `cos`,` tan` etc.) need angle in radians as argument. We on the other hand are used to express angle in degrees. The math module presents two angle conversion functions (`degrees()` and `radians()`) to convert angle in degrees to radians and vice versa.

### Trigonometric functions:

`radians()`: converts angle in degrees to radians.(Note: `π` radians is equivalent to `180` degrees)

```python
>>> math.radians(30)
0.5235987755982988
```

`degrees()`: converts angle in radians to degree.

```python
>>> math.degrees(math.pi/6)
29.999999999999996
```

The ollowing statements show `sin`, `cos` and `tan` ratios for angle of `30` degrees (`0.5235987755982988 radians`)

```python
>> math.sin(0.5235987755982988)
0.49999999999999994
>>> math.cos(0.5235987755982988)
0.8660254037844387
>>> math.tan(0.5235987755982988)
0.5773502691896257
sin(30)	0.5	 0.49999999999999994
cos(30)	3/2  	 0.8660254037844387)
tan(30)	1/2	 0. 5773502691896257
```

`math.log()`: returns natural logarithm of given number. Natural logarithm is calculated to the base e.

`math.log10()`: returns base-10 logarithm or standard logarithm of given number.

```python
>>> math.log10(10)
1.0
```

`math.exp()`: returns a float number after raising e (`math.e`) to given number. `exp(x)` is equivalent to `e**x`

```python
>>> math.log10(10)
1.0
>>> math.e**10
22026.465794806703
```

`math.pow()`: This function receives two float arguments, raises first to second and returns the result. `pow(4,4)` is equivalent to `4**4`

```python
>>> math.pow(4,4)
256.0
>>> 4**4
256
```

`math.sqrt()`: This function computes square root of given number 

```python
>>> math.sqrt(100)
10.0
>>> math.sqrt(3)
1.7320508075688772
```

### Representation functions:
The `ceil()` function approximates given number to smallest integer greater than or equal to given floating point number. The `floor()` function returns a largest integer less than or equal to given number

```python
>>> math.ceil(4.5867)
5
>>> math.floor(4.5687)
4
```

### sys module
This module provides functions and variables used to manipulate different parts of the Python runtime environment.

### `sys.argv`
This return list of command line arguments passed to a Python script.  Item at 0th index of this list is always the name of the script. Rest of the arguments are stored at subsequent indices.

Here is a Python script (test.py) consuming two arguments from command line.

```python
import sys
print ("My name is {}. I am {} years old".format(sys.argv[1], sys.argv[2]))
```

This script is executed from command line as follows:

```bash
C:\python37>python tmp.py Iden 25
My name is Iden. I am 25 years old
```

### `sys.exit`
This causes program to end and return to either Python console or command prompt. It is used to safely exit from program in case of exception.


### `sys.maxsize`
It returns the largest integer a variable can take.

```python
>>> import sys
>>> sys.maxsize
9223372036854775807
```

### `sys.path`
This is an environment variable that returns search path for all Python modules.

```python
>>> sys.path
['', 'C:\\python37\\Lib\\idlelib', 'C:\\python37\\python36.zip', 'C:\\python37\\DLLs', 'C:\\python37\\lib', 'C:\\python37', 'C:\\Users\\acer\\AppData\\Roaming\\Python\\Python37\\site-packages', 'C:\\python37\\lib\\site-packages']
```

`sys.stdin`, `sys.stdout`, `sys.stderr`

These are file objects used by the interpreter for standard input, output and errors. stdin is used for all interactive input (Python shell). stdout is used for the output of `print()` and of `input()`. The interpreter’s prompts and error messages go to `stderr.`

### `sys.version`
This attribute displays a string containing version number of current Python interpreter.

### collections module
This module provides alternatives to built-in container data types such as `list`, `tuple` and `dict`.

### `namedtuple()` function:
This function is a factory function that returns object of  a tuple subclass with named fields. Any valid Python identifier may be used for a field name except for names starting with an underscore.

### `collections.namedtuple(typename, field-list)`
The typename parameter is the subclass of tuple. Its object has attributes mentioned in field list. These field attributes can be accessed by lookup as well as by its index.

Following statement declares a employee namedtuple having name, age and salary as fields

```python
>>> import collections
>>> employee=collections.namedtuple('employee', [name, age, salary])
To create a new object of this namedtuple
>>> e1=employee("Iden", 251, 20000)
```

Values of the field can be accessible by attribute lookup

```python
>>> e1.name
'Iden'
```

Or by index

```python
>>> e1[0]
'Iden'
```
### `OrderedDict()` function

Ordered dictionary is similar to a normal dictionary. However, normal dictionary the order of insertion of keys in it whereas ordered dictionary object remembers the same. The key-value pairs in normal dictionary object appear in arbitrary order.

```python
>>> d1={}
>>> d1['A']=20
>>> d1['B']=30
>>> d1['C']=40
>>> d1['D']=50
```

We then traverse the dictionary by a for loop,

```python
>>> for k,v in d1.items():
print (k,v)

A 20
B 30
D 50
C 40
```

But in case of OrderedDict object:

```python
>>> import collections
>>> d2=collections.OrderedDict()
>>> d2['A']=20
>>> d2['B']=30
>>> d2['C']=40
>>> d2['D']=50
```

Key-value pairs will appear in the order of their insertion.

```python
>>> for k,v in d2.items():
print (k,v)
A 20
B 30
C 40
D 50
```

### `deque()` function

A deque object supports append and pop operation from both ends of a list. It is more memory efficient than a normal list object because in a normal list, removing one of iem causes all items to its right to be shifted towards left. Hence it is very slow.

```python
>>> q=collections.deque([10,20,30,40])
>>> q.appendleft(110)
>>> q
deque([110, 10, 20, 30, 40])
>>> q.append(41)
>>> q
deque([0, 10, 20, 30, 40, 41])
>>> q.pop()
40
>>> q
deque([0, 10, 20, 30, 40])
>>> q.popleft()
110
>>> q
deque([10, 20, 30, 40])
```

### statistics module
This module provides following statistical functions :

`mean()` : calculate arithmetic mean of numbers in a list

```python
>>> import statistics
>>> statistics.mean([2,5,6,9])
5.5
```

`median()` : returns middle value of numeric data in a list. For odd items in list, it returns value at `(n+1)/2` position. For even values, average of values at `n/2` and `(n/2)+1` positions is returned.

```python
>>> import statistics
>>> statistics.median([1,2,3,8,9])
3
>>> statistics.median([1,2,3,7,8,9])
5.0
```

`mode()`: returns most repeated data point in the list.

```python
>>> import statistics
>>> statistics.mode([2,5,3,2,8,3,9,4,2,5,6])
2
```

`stdev()` : calculates standard deviation on given sample in the form of list.

```python
>>> import statistics
>>> statistics.stdev([1,1.5,2,2.5,3,3.5,4,4.5,5])
1.3693063937629153
```

### time module
This module has many time related functions.

`time()`:

This function returns current system time in ticks. The ticks is number of seconds elapsed after epoch time i.e. `12.00 am, January 1, 1970.`

```python
>>> time.time()
1544348359.1183174
```

`localtime()`:

This function translates time in ticks in a time tuple notation.

```python
>>> tk=time.time()
>>> time.localtime(tk)
time.struct_time(tm_year=2018, tm_mon=12, tm_mday=9, tm_hour=15, tm_min=11, tm_sec=25, tm_wday=6, tm_yday=343, tm_isdst=0)
```

`asctime()`:
This functions returns a readable format of local time

```python
>>> tk=time.time()
>>> tp=time.localtime(tk)
>>> time.asctime(tp)
'Sun Dec  9 15:11:25 2018'
```

`ctime()`:
This function returns string representation of system's current time

```python
>>> time.ctime()
'Sun Dec  9 15:17:40 2018'
```

`sleep()`:
This function halts current program execution for a specified duration in seconds.

```python
>>> time.ctime()
'Sun Dec  9 15:19:14 2018'
>>> time.sleep(20)
>>> time.ctime()
'Sun Dec  9 15:19:34 2018'
```

Few more built-in modules will be discussed in separate subsequent later chapters of this course.

- re module
- threading module
- cgi module
- tkinter module
- csv module
- pickle module
- socket module
- sqlite3 module
- json module
