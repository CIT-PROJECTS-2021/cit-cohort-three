import hashlib, binascii
# import cryptography


"""
Hashing using sha3_256
"""
data = 'Hello World'
data = data.encode('utf-8')
print(data)
hash = hashlib.sha3_256(data).hexdigest()
print(hash)


"""
Hashing using sha256
"""
hash = hashlib.sha256(data).hexdigest()
print(hash)

"""
Hashing using sha1
"""
hash = hashlib.sha1(data).hexdigest()
print(hash)

"""
Hashing using md5
"""
hash = hashlib.md5(data).hexdigest()
print(hash)

# print(cryptography)


letters = {'a': 1, 'b': 2, 'c': 3}
print(letters['b'].__hash__())