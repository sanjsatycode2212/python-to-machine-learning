## this is a powerfull statement that allows us to control the flow of our program.

## Syntax:

# if condition:
#     # code to be executed if condition is true



# syntax with else:

# if condition:
#     # code to be executed if condition is true
# else:
#     # code to be executed if condition is false




# syntax with elif:  >>>> in this elif condition we can check multiple conditions in one program.><

# if condition1:
#     # code to be executed if condition1 is true
# elif condition2:
#     # code to be executed if condition2 is true
# else:
#     # code to be executed if both conditions are false



## now we do some question based on conditional statements:>>>>>

##  1>>> ...   Accept two numbers and print the greatest between them.

# num1 = int(input("enter your num1:"))
# num2 = int(input("enter your num2:"))

# if num1 > num2:
#     print(f"{num1} is greatest")
# else:
#     print(f"{num2} is greatest")


 # output: enter your num1:45
 #         enter your num2:78
 #         78 is greatest



## 2>>>... Accept the gender from the user as char and print the respective greeting message 
##            Ex - Good Morning Sir (on the basis of gender).    


# gender = input("enter your gender (M/F):")

# if gender == 'M' or gender =='m':
#     print("Good Morning Sir")
# elif gender == 'F' or gender == 'f':
#     print("Good Morning Ma'am")
# else:
#     print("Good Morning")



# output: enter your gender (M/F):f
#         Good Morning Ma'am
# output: enter your gender (M/F):M
#         Good Morning Sir
# output: enter your gender (M/F):x
#         Good Morning  



# question 03.
## Accept an integer and check whether it is an even number or odd.

# num1 = int(input("enter your number:"))

# if num1 % 2 == 0:
#     print(f"{num1} is even number")
# else:
#     print(f"{num1} is odd number")  

# output: enter your number:45
#         45 is odd number
# output: enter your number:68
#         68 is even number
# output: enter your number:0
#         0 is even number

# question 04.
##   accept name and age from the user. Check if the user is a valid voter or not.
##      ex:- “hello satyam you are a valid voter”

# name  = input("enter your name :- ")
# age = int(input("enter your age :- "))

# if age >= 18:
#     print(f" hey {name} you are a valid voter")
# else:
#     print(f" hey {name} you are not a valid voter")

# output: enter your name :- satyam
#         enter your age :- 20
#         hey satyam you are a valid voter
# output: enter your name :- ankit
#         enter your age :- 16
#         hey ankit you are not a valid voter

year = int(input("enter the year :- "))

if year%4==0 or year%400==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

