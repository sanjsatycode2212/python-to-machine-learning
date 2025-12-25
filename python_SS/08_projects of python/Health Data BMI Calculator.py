
# >>>>>>>>>>>>>>>>>>   these all are steps <<<<<<<<<<<<<<<<<<<<<<<<<<<

# import liabrary
# create height and weight array
# find BMI using weight/(height**2)
# 4. BMI Categories
# Underweight < 18.5
# Normal 18.5 - 24.9
# Overweight 25 - 29.9
# Obese >= 30
# Highest & Lowest BMI
# Healthy persons (normal category)


import numpy as np

heights = np.array([1.70, 1.55, 1.80, 1.62, 1.75])
weights = np.array([70, 50, 90, 55, 80])

BMI = weights/(heights**2)
print("BMI :- ",BMI)

underweight = BMI <18.5
underweight = BMI < 18.5
normal = (BMI >= 18.5) & (BMI < 25)
overweight = (BMI >= 25) & (BMI < 30)
obese = BMI >= 30

print("Underweight count:", np.sum(underweight))
print("Normal count:", np.sum(normal))
print("Overweight count:", np.sum(overweight))
print("Obese count:", np.sum(obese))

print("highest BMI :- ",np.max(BMI))
print("lowest BMI :- ",np.min(BMI))

healthy_persons = np.where(normal)[0]
print("Index of healthy persons:", healthy_persons)

