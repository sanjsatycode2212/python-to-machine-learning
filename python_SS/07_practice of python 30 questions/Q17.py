a = int(input("enter you number :- "))
b = int(input("enter you number :- "))

for i in range(2, min(a,b)+1):
    c = a*b
    if a%i==0 and b%i==0:
        print("gcd",i)
        print("your LCM" ,c//i)
