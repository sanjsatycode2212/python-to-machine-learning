## input  >>>  means to give input by a us directly  and   2.>> take input by the user . 
## input =>> input is a inbuild function in python programming language which is use to take input from user.
## input() function always take input as a string data type.

## ex:->>>

# taking input from user
name = input("Enter your name: ")  ## here name is variable name and input() function is used to take input from user.
print("Hello, " + name + "!")  ## here name is variable name and input() function is used to take input from user.  
print(type(name))  ## type() is used to check the data type of variable.


# taking input from user
age = input("Enter your age: ")  ## here age is variable name and input() function is used to take input from user.
print("You are " + age + " years old.")  ## here age is variable name and input() function is used to take input from user.
print(type(age))  ## type() is used to check the data type of variable.



### >>>>>>>>>>>>>>>>>>>>  here print is give output to the user.  means for see out we call print() function  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


# note:--

# >>>>>>   input() function always take input as a string data type. <<<<<
# >>>>>>   to take input as a integer or float data type we have to use int() or float() function. <<<<<
# >>>>>>   we can use input() function to take input from user in python programming language. <<<<<
# >>>>>>   we can use type() function to check the data type of variable in python programming language. <<<<<
# >>>>>>   we can concatenate string with + operator in python programming language. <<<<<
# >>>>>>   we can use f-string to format string in python programming language. <<<<<
# >>>>>>   we can use , to concatenate string with other data types in python programming language


print("Hello,", name + "!")  ## using , to concatenate string with other data types
print(f"Hello, {name}!")  ## using f-string to format string
print("You are", age, "years old.")  ## using , to concatenate string with other data types
print(f"You are {age} years old.")  ## using f-string to format string

# taking integer input from user
age = int(input("Enter your age: "))  ## here age is variable name and input() function is used to take input from user.
print(age)  ## here age is variable name and input() function is used to take input from user.
print(type(age))  ## type() is used to check the data type of variable.