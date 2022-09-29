# bubble sort using a while loop

def bubble_sort(a):
    n = len(a)
    while n > 1:
        i = 1
        while i < n:
            if a[i-1] > a[i]:
                a[i-1], a[i] = a[i], a[i-1]
            i += 1
        n -= 1
    return a


# optimized bubble sort using a while loop by adding a swap flag
def bubble_sort_opt(a):
    n = len(a)
    while n > 1:
        i = 1
        swap = False
        while i < n:
            if a[i-1] > a[i]:
                a[i-1], a[i] = a[i], a[i-1]
                swap = True
            i += 1
        if not swap:
            break
        n -= 1
    return a

def bubble_sort_other(arr):
    i = 0
    while i < len(arr):
        j = 0
        while j < len(arr) - 1:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j += 1
        i += 1


# selection sort using a while loop
def selection_sort(a):
    n = len(a)
    while n > 1:
        i = 0
        max_index = 0
        while i < n:
            if a[i] > a[max_index]:
                max_index = i
            i += 1
        a[n-1], a[max_index] = a[max_index], a[n-1]
        n -= 1
    return a

# selection sort using a for loop and while loop
def selection_sort2(a):
    n = len(a)
    for i in range(n-1, 0, -1):
        max_index = 0
        j = 1
        while j <= i:
            if a[j] > a[max_index]:
                max_index = j
            j += 1
        a[i], a[max_index] = a[max_index], a[i]
    return a

if __name__ == '__main__':
    a = [5, 4, 3, 2, 1]
    print(bubble_sort(a))
    b = [5, 4, 3, 2, 1]
    print(bubble_sort_opt(b))


# Explanation
# The bubble sort algorithm is a simple sorting algorithm that repeatedly steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, which indicates that the list is sorted. The algorithm gets its name from the way smaller elements "bubble" to the top of the list. Because it only uses comparisons to operate on elements, it is a comparison sort. Although the algorithm is simple, most of the other sorting algorithms are more efficient for large lists.

# The bubble sort makes multiple passes through a list. It compares adjacent items and exchanges those that are out of order. Each pass through the list places the next largest value in its proper place. In essence, each item "bubbles" up to the location where it belongs.