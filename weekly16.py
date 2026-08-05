# Implement bubble sort.

arr = [64, 34, 25, 12, 22, 11, 90]

n = len(arr)

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Sorted Array:")
print(arr)
# Implement selection sort. 

arr = [64, 25, 12, 22, 11]

n = len(arr)

for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]

print("Sorted Array:")
print(arr)
# Implement insertion sort. 
arr = [12, 11, 13, 5, 6]

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

print("Sorted Array:")
print(arr)
# Compare performance of sorting algorithms. 
import time

# Bubble Sort
def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

# Built-in Sort
def builtin_sort(arr):
    return sorted(arr)

numbers = [64, 34, 25, 12, 22, 11, 90]

start = time.time()
bubble_sort(numbers)
end = time.time()
print("Bubble Sort Time:", end - start)

start = time.time()
builtin_sort(numbers)
end = time.time()
print("Built-in Sort Time:", end - start)

# Demonstrate stable vs unstable sorting. 
students = [
    ("Rahul", 80),
    ("Amit", 90),
    ("Riya", 80),
    ("Sneha", 90)
]

sorted_students = sorted(students, key=lambda x: x[1])

print("Stable Sort:")
for student in sorted_students:
    print(student)
# Sorting visualization logic