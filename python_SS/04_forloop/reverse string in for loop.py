n = input("Enter a string: ")
m = ""
for i in range(len(n)-1, -1, -1):
    print(n[i])
m = m+n[i]
print(f"your reversed string is {m}")
 