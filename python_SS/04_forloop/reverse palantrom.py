n = input("Enter a string: ")
m = ""
for i in range(len(n)-1, -1, -1):
    m = m+n[i]
    print(m)
print(f"your reversed string is {m}")
if m==n:
    print("your string is paladtrom")
else:
    print("your string is not paladtrom")