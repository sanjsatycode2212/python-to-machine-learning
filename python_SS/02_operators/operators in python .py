a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# addition
add = a+b
print("Addition:", add)
# subtraction
sub = a-b
print("Subtraction:", sub)
# multiplication
mul = a*b
print("Multiplication:", mul)
# division
div = a/b
print("Division:", div)
# modulus
mod = a%b
print("Modulus:", mod)
# exponentiation
exp = a**b
print("Exponentiation:", exp)
# floor division
floordiv = a//b
print("Floor Division:", floordiv)
# comparison operators
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater than:", a > b)
print("Less than:", a < b)
print("Greater than or equal to:", a >= b)
print("Less than or equal to:", a <= b)
# logical operators
print("Logical AND:", (a > 0) and (b > 0))
print("Logical OR:", (a > 0) or (b > 0))
print("Logical NOT:", not(a > 0))
# bitwise operators
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)
# assignment operators
c = a
c += b
print("Assignment (c += b):", c)
c = a
c -= b
print("Assignment (c -= b):", c)
c = a
c *= b
print("Assignment (c *= b):", c)
c = a
c /= b
print("Assignment (c /= b):", c)
c = a
c %= b
print("Assignment (c %= b):", c)
c = a
c **= b
print("Assignment (c **= b):", c)
c = a
c //= b
print("Assignment (c //= b):", c)
# membership operators
list1 = [a, b, 10, 20]
print("Membership (a in list1):", a in list1)
print("Membership (30 not in list1):", 30 not in list1)
# identity operators
print("Identity (a is b):", a is b)
print("Identity (a is not b):", a is not b)     
a = 10
b = 10
print("Identity (a is b):", a is b)



