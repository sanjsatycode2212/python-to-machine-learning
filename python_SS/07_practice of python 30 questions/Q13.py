num = int(input("enter your num :- "))
count = 0
for i in range(1,100):
    if num % i == 0:
        count = count + 1
print(count)

# if count == 2:
#     print(f"{num} :- number is a prime number ")
# else:
#     print(f"{num}:-  is not prime number")
