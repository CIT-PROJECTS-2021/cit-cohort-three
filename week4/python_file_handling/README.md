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
file = open("filename.txt", "mode") # General syntax
# Modern recommended way:
# with open("filename.txt", "mode", encoding="utf-8") as f:
#     # operations
f = open("test.txt", encoding="utf-8")    # open file in current directory, encoding specified
# f = open("C:/Python38/README.txt", encoding="utf-8")  # specifying full path, encoding specified
```

We can specify the mode while opening a file. In mode, we specify whether we want to read (`r`), write (`w`), or append (`a`) to the file. We also specify if we want to open the file in text mode (`t`, default) or binary mode (`b`).

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
f = open("test.txt", encoding="utf-8")      # equivalent to 'rt', encoding specified
f = open("test.txt", 'w', encoding="utf-8")  # write in text mode, encoding specified
f = open("img.bmp",'r+b') # read and write in binary mode
```
Unlike other languages, the character 'a' does not represent the number 97 until it is encoded using an encoding scheme like ASCII or UTF-8.

Moreover, the default encoding is platform dependent. In windows, it is cp1252 but utf-8 in Linux.

So, we must not also rely on the default encoding or else our code will behave differently in different platforms.

Hence, when working with files in text mode, it is highly recommended to specify the encoding type.

```python
f = open("test.txt", mode='r', encoding='utf-8')
```

Closing Files in Python
When we are done with performing operations on the file, we need to properly close the file.

Closing a file will free up the resources that were tied with the file. While Python's garbage collector might eventually close unreferenced files, explicitly closing files is crucial.

The `close()` method is used for this:
```python
f = open("test.txt", encoding='utf-8')
# perform file operations
f.close()
```

However, if an exception occurs during file operations, the `f.close()` line might be skipped. A `try...finally` block can guarantee closure:
```python
try:
   f = open("test.txt", encoding='utf-8')
   # perform file operations
finally:
   f.close()
```

**The recommended and most Pythonic way to handle files is using the `with` statement.** This ensures that the file is automatically closed when the block inside the `with` statement is exited, even if errors occur.

```python
with open("test.txt", encoding='utf-8') as f:
   # perform file operations
   # f.close() is not needed; it's handled automatically
```
This approach is cleaner and safer.

### Writing to Files in Python
In order to write into a file in Python, we need to open it in write `w`, append a or exclusive creation `x` mode.

We need to be careful with the `w` mode, as it will overwrite the file if it already exists, erasing all previous data. If the file does not exist, it creates a new one.

Writing a string (in text mode) or a sequence of bytes (in binary mode) is done using the `write()` method. 
- In text mode, `write()` returns the number of characters written.
- In binary mode, it returns the number of bytes written.

```python
# Example of writing to a text file
content_to_write = "my first file\nThis file\n\ncontains three lines\n"
try:
    with open("test.txt", 'w', encoding='utf-8') as f:
        num_chars_written = f.write(content_to_write)
        print(f"Number of characters written: {num_chars_written}")
except IOError as e:
    print(f"Error writing to file: {e}")

```

This program will create a new file named `test.txt` in the current directory if it does not exist. If it does exist, it is overwritten with the new content.

We must include newline characters (`\n`) ourselves to distinguish different lines in text files.

### Reading Files in Python
To read a file in Python, we must open the file in reading r mode.

There are various methods available for this purpose. We can use the read(size) method to read in the size number of data. If the size parameter is not specified, it reads and returns up to the end of the file.

Assuming `test.txt` was created with the content:
```
my first file
This file

contains three lines
```
We can read it in the following ways:

```python
# Open the file (ensure it exists from the writing example)
try:
    with open("test.txt", 'r', encoding='utf-8') as f:
        # read the first 4 data
        print(f"f.read(4): '{f.read(4)}'") # Output: 'my f'

        # read the next 4 data
        print(f"f.read(4) again: '{f.read(4)}'") # Output: 'irst'
        
        # read in the rest till end of file
        print(f"f.read() for the rest:\n'{f.read()}'")
        # Output: 
        # ' file
        # This file
        # 
        # contains three lines
        # '
        
        # further reading returns empty string
        print(f"f.read() at EOF: '{f.read()}'") # Output: ''
except FileNotFoundError:
    print("Error: test.txt not found. Run the writing example first.")
except IOError as e:
    print(f"Error reading file: {e}")
```

