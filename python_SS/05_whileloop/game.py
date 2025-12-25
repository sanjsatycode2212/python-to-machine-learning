user = int(input("Enter a number :- "))
num = 9

while user > 0:
    if user < num:
        print("Your number is smaller than the correct number, please try again")
    elif user > num:
        print("Your number is greater than the correct number, please try again")
    elif user == num:                             
        print("You have entered the correct number")
    break
user = int(input("Enter a number :- "))


# num = 9

# user = int(input("Enter a number :- "))

# while user > 0:

#     if user < num:
#         print("Your number is smaller than the correct number, please try again")
    
#     elif user > num:
#         print("Your number is greater than the correct number, please try again")

#     else:       
#         print("You have entered the correct number")
#         break

#     user = int(input("Enter a number :- "))
