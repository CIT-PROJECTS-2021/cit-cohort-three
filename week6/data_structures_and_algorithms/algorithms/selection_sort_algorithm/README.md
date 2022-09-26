---
description: >-
    In this lesson, we will learn about the selection sort algorithm. We will also learn how to implement it in Python.
---

Selection sort is a sorting algorithm that sorts an array by repeatedly finding the `minimum` element (considering ascending order) from unsorted part and putting it at the beginning. The algorithm maintains two subarrays in a given array.

1. The subarray which is already sorted.
2. Remaining subarray which is unsorted.

In every iteration of selection sort, the `minimum` element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray.

### Working of Selection Sort
1. Set the first element as `minimum`.

![Set the first element as `minimum`](https://cdn.programiz.com/cdn/farfuture/w1ZKsO2Obaw1WV03_lamX22SVyapwhbiKoLkT5Raiiw/mtime:1582112622/sites/tutorial2program/files/Selection-sort-0-initial-array.png)

2. Compare `minimum` with the second element. If the second element is smaller than `minimum`, assign the second element as `minimum`.

Compare `minimum` with the third element. Again, if the third element is smaller, then assign `minimum` to the third element otherwise do nothing. The process goes on until the last element.

![Compare minimum with the remaining of the elements](https://cdn.programiz.com/cdn/farfuture/9jjqXX0fGtJE2ul2Mga20fvf_GkNlFAFsDMwrrwFzbQ/mtime:1582112622/sites/tutorial2program/files/Selection-sort-0-comparision.png)

3. Swap the `minimum` element with the first element of the array.

![Swap the first with the minimum](https://cdn.programiz.com/cdn/farfuture/6o-qergdHNq6D7eBxBi87yIuCLc7MJy2BHR4QHeNxxQ/mtime:1582112622/sites/tutorial2program/files/Selection-sort-0-swapping.png)

4. For each iteration, indexing starts from the first unsorted element. Step 1 to 3 are repeated until all the elements are placed at their correct positions.

![First iteration](https://cdn.programiz.com/cdn/farfuture/VPGtdVYag2vfHBotOaFEiYLqvWAD_Jwfnwur_AtKQHo/mtime:1582112622/sites/tutorial2program/files/Selection-sort-0.png)

![second iteration](https://cdn.programiz.com/cdn/farfuture/hgxXpCSrHui7tbyJUQNnh8N5l8MPbdbL6dlstS4-G3M/mtime:1582112622/sites/tutorial2program/files/Selection-sort-1.png)

![Third iteration](https://cdn.programiz.com/cdn/farfuture/mDT4W_wUoS9eYT1JoUWjZuh4XBVXGDuiV9cr4Rylggk/mtime:1582112622/sites/tutorial2program/files/Selection-sort-2.png)

![Fourth iteration](https://cdn.programiz.com/cdn/farfuture/dsZIa58W_SRP0yB21QmrWGQvrmob8yAVa94iCtIPWoo/mtime:1582112622/sites/tutorial2program/files/Selection-sort-3_1.png)


### Selection Sort Algorithm

```python
selectionSort(array, size)
  repeat (size - 1) times
  set the first unsorted element as the minimum
  for each of the unsorted elements
    if element < currentMinimum
      set element as new minimum
  swap minimum with first unsorted position
end selectionSort
```

### Implementation in Python

```python
# Selection sort in Python


def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)
```