# Implementation of quick sort algorithm

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


# Alternative implementation of quick sort algorithm
def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort2(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort2(arr, low, pi - 1)
        quick_sort2(arr, pi + 1, high)

if __name__ == "__main__":
    arr = [5, 2, 1, 8, 4, 7, 6, 3]
    print(quick_sort(arr))
    quick_sort2(arr, 0, len(arr) - 1)
    print(arr)
    