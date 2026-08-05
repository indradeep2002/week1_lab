# Define data structure with example.

numbers = [10, 20, 30, 40, 50]

print("Data Structure (List):", numbers)
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])

# Find time complexity of a simple loop. 
n = int(input("Enter a number: "))

for i in range(n):
    print(i) 
    #The loop executes n times.
    #Therefore, the time complexity is O(n).

# Compare time complexity of two algorithms. 
# Algorithm 1 - O(n)

n = 5

print("Algorithm 1 (O(n))")
for i in range(n):
    print(i)

# Algorithm 2 - O(n²)

print("\nAlgorithm 2 (O(n²))")
for i in range(n):
    for j in range(n):
        print(i, j)

# Program demonstrating O(n) vs O(n²). 
n = int(input("Enter value of n: "))

print("O(n) Example:")
for i in range(n):
    print(i)

print("\nO(n²) Example:")
for i in range(n):
    for j in range(n):
        print(i, j)

# Optimize a given inefficient algorithm.

# Case study on algorithm efficiency.