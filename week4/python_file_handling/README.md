---
description: >-
    This week we will learn how to read and write files in Python. We will also learn
    how to use the `with` statement to open files.
---

# Python File Handling

**Files**

Files are named locations on disk to store related information. They are used to permanently store data in a non-volatile memory (e.g. hard disk).

Since Random Access Memory (RAM) is volatile (which loses its data when the computer is turned off), we use files for future use of the data by permanently storing them.

When we want to read from or write to a file, we need to open it first. When we are done, it needs to be closed so that the resources that are tied with the file are freed.

Hence, in Python, a file operation takes place in the following order:

- Open a file
- Read or write (perform operation)
- Close the file

### Opening Files in Python
Python has a built-in `open()` function to open a file. This function returns a file object, also called a handle, as it is used to read or modify the file accordingly.

The `open()` function takes two parameters; filename, and mode.

```python
file = open("filename.txt", "mode") # syntax
f = open("test.txt")    # open file in current directory
f = open("C:/Python38/README.txt")  # specifying full path
```

We can specify the mode while opening a file. In mode, we specify whether we want to read r, write w or append a to the file. We can also specify if we want to open the file in text mode or binary mode.

The default is reading in text mode. In this mode, we get strings when reading from the file.

On the other hand, binary mode returns bytes and this is the mode to be used when dealing with non-text files like images or executable files.

There are various modes available for opening a file. The default mode is `r`, which means open for reading in text mode. In addition, there are several modes:

| Mode | Description |
| --- | --- |
|- `r` | - open for reading (default)
|- `w` | - open for writing, truncating the file first
|- `x` | - open for exclusive creation, failing if the file already exists
|- `a` | - open for writing, appending to the end of the file if it exists
|- `b` | - binary mode
|- `t` | - text mode (default)
|- `+` | - open for updating (reading and writing)
|- `w+`|  - open for reading and writing, truncating the file first
|- `r+`|  - open for reading and writing, starting at the beginning of the file
|- `a+`|  - open for reading and writing, appending to the end of the file if it exists
|- `x+`|  - open for updating, failing if the file already exists
|- `b+`|  - open for updating in binary mode
|- `wb`|  - open for writing in binary mode
|- `rb`|  - open for reading in binary mode
|- `ab`|  - open for appending in binary mode
|- `rt`|  - open for reading in text mode (default)
|- `wt`|  - open for writing in text mode
|- `at`|  - open for appending in text mode
|- `xt`|  - open for exclusive creation in text mode, failing if the file already exists

```python
f = open("test.txt")      # equivalent to 'r' or 'rt'
f = open("test.txt",'w')  # write in text mode
f = open("img.bmp",'r+b') # read and write in binary mode
```
Unlike other languages, the character a does not imply the number 97 until it is encoded using ASCII (or other equivalent encodings).

Moreover, the default encoding is platform dependent. In windows, it is cp1252 but utf-8 in Linux.

So, we must not also rely on the default encoding or else our code will behave differently in different platforms.

Hence, when working with files in text mode, it is highly recommended to specify the encoding type.

```python
f = open("test.txt", mode='r', encoding='utf-8')
```

Closing Files in Python
When we are done with performing operations on the file, we need to properly close the file.

Closing a file will free up the resources that were tied with the file. It is done using the close() method available in Python.

Python has a garbage collector to clean up unreferenced objects but we must not rely on it to close the file.

```python
f = open("test.txt", encoding = 'utf-8')
# perform file operations
f.close()
```

This method is not entirely safe. If an exception occurs when we are performing some operation with the file, the code exits without closing the file.

A safer way is to use a `try...finally` block.

```python
try:
   f = open("test.txt", encoding = 'utf-8')
   # perform file operations
finally:
   f.close()
```

This way, we are guaranteeing that the file is properly closed even if an exception is raised that causes program flow to stop.

The best way to close a file is by using the with statement. This ensures that the file is closed when the block inside the with statement is exited.

We don't need to explicitly call the `close()` method. It is done internally.

```python
with open("test.txt", encoding = 'utf-8') as f:
   # perform file operations

```

### Writing to Files in Python
In order to write into a file in Python, we need to open it in write `w`, append a or exclusive creation `x` mode.

We need to be careful with the `w` mode, as it will overwrite into the file if it already exists. Due to this, all the previous data are erased.

Writing a string or sequence of bytes (for binary files) is done using the `write() ` method. This method returns the number of characters written to the file.

```python
with open("test.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")
```

This program will create a new file named `test.txt` in the current directory if it does not exist. If it does exist, it is overwritten.

We must include the newline characters ourselves to distinguish the different lines.

