# Numpy Array Quiz

## Question 1

What is the result of the following code?

```python
    import numpy as np
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    c = a + b
    print(c)
```

c = ([5, 7, 9])

## Question 2

Create a numpy array of 10 zeros. and reshape it to (2, 5)

import numpy as np
array=np.zeros(10)
print("An array of 10 zeros:")
print(array)


## Question 3

Find Mean, Mode, Median, Standard Deviation of the following data

```python
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
```


# Python program to print
# mean of elements
  
# list of elements to calculate mean
n_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n = len(n_num)
  
get_sum = sum(n_num)
mean = get_sum / n
  
print("Mean / Average is: " + str(mean))

# Python program to print
# median of elements
  
# list of elements to calculate median
n_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n = len(n_num)
n_num.sort()
  
if n % 2 == 0:
    median1 = n_num[n//2]
    median2 = n_num[n//2 - 1]
    median = (median1 + median2)/2
else:
    median = n_num[n//2]
print("Median is: " + str(median))

# Python program to print
# mode of elements
from collections import Counter
  
# list of elements to calculate mode
n_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
n = len(n_num)
  
data = Counter(n_num)
get_mode = dict(data)
mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]
  
if len(mode) == n:
    get_mode = "No mode found"
else:
    get_mode = "Mode is / are: " + ', '.join(map(str, mode))
      
print(get_mode)

## Question 4

create a 6x6 numpy array with random values and find the min and max values

import numpy as np
x = np.random.random((6,6))
print("Original Array:")
print(x) 
xmin, xmax = x.min(), x.max()
print("Minimum and Maximum Values:")
print(xmin, xmax)



## Question 5

create a 3D numpy array and reshape it to 2D

import numpy as np
array=np.array( [[[ 5,  4],
      [ 6,  9]],
 
      [[ 1,  0],
      [ 9,  5]],
 
      [[ 4,  9],
      [13, 19]],
                  
      [[ 8, 10],
      [ 1, 5]]])
reshaped_array=np.reshape(array,(4,4))
print("Original array:\n", array)
print("Reshaped array:\n", reshaped_array)

## Question 6

create 1D array from this data

```python
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
import numpy as np

#create numpy array
a = np.array([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(a)
