name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 18:
    print(f"Hello {name}, you are eligible to vote.")
else:
    print(f"Hello {name}, you are not eligible to vote yet.")  