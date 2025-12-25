# in elif_else conditional statements are used to check multiple conditions.



# syntax with if:
# if condition:
#      code to be executed if condition is true
# elif condition2:
#      code to be executed if condition2 is true
# else:
#      code to be executed if both conditions are false


# >>>  You cna also create if elif ladder using multiple conditions of elif. <<<< 
####### Questions 1: 

# take the input of temperature in celsius
# Below 0°C → "Freezing Cold 
# 0°C to 10°C → "Very Cold 
# 10°C to 20°C → "Cold 
# 20°C to 30°C → "Pleasant 
# 30°C to 40°C → "Hot 
# Above 40°C → "Very Hot " 

temp = float(input("enter the temperature in celsius:"))
if temp < 0:
    print("Freezing Cold")
elif 0 <= temp < 10:
    print("Very Cold")
elif 10 <= temp < 20:
    print("Cold") #               >>>>>>  you can do multiple question like this <<<<                    
elif 20 <= temp < 30:
    print("Pleasant")
elif 30 <= temp < 40:
    print("Hot")
else:
    print("Very Hot")

# output: enter the temperature in celsius:- -5
#         Freezing Cold
# output: enter the temperature in celsius:- 7
#         Very Cold
# output: enter the temperature in celsius:- 15
#         Cold
# output: enter the temperature in celsius:- 25
#         Pleasant
# output: enter the temperature in celsius:- 35
#         Hot
# output: enter the temperature in celsius:- 45
#         Very Hot

