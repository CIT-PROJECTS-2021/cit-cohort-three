---
description: >-
    In this lesson, we will learn about the Quick Sort algorithm. We will also learn how to implement it in Python.
---

Quicksort is a sorting algorithm based on the divide and conquer approach where

1. An array is divided into subarrays by selecting a pivot element (element selected from the array).

While dividing the array, the pivot element should be positioned in such a way that elements less than pivot are kept on the left side and elements greater than pivot are on the right side of the pivot.

2. The left and right subarrays are also divided using the same approach. This process continues until each subarray contains a single element.

3. At this point, elements are already sorted. Finally, elements are combined to form a sorted array.

### Working of Quicksort Algorithm
**1. Select the Pivot Element**

There are different variations of quicksort where the pivot element is selected from different positions. Here, we will be selecting the rightmost element of the array as the pivot element.

![Select a pivot element](https://cdn.programiz.com/cdn/farfuture/7qpYqe1UtqYbKzIBY_W8ljqkUz9iS6jZGobim6LDhtM/mtime:1582112622/sites/tutorial2program/files/quick-sort-0.1_0.png)

**2. Rearrange the Array**

Now the elements of the array are rearranged so that elements that are smaller than the pivot are put on the left and the elements greater than the pivot are put on the right.

![Put all the smaller elements on the left and greater on the right of pivot element ](https://cdn.programiz.com/cdn/farfuture/1Xn_e4xeHQjOsXExVhTgVbggPgpMk9WV4Z8gxmZgdyg/mtime:1582112622/sites/tutorial2program/files/quick-sort-0.2_0.png)

Here's how we rearrange the array:

1. A pointer is fixed at the pivot element. The pivot element is compared with the elements beginning from the first index.

![Comparison of pivot element with element beginning from the first index](https://cdn.programiz.com/cdn/farfuture/zaN86RZ0WfV0PhWpWDhis-f9lWlfgKJt_liYoGjZAIk/mtime:1617189498/sites/tutorial2program/files/quick-sort-partition-first-step.png)

2. If the element is greater than the pivot element, a second pointer is set for that element.

![If the element is greater than the pivot element, a second pointer is set for that element.](https://cdn.programiz.com/cdn/farfuture/RzFeResnC88JRu9IFh2YqUKZMXltQ51EeiioINCMcEA/mtime:1617189487/sites/tutorial2program/files/quick-sort-partition-second-step.png)

3. Now, pivot is compared with other elements. If an element smaller than the pivot element is reached, the smaller element is swapped with the greater element found earlier.

![Pivot is compared with other elements](https://cdn.programiz.com/cdn/farfuture/QA-TsXFkcz3cNyJikcbIWxepFVDu8ntl220KzlG8zdw/mtime:1617189492/sites/tutorial2program/files/quick-sort-partition-third-step.png)

4. Again, the process is repeated to set the next greater element as the second pointer. And, swap it with another smaller element.

![The process is repeated to set the next greater element as the second pointer.](https://cdn.programiz.com/cdn/farfuture/tMmdAbX5gev9K20XI1kzQ3n932vSjnN1MszZouHV7Yc/mtime:1617189469/sites/tutorial2program/files/quick-sort-partition-fourth-step.png)

5. The process goes on until the second last element is reached.

![The process goes on until the second last element is reached](https://cdn.programiz.com/cdn/farfuture/MNYV977xf4N3cgCpAtkB1KDyPqyG9OvlKSkHSdd0kys/mtime:1617189475/sites/tutorial2program/files/quick-sort-partition-fifth-step.png)

6. Finally, the pivot element is swapped with the second pointer.

![Finally, the pivot element is swapped with the second pointer.
](https://cdn.programiz.com/cdn/farfuture/lAMcHRRzL8TJEh7bjY3rAufTTy3y5-o4Nt0z5L1AB8A/mtime:1617189481/sites/tutorial2program/files/quick-sort-partition-sixth-step.png)

3. Divide Subarrays

Pivot elements are again chosen for the left and the right sub-parts separately. And, step 2 is repeated.

![Select pivot element of in each half and put at correct place using recursion](https://cdn.programiz.com/cdn/farfuture/dK3pGyiHqFZOYklwABPBZ4zq_VZU1dMWBIbWhHJ-Rgw/mtime:1617189464/sites/tutorial2program/files/quick-sort_1.png)

The subarrays are divided until each subarray is formed of a single element. At this point, the array is already sorted.

### Quick Sort Algorithm

```python
quickSort(array, leftmostIndex, rightmostIndex)
  if (leftmostIndex < rightmostIndex)
    pivotIndex <- partition(array,leftmostIndex, rightmostIndex)
    quickSort(array, leftmostIndex, pivotIndex - 1)
    quickSort(array, pivotIndex, rightmostIndex)

partition(array, leftmostIndex, rightmostIndex)
  set rightmostIndex as pivotIndex
  storeIndex <- leftmostIndex - 1
  for i <- leftmostIndex + 1 to rightmostIndex
  if element[i] < pivotElement
    swap element[i] and element[storeIndex]
    storeIndex++
  swap pivotElement and element[storeIndex+1]
return storeIndex + 1
```

### Python Implementation

```python
# Quick sort in Python

# function to find the partition position
def partition(array, low, high):

  # choose the rightmost element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)


data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)
```


### References

1. [Quick Sort - GeeksforGeeks](https://www.geeksforgeeks.org/quick-sort/)
2. [Quick Sort - Tutorialspoint](https://www.tutorialspoint.com/data_structures_algorithms/quick_sort_algorithm.htm)
3. [Quick Sort - Programiz](https://www.programiz.com/dsa/quick-sort)
4. [Quick Sort - HackerEarth](https://www.hackerearth.com/practice/algorithms/sorting/quick-sort/tutorial/)
5. [Quick Sort - YouTube](https://www.youtube.com/watch?v=SLauY6PpjW4)