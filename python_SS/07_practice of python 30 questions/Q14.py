year = int(input("enter your input"))

if year%4==0 or year%100==0 or year%400==0:
    print("year is a leap year")
else:
    print("year is not leap year")