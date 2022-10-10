---
description: >-
    In this section we shall provide a few examples about calculating cryptographic hash functions in Python. We shall use the `hashlib` module from the Python standard library.
---

# Cryptographic Hash Functions - Examples
We shall use the standard Python library hashlib. The input data for hashing should be given as bytes sequence (bytes object), so we need to encode the input string using some text encoding, e.g. utf8. The produced output data is also a bytes sequence, which can be printed as hex digits using binascii.hexlify() as shown below:

```python
import hashlib, binascii

text = 'hello'
data = text.encode("utf8")

sha256hash = hashlib.sha256(data).digest()
print("SHA-256:   ", binascii.hexlify(sha256hash))

sha3_256 = hashlib.sha3_256(data).digest()
print("SHA3-256:  ", binascii.hexlify(sha3_256))

blake2s = hashlib.new('blake2s', data).digest()
print("BLAKE2s:   ", binascii.hexlify(blake2s))

ripemd160 = hashlib.new('ripemd160', data).digest()
print("RIPEMD-160:", binascii.hexlify(ripemd160))
```

The output of the above program is:

```sh
SHA-256:    b'2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
SHA3-256:   b'3338be694f50c5f338814986cdf0686453a888b84f424d792af4b9202398f392'
BLAKE2s:    b'19213bacc58dee6dbde3ceb9a47cbb330b3d86f8cca8997eb00be456f140ca25'
RIPEMD-160: b'108f07b8382412612c048d07d13f814118445acd'
```



