a = "abhishek"
for char in a:
    print(char)
    l = type(bh)
print(l)
for i in range(1, 4, 2): #here i give a specigic range and then i print a which is string, using thid i will get the index value.
    print(a[i])


user1 = int(input("user1:-"))
user2 = int(input("user2:-"))
user3 = int(input("user3:-"))
user4 = int(input("user4:-"))

if user1>user2 and user1>user3 and user1>user4:
    print("user1 is greatest", user1)
elif user2>user1 and user2>user3 and user2>user4:
    print("user2 is greatest", user2)
elif user3>user1 and user3>user2 and user3>user4:
    print("user3 is greatest", user3)
elif user4>user1 and user4>user2 and user4>user3:
    print("user4 is greatest", user4)
else:
    print("inavlid number")


### question 8

spam = "make a lot of money"
spam2 = "buy now", 
spam3 = "subscribe this",
spam4 = "click this"
user = input("say something:->>> "  "  ")

while user==spam or user!=spam:
    if user==spam: #or user == spam2 or user == spam3 or user == spam4
        print("you are spammer")
    else:
        print("hello") # print("you are not spammer")
    user = input("say something:->>> "  "  ")


# question 10

user = input("enter your name :- ")
list =["satyam","shivam","sundram","abhisekh"]

if user in list:
    print("done")
else:
    print("out of list")


# qyes 11

post = " hello my name is satyam and i am currenlty workig in style union"
user = input("say about satyam:->>")
if user in post:
    print("yes you are satyam")
else:
    ("spam")
