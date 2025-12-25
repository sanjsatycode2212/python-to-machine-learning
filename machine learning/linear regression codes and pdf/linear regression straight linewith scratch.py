import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X = np.array([35, 40, 50, 60, 65]).reshape(-1, 1)
Y = np.array([1, 2, 3, 6, 5]).reshape(-1, 1)
print(X)
print(Y)



X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.30, random_state=40
)

lr = LinearRegression()
lr.fit(X_train, Y_train)

print("Coefficient (m):", lr.coef_)
print("Intercept (c):", lr.intercept_)
w = 0
b = 0
def model(w, x, b):
    f = w * x + b
    return f

result = model(2, 5, 3)
print(result)

plt.plot(data=result)
plt.show()
