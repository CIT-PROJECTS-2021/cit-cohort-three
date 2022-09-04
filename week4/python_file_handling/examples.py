# Programs to demonstrate file handling in Python

# Open a file for reading
f = open("test.txt", "r")
print(f.read())
f.close()

# Open a file for writing
f = open("test.txt", "w")
f.write("This is a test file")
f.close()

# Open a file for appending
f = open("test.txt", "a")
f.write("This is a test file")
f.close()

# Open a file for reading and writing
f = open("test.txt", "r+")
f.write("This is a test file")
f.close()

# Open a file for reading and writing
f = open("test.txt", "w+")
f.write("This is a test file")
f.close()

# Open a file for reading and writing
f = open("test.txt", "a+")
f.write("This is a test file")
f.close()

# Open a binary file for reading
f = open("test.txt", "rb")
print(f.read())
f.close()

# Open a binary file for writing
f = open("test.txt", "wb")
f.write("This is a test file")  
f.close()

# Open a binary file for appending
f = open("test.txt", "ab")
f.write("This is a test file")
f.close()

# Open a binary file for reading and writing
f = open("test.txt", "r+b")
f.write("This is a test file")
f.close()