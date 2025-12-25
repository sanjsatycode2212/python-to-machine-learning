temp = int(input("Enter a temperature in Celsius: "))
if temp >= 0 and temp<=0:
    print("freezing cold.")
elif temp>=0 and temp<=10:
    print("very cold.")
elif temp>=10 and temp<20:
    print("cold.")  
elif temp>=20 and temp<=30:
    print("normal temp.")
elif temp>=30 and temp<=40:
    print("hot.")
elif temp==40:
    print("very hot.")
else:
    print("normal day.")
