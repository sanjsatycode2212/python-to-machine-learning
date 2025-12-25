## print reverse of giving string.

str = input("enter your string :- ")
rev = ""
for i in range(len(str)-1,-1,-1):
    print(str[i])