import statistics
import numpy as np
import pandas as pd

davids_marks = np.array([
    [78, 67, 90],
    [34, 55, 23],
    [12, 89, 45]
])

# Mode
mode = statistics.mode(davids_marks.flatten())

print(davids_marks.flatten())

# Median
median = np.median(davids_marks)

# Mean
mean = np.mean(davids_marks)

print(f"Mode: {mode}, Median: {median}, Mean: {mean}")

# create a numpy array using ndim
two_dim = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], ndmin=3)
print(two_dim.ndim)


davids_marks = np.array([
    [78, 67, 90], # 0 1st row
    [34, 55, 23], # 1 2nd row
    [12, 89, 45] # 2 3rd row
])

# Row X Column
print(davids_marks[0][2])
print(davids_marks[2][1])

diagonal = [davids_marks[0][0], davids_marks[1][1], davids_marks[2][2]]
print(diagonal)


my_arr = np.array([[i for i in range(4)] for _ in range(4)])
print(my_arr.ndim)


# Array slicing
print(davids_marks[0, 2])
print(davids_marks[:1, :2])
print(davids_marks[2, 1])

# NumPy Data types
"""
1. i - integer
2. b - boolean
3. u - unsigned integer
"""

# check data type
print(davids_marks.dtype)


fruits = np.array(['apple', 'banana', 'cherry'])

print(fruits.dtype)


# Copy vs View
mary_marks = davids_marks.copy()

print(mary_marks)

print(mary_marks.view())

print(mary_marks.base)

# Numpy Array Shape
# This refers to the number of elements in each dimension.
print(davids_marks.shape)

arr = np.array([1, 2, 3, 4, 5])
print(arr.shape)

# Reshaping Arrays
arr = np.array([i+1 for i in range(12)])
print(arr)
# [ 1  2  3  4  5  6  7  8  9 10 11 12]
# [[1, 2, 3],[4, 5, 6],[7, 8, 9],[10, 11, 12]]
# [[1, 2, 3, 4, 5, 6],[7, 8, 9, 10, 11, 12]]
arr = arr.reshape(4, 3)
print(arr)
arr = arr.reshape(2, 6)
print(arr)
# two arrays -> three arrays -> elements
# [[[1, 2], [3, 4], [5, 6]],[[7, 8], [9, 10], [11, 12]]]
arr = arr.reshape(2, 3, 2)
print(arr)

arr = np.array([[[1], [2], [3], [4]],[[5], [6], [7], [8]],[[9], [10], [11], [12]]])
print(arr.ndim)