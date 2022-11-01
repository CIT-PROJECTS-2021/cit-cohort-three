import numpy as np
import statistics
# scipy.stats is a library of statistical functions

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a + b

print(c)

# Create a numpy array of 10 zeros. and reshape it to (2, 5)
arr = np.zeros(10).reshape(2, 5)
# arr = np.array([0 for i in range(10)]).reshape(2, 5)
print(arr.shape)

# Find Mean, Mode, Median, Standard Deviation of the following data
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

mean = np.mean(data)

mode = statistics.mode(data)

median = np.median(data)

std = np.std(data)

print(f"Mean: {mean}, Mode: {mode}, Median: {median}, Standard Deviation: {std}")

# create a 6x6 numpy array with random values and find the min and max values
arr = np.random.randint(0, 100, 36).reshape(6, 6)
print(arr)

# create a 3D numpy array and reshape it to 2D

arr = np.array([i for i in range(27)]).reshape(3, 3, 3)
#  arr = np.arange(27).reshape(3, 3, 3)
#  arr = np.array([i for i in range(27)], ndmin=3)


# create 1D array from this data
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data = np.array(data)
data = data.flatten()
print(data.shape)


arr = np.random.randint(0, 100, 36).reshape(6, 6)

print(statistics.mode(arr.flatten()))