def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Explanation:
# 1. The outer loop runs from 0 to the length of the array.
# 2. The inner loop runs from 0 to the length of the array minus the outer loop index minus 1.
# This is because the inner loop is comparing the current index with the next index.
# 3. If the current index is greater than the next index, then the two values are swapped.
# 4. The inner loop runs until the end of the array.

def optimized_bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Explanation:
# 1. The outer loop runs from 0 to the length of the array.
# 2. A swapped variable is initialized to False.
# 3. The inner loop runs from 0 to the length of the array minus the outer loop index minus 1.
# This is because the inner loop is comparing the current index with the next index.
# 4. If the current index is greater than the next index, then the two values are swapped.
# 5. The swapped variable is set to True.
# 6. If the swapped variable is False, then the array is sorted and the loop is broken.
# 7. The inner loop runs until the end of the array.


# Bubble Sort optimized with time
import timeit

# Bubble Sort
print(timeit.timeit("bubble_sort([1, 2, 3, 4, 5])", setup="from __main__ import bubble_sort", number=1000000))

