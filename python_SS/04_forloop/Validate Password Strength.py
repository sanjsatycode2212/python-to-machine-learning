p =  input("Enter your password: ")
if len(p) <= 8:
    print("Weak password")
elif len(p) > 8 and any(char.isdigit() for char in p) and any(char.isupper() for char in p) and any(char.islower() for char in p) and any(char in "!@#$%^&*()-+" for char in p):
    print("Strong password")
else:   
    print("Moderate password")  