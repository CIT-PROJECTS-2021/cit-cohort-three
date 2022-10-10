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

print(text[::-1])