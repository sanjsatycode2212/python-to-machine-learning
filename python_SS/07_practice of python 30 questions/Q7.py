# print factorial of a number ans sum of that factorial.

num = int(input("enter your num :- "))
fact = 1
for i in range(1,num+1):
    fact = fact * i
    # print(fact)
print(fact)