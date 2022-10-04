---
description: >-
    Reverse Cipher is a simple cipher that reverses the order of the characters in the message. It is a weak cipher because it is very easy to crack. It is also known as the reverse cipher.
---

### Algorithm of Reverse Cipher
The algorithm of reverse cipher holds the following features −

    - Reverse Cipher uses a pattern of reversing the string of plain text to convert as cipher text.

    - The process of encryption and decryption is same.

    - To decrypt cipher text, the user simply needs to reverse the cipher text to get the plain text.

![Reverse Cipher](https://www.tutorialspoint.com/cryptography_with_python/images/dawback.jpg)

### Example
Consider an example where the statement This is program to explain reverse cipher is to be implemented with reverse cipher algorithm. The following python code uses the algorithm to obtain the output.

```python
# Python program to illustrate Reverse Cipher Technique

def reverse(text):
    result = ""
    for i in range(len(text) - 1, -1, -1):
        result += text[i]
    return result

# plain text
text = "This is program to explain reverse cipher"

# calling the reverse function
s = reverse(text)

print("Plain Text : ", text)
print("Cipher: ", s)
```

When the above code is executed, it produces the following result −

```commandline
Plain Text :  This is program to explain reverse cipher
Cipher:  repihc esrever ylniapxe ot margorp si sihT
```

### Explaination
The above code uses the reverse function to reverse the string of plain text. The reverse function takes the string as an argument and returns the reversed string. The reversed string is stored in the variable s. The variable s is printed as the cipher text.

### Assignment.
1. Write a python program to implement reverse cipher algorithm using a while loop.
2. Using lambda function, write a python program to implement reverse cipher algorithm.