We can see that the `read()` method returns a newline as `'\n'`. Once the end of the file is reached, we get an empty string on further reading.

We can change our current file cursor (position) using the `seek()` method. Similarly, the `tell()` method returns our current position (in number of bytes).

```python
try:
    with open("test.txt", 'r', encoding='utf-8') as f:
        f.read() # Read to the end to know file size for tell()
        file_size = f.tell() # get the current file position (end of file)
        print(f"f.tell() after reading whole file: {file_size}")

        f.seek(0)   # bring file cursor to initial position
        print(f"f.seek(0), new position: {f.tell()}")

        print("\nContent after f.seek(0):")
        print(f.read()) # read the entire file
except FileNotFoundError:
    print("Error: test.txt not found.")
except IOError as e:
    print(f"Error with seek/tell: {e}")
```
Output for `seek()`/`tell()` example (assuming `test.txt` content from above):
```
f.tell() after reading whole file: 44 
f.seek(0), new position: 0

Content after f.seek(0):
my first file
This file

contains three lines

```

We can read a file line-by-line using a `for` loop. This is both efficient and memory-friendly for large files.

```python
try:
    with open("test.txt", 'r', encoding='utf-8') as f:
        print("\nReading line by line with a for loop:")
        for line in f:
            print(line, end='') # end='' prevents double newlines
except FileNotFoundError:
    print("Error: test.txt not found.")
except IOError as e:
    print(f"Error reading line by line: {e}")

```
Output:
```
Reading line by line with a for loop:
my first file
This file

contains three lines
```

In this program, the lines in the file itself include a newline character `\n`. So, we use the end parameter of the `print()` function to avoid two newlines when printing.

Alternatively, we can use the `readline()` method to read individual lines of a file. This method reads a file up to and including the next newline character.

```python
try:
    with open("test.txt", 'r', encoding='utf-8') as f:
        print("\nUsing f.readline():")
        print(f"1st readline: '{f.readline()}'", end='') # 'my first file\n'
        print(f"2nd readline: '{f.readline()}'", end='') # 'This file\n'
        print(f"3rd readline: '{f.readline()}'", end='') # '\n'
        print(f"4th readline: '{f.readline()}'", end='') # 'contains three lines\n'
        print(f"5th readline (EOF): '{f.readline()}'")   # ''
except FileNotFoundError:
    print("Error: test.txt not found.")
except IOError as e:
    print(f"Error with readline(): {e}")
```

Lastly, the `readlines()` method reads all remaining lines from the file and returns them as a list of strings. Each string in the list includes the newline character.

```python
try:
    with open("test.txt", 'r', encoding='utf-8') as f:
        lines_list = f.readlines()
        print(f"\n\nUsing f.readlines():\n{lines_list}")
        # Output: ['my first file\n', 'This file\n', '\n', 'contains three lines\n']
except FileNotFoundError:
    print("Error: test.txt not found.")
except IOError as e:
    print(f"Error with readlines(): {e}")
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

### Directory and File Path Management

Python provides robust tools for managing directories and file paths. While the `os` module has traditionally been used, the `pathlib` module (introduced in Python 3.4) offers an object-oriented and more readable approach.

**Using `pathlib.Path` (Recommended)**

The `pathlib` module provides `Path` objects to represent file system paths.

```python
from pathlib import Path
```

**Creating a Directory:**

```python
# Using pathlib
p_newdir = Path("newdir_pathlib")
try:
    p_newdir.mkdir(exist_ok=True) # exist_ok=True prevents error if directory already exists
    print(f"Directory '{p_newdir}' created or already exists.")
