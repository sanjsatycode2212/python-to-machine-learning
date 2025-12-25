user = int(input("enter your units: "))
if user <= 100:
    bill = user * 3
    print("your total bill is:", bill)
elif user <= 200:
    bill = user * 5
    print("your total bill is:", bill)
elif user <= 300:
    bill = user * 8
    print("your total bill is:", bill)
elif user > 300:
    bill = user * 10
    print("your total bill is:", bill)
else : 
    print("see again")