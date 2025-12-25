a = int(input("enter you number :- "))
b = int(input("enter you number :- "))

for i in range(2, min(a,b)+1):
    if a%i==0 and b%i==0:
       
        print("gcd",i)
