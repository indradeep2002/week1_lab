# Traverse and print elements of an array.

arr = [10, 20, 30, 40, 50]

print("Array elements are:")

for element in arr:
    print(element)

# Insert an element at a specific position.

arr = [10, 20, 30, 40, 50]

print("Original List:", arr)

position = int(input("Enter the position (0-based index): "))
element = int(input("Enter the element to insert: "))

arr.insert(position, element)

print("Updated List:", arr)

# Delete an element from an array. 


arr = [10, 20, 30, 40, 50]

print("Original List:", arr)

element = int(input("Enter the element to delete: "))

if element in arr:
    arr.remove(element)
    print("Updated List:", arr)
else:
    print("Element not found!")

# Find missing number in an array.

# Find longest substring without repeating characters.
# Find Longest Substring Without Repeating Characters

s = input("Enter a string: ")

longest = ""
current = ""

for ch in s:
    if ch not in current:
        current += ch
    else:
        while ch in current:
            current = current[1:]
        current += ch

    if len(current) > len(longest):
        longest = current

print("Longest Substring:", longest)
print("Length:", len(longest))

# Rotate array by k steps

# Rotate Array by k Steps

arr = [1, 2, 3, 4, 5, 6, 7]

k = int(input("Enter number of rotations: "))

k = k % len(arr)

rotated = arr[-k:] + arr[:-k]

print("Rotated Array:", rotated)



















