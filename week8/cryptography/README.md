---
description: >-
    This week we will be learning about cryptography, a method of protecting information by encoding it. We will be learning about the different types of ciphers, and how to implement them in Python.
---

Modern cryptography is the one used widely among computer science projects to secure the data messages. This lecture covers the basic concepts of cryptography and its implementation in Python scripting language. After completing this lecture, you will be able to relate the basic techniques of cryptography in real world scenarios.

**Cryptography** is the art of communication between two users via coded messages. The science of cryptography emerged with the basic motive of providing security to the confidential messages transferred from one party to another.

**Cryptography** is defined as the art and science of concealing the message to introduce privacy and secrecy as recognized in information security.

### **Terminologies of Cryptography**
The frequently used terms in cryptography are explained here −

### **Plain Text**
The plain text message is the text which is readable and can be understood by all users. The plain text is the message which undergoes cryptography.

### **Cipher Text**
Cipher text is the message obtained after applying cryptography on plain text.

### **Encryption**
The process of converting plain text to cipher text is called encryption. It is also called as encoding.

### **Decryption**
The process of converting cipher text to plain text is called decryption. It is also termed as decoding.

The diagram given below shows an illustration of the complete process of cryptography −

![Cryptography (Encryption and Decryption)](https://www.tutorialspoint.com/cryptography_with_python/images/encryption.jpg)

### Characteristics of Modern Cryptography
The basic characteristics of modern cryptography are as follows −

    - It operates on bit sequences.

    - It uses mathematical algorithms for securing the information.

    - It requires parties interested in secure communication channel to achieve privacy.


### **Types of Cryptography**
The cryptography can be broadly classified into two types −

### **Symmetric Cryptography**
In symmetric cryptography, the same key is used for both encryption and decryption. The key is shared between the sender and receiver. The sender encrypts the message using the key and sends it to the receiver. The receiver decrypts the message using the same key. The sender and receiver must have the same key to decrypt the message.

Examples of symmetric cryptography are:
    
        - DES (Data Encryption Standard)
    
        - AES (Advanced Encryption Standard)
    
        - Blowfish
    
        - RC4
    
        - RC5
    
        - IDEA
    
        - Triple DES
    
        - Twofish

![Symmetric Cryptography](https://www.encryptionconsulting.com/wp-content/uploads/2022/08/3.jpg)

### **Asymmetric Cryptography**

In asymmetric cryptography, two different keys are used for encryption and decryption. One key is used for encryption and the other key is used for decryption. The sender encrypts the message using the public key and sends it to the receiver. The receiver decrypts the message using the private key. The sender and receiver must have the same key to decrypt the message.

Examples of asymmetric cryptography are:
    
        - RSA (Rivest–Shamir–Adleman)
    
        - Diffie–Hellman key exchange
    
        - ElGamal encryption
    
        - DSA (Digital Signature Algorithm)
    
        - ECC (Elliptic Curve Cryptography)


![Asymmetric Cryptography](https://www.encryptionconsulting.com/wp-content/uploads/2022/08/4.jpg)


### Hash Functions
Hash functions are used to generate a fixed length of output from a variable length of input. The hash function is a one-way function. It is not possible to reverse the hash function. The hash function is used to generate a unique hash value for a given input. 

The hash value is used to verify the integrity of the data. The hash function is used to generate a unique hash value for a given input. The hash value is used to verify the integrity of the data.

Examples of hashing algorithms:
    - MD5 (Message Digest 5)
    - SHA (Secure Hash Algorithm)
    - SHA-1 (Secure Hash Algorithm 1)
    - SHA-2 Family which includes SHA-224, SHA-256, SHA-384, SHA-512
    - SHA-3
    - Whirlpool
    - etc

### Python Libraries for Cryptography
- cryptography
- pycrypto
- pycryptodome
- pyaes
- pydes
- pycryptopp
- hashlib
- etc
