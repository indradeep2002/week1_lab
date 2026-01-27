# question 1 - Check whether a number is positive or negative
num = float(input("Enter your number :- "))
if num>0 :
    print("your number is positive ")
else :
    print ("your number i negative ")

# question 2-  Check if a number is even or odd

num = float(input("Enter Your Number :- "))
if num%2 == 0 :
    print("Your number is even ")
else :
    print("Your number is odd")

# question 3  Find the greatest of three numbers

num1 = float(input("Enter your first number :- "))
num2 = float(input("Enter your second number :- "))
num3 = float(input("Enter your third number :- "))
if num1>num2 and num1>num3 :
    print("Your first number is biggest ")
elif num2>num1 and num2>num3 :
    print("Your second number is biggest ")
else : 
    print("Your third number is biggest") 

#question 4  Calculate electricity bill using conditional slabs

unit = int(input("Enter your bill unit :- "))
print("Your electrick bill is :- ", unit*25)

#question 5  Check whether a year is a leap year

year = int(input("Enter a year :-"))
if year%4 == 0 :
    print("the year is leap year")
else :
    print("the year is not leap year ")

#question 6  Build a grading system using marks

user_num = int(input("Enter your total marks :- "))
if user_num>=600 and user_num<=700 :
    print("your gared is A+ ")
elif user_num>=500 and user_num<=599 :
    print("your gared is A ")
elif user_num>=400 and user_num<=499 :
    print("your gared is B+ ")
elif user_num>=300 and user_num<=399 :
    print("your gared is B ")
elif user_num>=200 and user_num<=299 :
    print("your gared is C ")
else :
    print("You are fail , next time better luck!")

