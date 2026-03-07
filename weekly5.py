# ASSIGNMENT 1 -  Create a list and display its elements.


my_list = [10, 20, 30, 40, 50]

print("Elements of the list are:")
for item in my_list:
    print(item) 

#ASSIGNMENT 2 -  Find maximum and minimum element in a list.

numbers = [10,25,50,60,75,42,50,90]
maximum = max(numbers)
minimum = min(numbers)

print("List:", numbers)
print("Maximum element:", maximum)
print("Minimum element:", minimum)


#ASSIGNMENT 3 -  Count even and odd numbers in a list.

numbers = [10, 15, 22, 33, 40, 55]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("List:", numbers)
print("Number of even elements:", even_count)
print("Number of odd elements:", odd_count)

# ASSIGNMNET 4 -  Remove duplicate elements from a list.

numbers = [10, 20, 30, 20, 40, 10, 50 ,60]

unique_numbers = list(set(numbers))

print("Original List:", numbers)
print("List after removing duplicates:", unique_numbers)

# ASSIGNMENT 5 -  Find second largest element in a list.

n = int(input("Enter number of elements: "))

numbers = []

for i in range(n):
    num = int(input("Enter element: "))
    numbers.append(num)

numbers.sort()

second_largest = 

print("List:", numbers)
print("Second largest element:", second_largest)