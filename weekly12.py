# Use lambda function to find square of a number.
num = int(input("Enter a number: "))

square = lambda x: x * x

print("Square =", square(num))

# Use map and filter together in a program. 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

squares = list(map(lambda x: x ** 2, even_numbers))

print("Original List:", numbers)
print("Even Numbers:", even_numbers)
print("Squares of Even Numbers:", squares)

# Use reduce to calculate product of elements. 
from functools import reduce

numbers = [2, 3, 4, 5]

product = reduce(lambda x, y: x * y, numbers)

print("List:", numbers)
print("Product =", product)

# Perform array operations using NumPy. 
import numpy as np

arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([1, 2, 3, 4])

print("Array 1:", arr1)
print("Array 2:", arr2)

print("Addition:", arr1 + arr2)
print("Subtraction:", arr1 - arr2)
print("Multiplication:", arr1 * arr2)
print("Division:", arr1 / arr2)

# Data analysis using Pandas DataFrame. 
import pandas as pd

data = {
    "Name": ["Amit", "Riya", "Rahul", "Sneha"],
    "Marks": [85, 90, 78, 88]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\nAverage Marks:", df["Marks"].mean())
print("Maximum Marks:", df["Marks"].max())
print("Minimum Marks:", df["Marks"].min())

# Mini data-processing script using libraries
import pandas as pd
import numpy as np

# Create sample data
data = {
    "Student": ["A", "B", "C", "D"],
    "Marks": [80, 65, 90, 75]
}

df = pd.DataFrame(data)

# Add 5 bonus marks using NumPy
df["Final Marks"] = np.array(df["Marks"]) + 5

# Select students with marks greater than or equal to 80
result = df[df["Final Marks"] >= 80]

print("Original Data:")
print(df)

print("\nStudents Scoring 80 or More:")
print(result)

print("\nAverage Final Marks:", df["Final Marks"].mean())