### Reading Files in Python
To read a file in Python, we must open the file in reading r mode.

There are various methods available for this purpose. We can use the read(size) method to read in the size number of data. If the size parameter is not specified, it reads and returns up to the end of the file.

We can read the text.txt file we wrote in the above section in the following way:

```python
>>> f = open("test.txt",'r',encoding = 'utf-8')
>>> f.read(4)    # read the first 4 data
'This'

>>> f.read(4)    # read the next 4 data
' is '

>>> f.read()     # read in the rest till end of file
'my first file\nThis file\ncontains three lines\n'

>>> f.read()  # further reading returns empty sting
''
```

We can see that the `read()` method returns a newline as `'\n'`. Once the end of the file is reached, we get an empty string on further reading.

We can change our current file cursor (position) using the seek() method. Similarly, the `tell()` method returns our current position (in number of bytes).

```python
>>> f.tell()    # get the current file position
56

>>> f.seek(0)   # bring file cursor to initial position
0

>>> print(f.read())  # read the entire file

This is my first file
This file
contains three lines
```

We can read a file line-by-line using a for loop. This is both efficient and fast.

```python
>>> for line in f:
...     print(line, end = '')
...
This is my first file
This file
contains three lines
```

In this program, the lines in the file itself include a newline character `\n`. So, we use the end parameter of the `print()` function to avoid two newlines when printing.

Alternatively, we can use the `readline()` method to read individual lines of a file. This method reads a file till the newline, including the newline character.

```python
>>> f.readline()
'This is my first file\n'

>>> f.readline()
'This file\n'

>>> f.readline()
'contains three lines\n'

>>> f.readline()
''
```

Lastly, the `readlines()` method returns a list of remaining lines of the entire file. All these reading methods return empty values when the end of file (EOF) is reached.

```python
>>> f.readlines()
['This is my first file\n', 'This file\n', 'contains three lines\n']
```

### Python File Methods
There are various methods available with the file object. Some of them have been used in the above examples.

Here is the complete list of methods in text mode with a brief description:

|Method	| Description|
|---|---|
|close()	|Closes an opened file. It has no effect if the file is already closed.
|detach()	|Separates the underlying binary buffer from the TextIOBase and returns it.
|fileno()	|Returns an integer number (file descriptor) of the file.
|flush()	|Flushes the write buffer of the file stream.
|isatty()	|Returns True if the file stream is interactive.
|read(n)	|Reads at most n characters from the file. Reads till end of file if it is negative or None.
|readable()	|Returns True if the file stream can be read from.
|readline(n=-1)	|Reads and returns one line from the file. Reads in at most n bytes if specified.
|readlines(n=-1)	|Reads and returns a list of lines from the file. Reads in at most n bytes/characters if specified.
|seek(offset,from=SEEK_SET)	|Changes the file position to offset bytes, in reference to from (start, current, end).
|seekable()	|Returns True if the file stream supports random access.
|tell()	|Returns an integer that represents the current position of the file's object.
|truncate(size=None)	|Resizes the file stream to size bytes. If size is not specified, resizes to current location.
|writable()	|Returns True if the file stream can be written to.
|write(s)	|Writes the string s to the file and returns the number of characters written.
|writelines(lines)	|Writes a list of lines to the file.

### Python Directory and File Management
In this section, we will learn how to create, delete, rename, and move files and directories in Python.

### Creating a Directory
In order to create a directory in Python, we can use the `mkdir()` method of the `os` module.

```python
import os
os.mkdir("newdir")
```

This will create a new directory named `newdir` in the current working directory.

We can also create a nested directory using the `makedirs()` method. This method creates all intermediate-level directories if they do not exist.

```python
import os
os.makedirs("newdir/subdir")
```

This will create a new directory named `subdir` in the `newdir` directory.

### Deleting a Directory
In order to delete a directory in Python, we can use the `rmdir()` method of the `os` module.

```python
import os
os.rmdir("newdir/subdir")
```

This will delete the `subdir` directory from the `newdir` directory.

We can also delete a nested directory using the `removedirs()` method. This method removes all intermediate-level directories if they are empty.

```python
import os
os.removedirs("newdir/subdir")
```

This will delete the `subdir` directory from the `newdir` directory.

### Renaming a Directory
In order to rename a directory in Python, we can use the `rename()` method of the `os` module.

```python
import os
os.rename("newdir", "olddir")
```

This will rename the `newdir` directory to `olddir`.

### Moving a Directory
In order to move a directory in Python, we can use the `rename()` method of the `os` module.

```python
import os
os.rename("olddir", "newdir/olddir")
```

This will move the `olddir` directory to the `newdir` directory.

