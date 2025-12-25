num1  = int(input("num1 :- "))
num2  = int(input("num2 :- "))
num3  = int(input("num3 :- "))

if num1>num2 and num1>num3:
    print(f"gretest num1 is {num1}")
elif num2>num1 and num2>num3:
    print(f"gretest num2 is {num2}")
else:
    print(f"number is gretest number:- {num3}")
