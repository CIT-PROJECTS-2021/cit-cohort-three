import numpy as np

# Resize vs Reshape
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

new_arr = np.resize(arr, (3, 3))
print(new_arr)

# reshape
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

arr = arr.reshape(3, 3)
print(arr)


# Iterating Arrays
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# for item in arr:
#     print(item)

arr = np.array([[1, 2, 3], [4, 5, 6]])

for item in arr:
   for inner_item in item:
       print(inner_item)

# nditer()
for item in np.nditer(arr):
   print(item)


# ndenumerate()

arr = np.array([1, 2, 3])

for index, item in np.ndenumerate(arr):
   print(index[0], item)

# Joining Arrays
arr = np.array([[1, 2, 3], [8, 9, 10]])
arr1 = np.array([4, 5, 6, 7])

result = np.concatenate((arr.flatten(), arr1))
print(result)