# n = int(input("Enter a number: "))
n = 6
sum = 0
for i in range(1, n):
    if n%i==0:
        # sum = sum +1
        sum = sum +i
if sum ==n:
    print("your number is perfect")
else:
    print("your number is not perfect") 
# print(sum)