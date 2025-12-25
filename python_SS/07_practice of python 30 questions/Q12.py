    
hidden_num = 12
# user = int(input("enter your number :- "))
tries = 0

while True:
    user = int(input("enter your number :- "))
    if user == hidden_num:
        tries += 1
        print(f"you get number in tries {tries}:- ")
        break
    elif user > hidden_num:
        print(f"thoda sa niche jao :- ")
        tries += 1
    elif user < hidden_num:
        print(f"thoda sa uper jao :- ")
        tries += 1
    else :
        print("try again") 
        tries += 1