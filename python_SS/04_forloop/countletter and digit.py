str1 = input("Enter a string: ")
letters = 0
digits = 0
special = 0
for i in str1:
    if i.isalpha():
        letters +=1
    elif i.isdigit():
        digits += 1
    else:
        special += 1        
print(f"letters: {letters}, digits: {digits}, special: {special}")
