def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr


print(insertion_sort([1, 4, 2, -44, -12, 56, 23]))


def insertion_sort_optimized(arr):
    for i in range(1, len(arr)):
        while i > 0 and arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1

    return arr


print(insertion_sort_optimized([1, 4, 2, -44, -12, 56, 23]))