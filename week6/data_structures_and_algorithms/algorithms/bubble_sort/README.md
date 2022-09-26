---
description: >-
    In this lesson, we will learn about the bubble sort algorithm. We will also learn how to implement it in Python.
---

Bubble sort is an algorithm that compares adjacent elements in a list and swaps them if they are out of order. It continues to do this until the list is sorted. The algorithm is named bubble sort because the largest element in the list *"bubbles"* to the top of the list.

Just like the movement of air bubbles in water that rise to the top, the largest element in the list will bubble to the top. The algorithm will then ignore the largest element and repeat the process until the list is sorted.

### Working of the Bubble Sort Algorithm

Suppose we are trying to sort the following list of numbers in ascending order:

```python
[5, 1, 4, 2, 8]
```

1. **First Iteration (Compare and Swap)**

    1. Starting from the first index, compare the first and the second elements.
    2. If the first element is greater than the second element, swap them.
    3. Now, compare the second and the third elements. Swap them if they are not in order.
    4. The above process goes on until the last element


![Compare the Adjacent Elements](https://cdn.programiz.com/cdn/farfuture/kn1zM7ZGIj60jcTe3mv8gAtbrvFHqxgqfQ7F9MdjPuA/mtime:1582112622/sites/tutorial2program/files/Bubble-sort-0.png)

2. **Remaining Iteration**

The same process goes on for the remaining iterations.

After each iteration, the largest element among the unsorted elements is placed at the end.


![Put the largest element at the end](https://cdn.programiz.com/cdn/farfuture/LzbPYkOXS-DjqwLqtIrixMZCD1XLdU-JWWedrL1YIpw/mtime:1582112622/sites/tutorial2program/files/Bubble-sort-1.png)

In each iteration, the comparison takes place up to the last unsorted element.

![Compare the adjacent elements](https://cdn.programiz.com/cdn/farfuture/-C5A9EpPrCAwR2TFQlZhG0uy5aSKmq-ewMaWyXp8_a8/mtime:1582112622/sites/tutorial2program/files/Bubble-sort-2.png)

The array is sorted when all the unsorted elements are placed at their correct positions.


![The array is sorted if all elements are kept in the right order](https://cdn.programiz.com/cdn/farfuture/NnXQeMGuMJnIH0qzC1C5n7r4FOynP9vu3cWEdCK5Qjk/mtime:1582112622/sites/tutorial2program/files/Bubble-sort-3.png)

### Bubble Sort Algorithm

```python
bubbleSort(array)
  for i <- 1 to indexOfLastUnsortedElement-1
    if leftElement > rightElement
      swap leftElement and rightElement
end bubbleSort
```

### Bubble Sort Code in Python

```python
# Bubble sort in Python

def bubbleSort(array):
    
  # loop to access each array element
  for i in range(len(array)):

    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp


data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)
```


### Optimized Bubble Sort Algorithm
In the above algorithm, all the comparisons are made even if the array is already sorted. This increases the execution time.

To solve this, we can introduce an extra variable `swapped`. The value of `swapped` is set `true` if there occurs swapping of elements. Otherwise, it is set `false`.

After an iteration, if there is no swapping, the value of `swapped` will be `false`. This means elements are already sorted and there is no need to perform further iterations.

This will reduce the execution time and helps to optimize the bubble sort.

**Algorithm for optimized bubble sort is**

```python
bubbleSort(array)
  swapped <- false
  for i <- 1 to indexOfLastUnsortedElement-1
    if leftElement > rightElement
      swap leftElement and rightElement
      swapped <- true
end bubbleSort
```

### Optimized Bubble Sort in Python

```python
# Optimized Bubble sort in Python

def bubbleSort(array):
    
  # loop through each element of array
  for i in range(len(array)):
        
    # keep track of swapping
    swapped = False
    
    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping occurs if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp

        swapped = True
          
    # no swapping means the array is already sorted
    # so no need for further comparison
    if not swapped:
      break

data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)
```

