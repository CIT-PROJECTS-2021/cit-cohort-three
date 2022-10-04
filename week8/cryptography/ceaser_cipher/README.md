---
description: >-
    Ceaser cipher is a simple encryption technique. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example with a shift of 1, A would be replaced by B, B would become C, and so on.
---

### Algorithm of Caesar Cipher
The algorithm of Caesar cipher holds the following features −

    - Caesar Cipher Technique is the simple and easy method of encryption technique.

    - It is simple type of substitution cipher.

    - Each letter of plain text is replaced by a letter with some fixed number of positions down with alphabet.

The following diagram depicts the working of Caesar cipher algorithm implementation

![Caesar Cipher](https://www.tutorialspoint.com/cryptography_with_python/images/algorithm_caesar_cipher.jpg)

The program implementation of Caesar cipher algorithm is as follows
    
```python
# Python program to illustrate Caesar Cipher Technique
def encrypt(text,s):
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result

#check the above function
text = "CEASER CIPHER DEMO"
s = 4
print("Text  : " + text)
print("Shift : " + str(s))
print("Cipher: " + encrypt(text,s))
```

The output of the above program is as follows −

```python
Text  : CEASER CIPHER DEMO
Shift : 4
Cipher: GIEWIVrGMTLIVrHIQS
```

### Explanation
The plain text character is traversed one at a time.

    - For each character in the given plain text, transform the given character as per the rule depending on the procedure of encryption and decryption of text.

    - After the steps is followed, a new string is generated which is referred as cipher text.


### Decryption of Caesar Cipher
To decrypt the cipher text, we need to reverse the process of encryption. 

```python
# Python program to illustrate decrypting a Caesar Cipher

def decrypt(text,s):
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Decrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) - s - 65) % 26 + 65)
 
        # Decrypt lowercase characters
        else:
            result += chr((ord(char) - s - 97) % 26 + 97)
 
    return result

#check the above function
text = "GIEWIVrGMTLIVrHIQS"
s = 4
print("Cipher  : " + text)
print("Shift : " + str(s))
print("Text: " + decrypt(text,s))
```

The output of the above program is as follows −

```python
Cipher  : GIEWIVrGMTLIVrHIQS
Shift : 4
Text: CEASER CIPHER DEMO
```