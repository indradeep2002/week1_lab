# Explain merge sort algorithm.
# Implement merge sort.

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

arr = [38, 27, 43, 3, 9, 82, 10]

merge_sort(arr)

print("Sorted Array:", arr)

# Implement quick sort.

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return left + middle + right

arr = [38, 27, 43, 3, 9, 82, 10]

sorted_arr = quick_sort(arr)

print("Sorted Array:", sorted_arr)

# Compare merge sort and quick sort.
# Analyze worst-case of quick sort.


arr = [1, 2, 3, 4, 5, 6, 7]

print("Input Array:", arr)
print("Worst Case Time Complexity = O(n²)")

# Design hybrid sorting algorithm

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

def hybrid_sort(arr):
    if len(arr) <= 10:
        insertion_sort(arr)
    else:
        arr.sort()     

arr = [9, 4, 6, 2, 8, 1, 3]

hybrid_sort(arr)

print("Sorted Array:", arr)