# QUESTION :>>>> 1


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print("Both numbers are equal")
## here some issue in else printing beccause if we if condition is not true than else print but if use give same number than
##a cmpiler return again else part but both number are same so to avoid this we use elif statement.


