import numpy as np
import pandas as pd



# finding missing data

data = {
    "a":[1,np.nan,3,4,np.nan],
    "b":[1,2,np.nan,np.nan,5],
    "c":[np.nan,np.nan,3,4,np.nan],
    "d":[np.nan,2,3,np.nan,5]
}

df1 = pd.DataFrame(data)
print(df1)


#      a    b    c    d
# 0  1.0  1.0  NaN  NaN
# 1  NaN  2.0  NaN  2.0
# 2  3.0  NaN  3.0  3.0
# 3  4.0  NaN  4.0  NaN
# 4  NaN  5.0  NaN  5.0

print(df1.isna())


#        a      b      c      d
# 0  False  False   True   True
# 1   True  False   True  False
# 2  False   True  False  False
# 3  False   True  False   True
# 4   True  False   True  False

print(df1.isna().sum())

# a    2
# b    2
# c    3
# d    2
# dtype: int64

# we can find ki hamare dataset me ek bhi esi column he jisme data hi nhi he.

print(df1.isna().any())

# a    True
# b    True
# c    True
# d    True
# dtype: bool

# ---------------------------------------------------------------------------------------



# removing missing values

print(df1)

#      a    b    c    d
# 0  1.0  1.0  NaN  NaN
# 1  NaN  2.0  NaN  2.0
# 2  3.0  NaN  3.0  3.0
# 3  4.0  NaN  4.0  NaN
# 4  NaN  5.0  NaN  5.0

print(df1.dropna())

# Empty DataFrame
# Columns: [a, b, c, d]
# Index: []

print(df1.dropna(thresh=3))  # thresh=3 means ager row me total 3 values hogi wahi rkhega baki hata dega....

#      a   b    c    d
# 2  3.0 NaN  3.0  3.0



# ------------------------------------------------------------------------------------------------------




# filling the missing values

print(df1)

#      a    b    c    d
# 0  1.0  1.0  NaN  NaN
# 1  NaN  2.0  NaN  2.0
# 2  3.0  NaN  3.0  3.0
# 3  4.0  NaN  4.0  NaN
# 4  NaN  5.0  NaN  5.0

print(df1.fillna(0))

#      a    b    c    d
# 0  1.0  1.0  0.0  0.0
# 1  0.0  2.0  0.0  2.0
# 2  3.0  0.0  3.0  3.0
# 3  4.0  0.0  4.0  0.0
# 4  0.0  5.0  0.0  5.0

print(df1.fillna(4).astype(int))

#    a  b  c  d
# 0  1  1  4  4
# 1  4  2  4  2
# 2  3  4  3  3
# 3  4  4  4  4
# 4  4  5  4  5


values = {"a":120,"b":130,"c":50,"d":60}
print(df1.fillna(value=values))

#        a      b     c     d
# 0    1.0    1.0  50.0  60.0
# 1  120.0    2.0  50.0   2.0
# 2    3.0  130.0   3.0   3.0
# 3    4.0  130.0   4.0  60.0
# 4  120.0    5.0  50.0   5.0

print((df1.fillna(value=values).astype(int)))

#      a    b   c   d
# 0    1    1  50  60
# 1  120    2  50   2
# 2    3  130   3   3
# 3    4  130   4  60
# 4  120    5  50   5

print(df1.fillna(df1.mean()))

#           a         b    c         d
# 0  1.000000  1.000000  3.5  3.333333
# 1  2.666667  2.000000  3.5  2.000000
# 2  3.000000  2.666667  3.0  3.000000
# 3  4.000000  2.666667  4.0  3.333333
# 4  2.666667  5.000000  3.5  5.000000

print(df1.fillna(df1.mean()).astype(int))


#    a  b  c  d
# 0  1  1  3  3
# 1  2  2  3  2
# 2  3  2  3  3
# 3  4  2  4  3
# 4  2  5  3  5





