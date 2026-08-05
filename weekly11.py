# Handle division by zero exception. 

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

# Handle index out-of-range exception. 
try:
    numbers = [10, 20, 30, 40, 50]

    index = int(input("Enter index: "))
    print("Element:", numbers[index])

except IndexError:
    print("Error: Index is out of range.")
# Create and raise a custom exception. 
class AgeException(Exception):
    pass

try:
    age = int(input("Enter your age: "))

    if age < 18:
        raise AgeException("You are not eligible to vote.")

    print("You are eligible to vote.")

except AgeException as e:
    print("Custom Exception:", e)

# File handling program with proper exception handling. 
try:
    filename = input("Enter file name: ")

    file = open(filename, "r")
    data = file.read()

    print("File Content:")
    print(data)

    file.close()

except FileNotFoundError:
    print("Error: File does not exist.")

except PermissionError:
    print("Error: Permission denied.")

except Exception as e:
    print("An error occurred:", e)
    
# Banking system with exception handling. 
balance = 5000

try:
    amount = float(input("Enter withdrawal amount: "))

    if amount > balance:
        raise Exception("Insufficient Balance")

    balance -= amount

    print("Withdrawal Successful")
    print("Remaining Balance =", balance)

except Exception as e:
    print("Error:", e)

# Program handling multiple exceptions