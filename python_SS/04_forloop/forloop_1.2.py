#      >>>>>>>  Question number ..1..   :-     Accept an integer and Print hello world n times   <<<<<<<

# n = int(input("enter your input"))
# for i in range(1,n+1):
#     print("hello world")


#      >>>>>>>  Question number ..2..   :-    Print natural number up to n   <<<<<<<

# n = int(input("enter your input"))
# for i in range(0,n+1):
#     print(i)



#      >>>>>>>  Question number ..3..   :-   reverse for loop of a number n    <<<<<<<

# n = int(input("tell your input  :- "))
# for i in range(n,0,-1):
#     print(i)
    


#      >>>>>>>  Question number ..4..   :- take a number as input and prints its table      <<<<<<<


# n = int(input("tell your input  :- "))
# for i in range(1,11):
#     t = n*i
#     print(t)




#      >>>>>>>  Question number ..3..   :-   sum up upto n terms    <<<<<<<


# num = int(input("enter your input:- "))
# sum = 0
# for i in range(1,num+1):
#     sum = sum +i
#     print(sum)



#      >>>>>>>  Question number ..3..   :-   factorial of a number    <<<<<<<


# num = int(input("enter your input:- "))
# fact = 1
# for i in range(1,num+1):
#     fact = fact *i
#     print(fact)



#      >>>>>>>  Question number .. 3 ..   :-   print the sum if all odd and even numbers in a range seperatly     <<<<<<<

# num = int(input("enter your numbers :-  "))
# even = 0
# odd = 0

# for i in range (1,num):
#     if i%2 == 0:
#         even = even + i
#     else:
#         odd = odd+i
# print(f"your sum of number is :- {even},{odd}")



#      >>>>>>>  Question number ..3..   :-   print factor of a number    <<<<<<<





# num = int(input("enter your input:- "))
# for i in range(1,num+1):
#     if num%i == 0:
#         print(i)
   





#      >>>>>>>  Question number ..3..   :-  check number is perfect or not  <<<<<<<

# num = int(input("enter your input:- "))
# sum = 0
# for i in range(1,num):
# # for i in range(1,num):
#     if num%i == 0:
#          sum = sum + i

# print(sum)




#      >>>>>>>  Question number ..3..   :-  check number is perfect or not  <<<<<<<

num = int(input("enter your number"))
count = 0
for i in range(1,num+1):
    if num%i==0:   # yaha tk factor niklenge 
        count = count + 1
print(count)    
         

if count == 2:
    print(f"{num}  is a prime number")
else:
    print(f"{num}  is not prome number")



#      >>>>>>>  Question number ..3..   :-  reverse a string using inbuild   function  <<<<<<<

# s  = "satyam"
# b = ""
# for i in range(len(s)-1,-1,-1):
#     # b = b + s[i]
#     print(s[i])
# # print(b)






#      >>>>>>>  Question number ..3..   :-  check number is perfect or not  <<<<<<<


# s = input("enter your name or other")
# b = ""
# for i in range(len(s)-1,-1,-1):
#     b = b + s[i]
#     # print(s[i])
# print(b)

# if b == s:
#     print("your number is pallindrom")
# else:
#     print("your number is not pallindrom")