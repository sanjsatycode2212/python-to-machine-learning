import numpy as np
import pandas as pd

labels = ["a","b","c"]
my_list = [10,20,30]
arr = np.array([10,20,30])

# a = pd.Series(my_list)
# print(a)

# output :----
# 0    10
# 1    20
# 2    30
# dtype: int64

#we can give index of this list ..

a = pd.Series(my_list,index = labels )
print(a)


# output :----

# a    10
# b    20
# c    30
# dtype: int64


b = pd.Series(arr)
print(b)

# OUTPUT:-----
# 0    10
# 1    20
# 2    30
# dtype: int64

# Note :- series allways in one dimentional :--------


d = {1:10,2:20,3:30}
print(pd.Series(d))

# output :-------

# 1    10
# 2    20
# 3    30
# dtype: int64