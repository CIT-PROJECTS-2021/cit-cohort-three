# Implementation of the merge sort algorithm

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def merge_sort_simpler(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort_simpler(left)
        merge_sort_simpler(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        arr[k:] = left[i:] or right[j:]

    return arr


# merge sort shorter version
def merge_sort_shorter(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort_shorter(left)
        merge_sort_shorter(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            arr[k] = (left[i] if left[i] < right[j] else right[j])
            i += (left[i] < right[j])
            j += (left[i] >= right[j])
            k += 1

        arr[k:] = left[i:] or right[j:]

    return arr

if __name__ == "__main__":
    arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    merge_sort(arr)
    print(arr)

    