## reverse a number using while loop
A = int(input("enter your number"))
rev = 0
while A > 0:
    rev = rev * 10 + A % 10
   #rev = 0 * 10 + 457 % 10 = 7 is remainder
   # rev = 7 * 10 + 45 % 10 = 70 + 5 = 75
   # rev = 75 * 10 + 4 % 10 = 750 + 4 = 754
    A = A // 10
print("reversed number is", rev)
