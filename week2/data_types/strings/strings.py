# Print out Letters from A to Z

# convert A to int
a = ord('A') # 65
# convert Z to int
z = ord('Z') # 90
# loop through A to Z
for i in range(a, z+1):
    # convert int to char
    print(chr(i), end=' ')