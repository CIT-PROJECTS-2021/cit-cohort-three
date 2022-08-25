# Print out Letters from A to Z

# convert A to int
a = ord('A') # 65
# convert Z to int
z = ord('Z') # 90
# loop through A to Z
for i in range(a, z+1):
    # convert int to char
    print(chr(i), end=' ')


# password generator
chars = 'abcdefghijklmnopqrstuvwxyz'
nums = '0123456789'
special = '!@#$%^&*()_+'

size = int(input('Enter password size: '))

password = ''
selected = []
import random

for i in range(size):
    # randomly select from chars, nums, special
    r = random.randint(0, 3)
    # randomly select from chars, nums, special
    if r == 0:
        selected.append(chars)
    elif r == 1:
        selected.append(nums)
    else:
        selected.append(special)

    # randomly select from chars, nums, special
    r = random.randint(0, len(selected[i])-1)
    # randomly select from chars, nums, special
    password += selected[i][r]

print(password)