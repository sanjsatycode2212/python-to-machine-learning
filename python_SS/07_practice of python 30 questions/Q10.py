str = input("enter your string :- ")
rev = ""
for i in range(len(str)-1,-1,-1):
    print(str[i])

if str == rev:
    print("your string is a pallindromic")
else:
    print("your string is not pallinfromic")