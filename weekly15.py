# Implement linear search. 

arr = [10, 20, 30, 40, 50]
key = int(input("Enter the element to search: "))

found = False

for i in range(len(arr)):
    if arr[i] == key:
        print("Element found at index", i)
        found = True
        break

if not found:
    print("Element not found")
# Implement binary search.

arr = [10, 20, 30, 40, 50, 60, 70]
key = int(input("Enter the element to search: "))

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        print("Element found at index", mid)
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Element not found")
# Compare linear and binary search. 
# Linear Search

arr = [10, 20, 30, 40, 50]
key = int(input("Enter element to search: "))

found = False

for i in range(len(arr)):
    if arr[i] == key:
        print("Element found at index", i)
        found = True
        break

if not found:
    print("Element not found")
   
 # Binary Search

arr = [10, 20, 30, 40, 50]
key = int(input("Enter element to search: "))

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        print("Element found at index", mid)
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Element not found")
# Search in rotated sorted array.
# Search in Rotated Sorted Array

arr = [4, 5, 6, 7, 0, 1, 2]
target = int(input("Enter element to search: "))

low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == target:
        print("Element found at index", mid)
        break

    if arr[low] <= arr[mid]:
        if arr[low] <= target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    else:
        if arr[mid] < target <= arr[high]:
            low = mid + 1
        else:
            high = mid - 1
else:
    print("Element not found")
    
# Find first and last occurrence of an element.

arr = [1, 2, 2, 2, 3, 4, 5]
key = int(input("Enter element: "))

first = -1
last = -1

for i in range(len(arr)):
    if arr[i] == key:
        if first == -1:
            first = i
        last = i

print("First Occurrence:", first)
print("Last Occurrence:", last)

# Optimized search problem