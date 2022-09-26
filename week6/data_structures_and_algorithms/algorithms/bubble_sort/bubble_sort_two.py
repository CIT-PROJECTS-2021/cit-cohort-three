# Bubble sort in Python

def bubbleSort(array):
  print('Initial length: {}'.format(len(array)))

  # [-2, 45, 0, 11, -9]
  # -2

  # [45, 0, 11, -9]
  # 45
    
  # loop to access each array element
  for i in range(len(array)):

    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
       # [-2, 45, 0, 11, -9]
        # -2, 45
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        # -2
        temp = array[j]
        # -9
        array[j] = array[j+1]
        # -2
        array[j+1] = temp


data = [-2, 45, 0, 11, -9]

# bubbleSort(data)

# print('Sorted Array in Ascending Order:')
# print(data)



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


print(optimized_bubble_sort(data))

import timeit

exec_time = timeit.timeit("optimized_bubble_sort([-2, 45, 0, 11, -9])", setup="from __main__ import optimized_bubble_sort", number=1000000)
print(exec_time)