except OSError as e:
    print(f"Error creating directory {p_newdir}: {e}")

# Equivalent with os module
import os
os_newdir = "newdir_os"
if not os.path.exists(os_newdir):
    os.mkdir(os_newdir)
    print(f"Directory '{os_newdir}' created.")
else:
    print(f"Directory '{os_newdir}' already exists.")
```

**Creating Nested Directories:**

```python
# Using pathlib
p_nested = Path("parent_pathlib/child_subdir")
try:
    p_nested.mkdir(parents=True, exist_ok=True) # parents=True creates parent dirs if needed
    print(f"Nested directory '{p_nested}' created or already exists.")
except OSError as e:
    print(f"Error creating nested directory {p_nested}: {e}")

# Equivalent with os module
import os
os_nested = "parent_os/child_subdir_os"
try:
    os.makedirs(os_nested, exist_ok=True)
    print(f"Nested directory '{os_nested}' created or already exists.")
except OSError as e:
    print(f"Error creating nested directory {os_nested}: {e}")
```

**Deleting a Directory:**
Note: These methods typically only work if the directory is empty.

```python
# Using pathlib
# Assuming p_nested from above exists and is empty
try:
    p_nested_child = Path("parent_pathlib/child_subdir")
    p_nested_child.rmdir() # Remove child_subdir
    print(f"Directory '{p_nested_child}' deleted.")
    Path("parent_pathlib").rmdir() # Remove parent_pathlib
    print(f"Directory 'parent_pathlib' deleted.")
except FileNotFoundError:
    print("Directory not found for deletion.")
except OSError as e: # Catches error if directory is not empty
    print(f"Error deleting directory: {e}")


# Equivalent with os module
# Assuming os_nested from above exists and is empty
try:
    os.rmdir("parent_os/child_subdir_os")
    print("Directory 'parent_os/child_subdir_os' deleted.")
    os.rmdir("parent_os")
    print("Directory 'parent_os' deleted.")
except FileNotFoundError:
    print("Directory not found for deletion with os.rmdir.")
except OSError as e:
    print(f"Error deleting directory with os.rmdir: {e}")

# os.removedirs can remove nested empty directories:
# os.removedirs("parent_os/child_subdir_os") # This would remove both if empty
```

**Renaming a File or Directory:**

```python
# Using pathlib
p_old = Path("original_name_pathlib")
p_new = Path("renamed_name_pathlib")
try:
    p_old.mkdir(exist_ok=True) # Create a directory to rename
    p_old.rename(p_new)
    print(f"Directory '{p_old}' (original) renamed to '{p_new}'.")
    p_new.rmdir() # Clean up
except OSError as e:
    print(f"Error renaming with pathlib: {e}")


# Equivalent with os module
os_old = "original_name_os"
os_new = "renamed_name_os"
try:
    if not os.path.exists(os_old):
        os.mkdir(os_old)
    os.rename(os_old, os_new)
    print(f"Directory '{os_old}' (original) renamed to '{os_new}'.")
    os.rmdir(os_new) # Clean up
except OSError as e:
    print(f"Error renaming with os: {e}")
```

**Moving a File or Directory:**
Moving is often achieved by renaming to a different path.

```python
# Using pathlib
source_dir = Path("source_dir_pathlib")
source_dir.mkdir(exist_ok=True)
# Example file within source_dir
# (Path(source_dir) / "file_to_move.txt").write_text("Hello", encoding="utf-8") 

destination_dir_parent = Path("destination_parent_pathlib")
destination_dir_parent.mkdir(exist_ok=True)
new_location = destination_dir_parent / source_dir.name # e.g. destination_parent_pathlib/source_dir_pathlib

try:
    source_dir.rename(new_location)
    print(f"Directory '{source_dir}' moved to '{new_location}'.")
    # Clean up
    # (new_location / "file_to_move.txt").unlink(missing_ok=True)
    new_location.rmdir()
    destination_dir_parent.rmdir()
except OSError as e:
    print(f"Error moving with pathlib: {e}")


