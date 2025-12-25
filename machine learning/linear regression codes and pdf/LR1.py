import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X = np.array([1, 2, 3, 4, 5]) 
Y = np.array([35, 40, 50, 60, 65])

data = pd.DataFrame({
    "H":X,
    "marks":Y
})
print(data)

# data visualization using matplotlib.pyplot

# plt.plot(X, Y,marker = "o")
# plt.xlabel("Hours Studied")
# plt.ylabel("Marks")
# plt.grid(True)
# plt.title("Hours vs Marks")
# plt.show()
X_reshaped = X.reshape(-1, 1)

X_train,X_test,Y_train,Y_test = train_test_split(X_reshaped,Y,
                                                 test_size=0.28,
                                                 train_size=0.72,
                                                 random_state=42)
lr = LinearRegression()
lr.fit(X_train,Y_train)

y_pridict = lr.predict(X_test)
# print(y_pridict)

# print("Total data:", len(X))
# print("Training data:", len(X_train))
# print("Testing data:", len(X_test))
print(X_test)
print(Y_test)
print(y_pridict)
