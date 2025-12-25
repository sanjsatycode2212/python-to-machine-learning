import numpy as np
# prices = np.array([100,200,300])
# discount = 10

# final_prices = np.array([])
# for price in prices:
#     final_price = price - (price * discount / 100)
# d = np.append(prices,final_price)
# print(d)

# # print(final_prices)
# hii = d.astype(int)
# print(hii)


# arr = np.array([100,200,300])
# result = arr*5
# print(result)


# matrix = np.array([[100,200,300],[100,200,300]])
# vector = np.array([10,20,30])
# result = matrix+vector
# print(result)

# matrix addition:------------------


# arr1 = np.array([[100,200,300],[100,200,300]])
# arr2 = np.array([10,20])

# result = arr1+arr2
# print(result)
# print(arr1.reshape(2,3))
# output :- 
# ValueError: operands could not be broadcast together with shapes (2,3) (2,)

# issilye matrix ko +,- krne ke liye dimentionals same honi chahiye dono matrix.

# is error ko hum .reshape() se thik kr skte he.


arr1 = np.array([100,200,300])
arr2 = np.array([10,20,30])

# result = arr1+arr2
# print(result)


# find num values in matrix ;= ------

arr1 = np.array([[100,np.nan,300,np.nan,200,300]])
print(np.isnan(arr1))

# its return answer in true or false 
# jaha data hoga waha ye true kr dega jaha deta nhi hoga waha false kr dega.

# replace values nan ki jaagah.:-----

arr1 = np.array([[100,np.nan,300,np.nan,200,300]])
print(np.nan_to_num(arr1,nan=125))

# JAHA JAHA NUM VALUES HOGI WAHA WAHA 125 HO JAYEGA.

