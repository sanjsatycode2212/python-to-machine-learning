a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
c = int(input("Enter third number: "))
if a == b and b == c:
    print("Equilateral triangle")  
elif a == b or b == c or a == c:
    print("Isosceles triangle")
elif a != b and b != c and a != c:
    print("Scalene triangle")
else:
    print("invalid")