# Equivalent with os module
os_source_dir = "source_dir_os"
if not os.path.exists(os_source_dir):
    os.mkdir(os_source_dir)

os_dest_parent = "destination_parent_os"
if not os.path.exists(os_dest_parent):
    os.mkdir(os_dest_parent)
os_new_location = os.path.join(os_dest_parent, os_source_dir)

try:
    os.rename(os_source_dir, os_new_location)
    print(f"Directory '{os_source_dir}' moved to '{os_new_location}'.")
    # Clean up
    os.rmdir(os_new_location)
    os.rmdir(os_dest_parent)
except OSError as e:
    print(f"Error moving with os: {e}")

```
`pathlib` offers many more features for path manipulation, checking existence, iterating over directory contents, etc., making it a powerful tool for modern Python development.

### Error Handling for File Operations

When working with files, various errors can occur. Common ones include `FileNotFoundError` if a file doesn't exist when trying to read it, or `PermissionError` if the script doesn't have the necessary permissions. It's good practice to handle these exceptions using `try-except` blocks.

```python
filename = "non_existent_file.txt"
try:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except PermissionError:
    print(f"Error: You don't have permission to read '{filename}'.")
except IOError as e: # General I/O error
    print(f"An I/O error occurred: {e}")

# Example for permission error (conceptual, actual error depends on environment)
# try:
#    with open("/root/protected_file.txt", 'r', encoding='utf-8') as f: # Assuming no permission
#        content = f.read()
# except PermissionError:
#    print("Error: Permission denied to access a protected file.")
```

### Working with Common File Formats (CSV & JSON)

Python's standard library includes modules for easily working with common structured data formats like CSV and JSON.

**CSV (Comma-Separated Values)**

CSV files are simple text files where values are typically separated by commas. The `csv` module helps manage the nuances of CSV formatting.

**Writing to a CSV file:**
```python
import csv

data_to_write = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 24, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]
csv_filename = "users.csv"

try:
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data_to_write)
    print(f"Data written to {csv_filename}")
except IOError as e:
    print(f"Error writing CSV: {e}")
```
Note: `newline=''` is recommended when opening CSV files for writing to prevent blank rows.

**Reading from a CSV file:**
```python
import csv

csv_filename = "users.csv" # Assuming it was created above
try:
    with open(csv_filename, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        print(f"\nReading data from {csv_filename}:")
        for row in reader:
            print(row)
except FileNotFoundError:
    print(f"Error: {csv_filename} not found.")
except IOError as e:
    print(f"Error reading CSV: {e}")
```

**JSON (JavaScript Object Notation)**

JSON is a lightweight data-interchange format that is easily readable by humans and parsable by machines. The `json` module is used to work with JSON data.

**Writing Python dictionary to a JSON file:**
```python
import json

data_to_write = {
    "name": "Alice Wonderland",
    "age": 30,
    "email": "alice@example.com",
    "isStudent": False,
    "courses": [
        {"title": "Python 101", "credits": 3},
        {"title": "Advanced Python", "credits": 4}
    ]
}
json_filename = "user_data.json"

try:
    with open(json_filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(data_to_write, jsonfile, indent=4) # indent for pretty printing
    print(f"\nData written to {json_filename}")
except IOError as e:
    print(f"Error writing JSON: {e}")
```

**Reading from a JSON file into a Python dictionary:**
```python
import json

json_filename = "user_data.json" # Assuming it was created above
try:
    with open(json_filename, 'r', encoding='utf-8') as jsonfile:
        data_read = json.load(jsonfile)
        print(f"\nData read from {json_filename}:")
        print(data_read)
        print(f"Name: {data_read.get('name')}")
except FileNotFoundError:
    print(f"Error: {json_filename} not found.")
except json.JSONDecodeError:
    print(f"Error: Could not decode JSON from {json_filename}.")
except IOError as e:
    print(f"Error reading JSON: {e}")
```
These modules simplify handling the specifics of these formats, such as escaping special characters in CSV or converting between Python types and JSON types.

