# Temperature की 30-day array
# • Max, Min, Avg निकालना
# • कितने दिन > 40°C थे
# • Cold days (<20°C) count


import numpy as np

temperature = np.array([
    32, 34, 35, 33, 36, 
    38, 40, 41, 39, 37,
    35, 34, 36, 38, 39,
    40, 42, 41, 39, 37,
    36, 34, 33, 32, 31,
    30, 29, 28, 30, 32
])

print(temperature)

print("maximum tempreture :- ",np.max(temperature))
print("minimum tempreture :- ",np.min(temperature))


tem = np.sum(temperature)
ave = tem/30
print(ave)

cold_days = np.sum(temperature < 30)
print("Cold Days (below 30°C):", cold_days)

heat_days= np.where(temperature>=40)
print(heat_days)