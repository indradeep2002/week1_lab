# assignment 1 (write a program to print your name and age )
print ("name:- Rupsa Mondal")
print ("Age :- 20")
user_name = input("Enter your name :-")
print (user_name)
user_age = int(input("Enter your age :-"))
print (user_age)


# assignment 2 ( Take two numbers as input and print their sum, difference, product, and quotient.)

num_1 = int(input("Enter your first number :- "))
num_2 = int(input("Enter your second  number :- "))
print("Their sum is  ",num_1+num_2)
rint("Their difference  is  ",num_1-num_2)
print("Their product is  ",num_1*num_2)
print("Their quotient is  ",num_1/num_2)

# assignment 3 (Convert temperature from Celsius to Fahrenheit)

cel_tem = int(input("Enter the temperature in celsius :-"))
print ("Your fahrenhaeit temperatuer is  ",(cel_tem*9/5)+32)

# assignment 4 (Create a simple calculator using user input)
print("Simple Calculator")
print("-----------------")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print("Result =", num1 + num2)

elif choice == 2:
    print("Result =", num1 - num2)

elif choice == 3:
    print("Result =", num1 * num2)

elif choice == 4:
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Error! Division by zero")

else:
    print("Invalid choice")

 # assignment 6 ( Print a formatted bio using input values.)
 user_name = input("Enter your name:- ")
 user_age = int(input("Enter your age :- "))
 user_qualification = input("Enter your qualificaton :- ")
 user_softskill = input("Enter your softskill :- ")
 user_address = input("Enter your address :- ")
 user_fathername  = input("Enter your father's name :- ")
 user_mothername  = input("Enter your mother's name :- ")
print(user_name)
print(user_age)
print(user_qualification)
print(user_softskill)
print(user_address)
print(user_fathername)
print(user_mothername)

