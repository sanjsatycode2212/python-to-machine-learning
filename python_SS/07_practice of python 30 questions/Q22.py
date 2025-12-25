# num = int(input("enter your input sir ji :- "))
# print(f"this is your input :- {num}")
# arm = 0
# check = num
# while(num>0):
#     r = num%10
#     arm  = (r*r*r)+arm 
#     num = num//10
# print(f"this is sum off your input number :- {arm}")
# if arm==check:
#     print(f"{arm} :-is armstrong number")
# else:
#     print(f"{arm}:- not armstrong number")
    

num = 1000
sum = num
arm = 0

for i in range(num+1):
    r = num%10
    arm  = (r*r*r)+arm 
    num = num//10
    print(f"sum of arm :- {i}")
    # if arm == sum[i] :
    #     print(f"{arm} :-is armstrong number")
    # else:
    #     print(f"{arm}:- not armstrong number")

