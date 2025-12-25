# Data frame :- when we combine multiple series its call data frame :----

import numpy as np
import pandas as pd

data = {
    "name":["jhon","satyam","shivam","sundram"],
    "age" :[10,20,30,40],
    "City":["ahm","guj","mh","uk"],
    "salary":[65000,66000,47000,52500]
}
df= pd.DataFrame(data)
print(df)



#       name  age City  salary
# 0     jhon   10  ahm   65000
# 1   satyam   20  guj   66000
# 2   shivam   30   mh   47000
# 3  sundram   40   uk   52500



# print(df["name"])
# print(df["age"])
# print(df["salary"])
# print(df["City"])


# # creating a column :---
# df["designation"] = ["doctor","police","eng","doc"]
# print(df)


#       name  age City  salary designation
# 0     jhon   10  ahm   65000      doctor
# 1   satyam   20  guj   66000      police
# 2   shivam   30   mh   47000         eng
# 3  sundram   40   uk   52500         doc



# removing columns :- 
# df = df.drop("designation",axis=1)
# print(df)
# if we want to delete permanent column the use inplace = true

#       name  age City  salary
# 0     jhon   10  ahm   65000
# 1   satyam   20  guj   66000
# 2   shivam   30   mh   47000
# 3  sundram   40   uk   52500



# selecting and accessing rows of the data:-------

# df = df.loc[[0,1]]
# print(df)

#      name  age City  salary
# 0    jhon   10  ahm   65000
# 1  satyam   20  guj   66000

# df = df.loc[[0,1]][["City","salary"]]
# print(df)

#   City  salary
# 0  ahm   65000
# 1  guj   66000

# df = df.iloc[1,3]
# print(df)


# conditional selection :-----------------

# i only want to see whose pepole age above 10.

df = df[df["age"] > 10]
print(df)

#       name  age City  salary
# 1   satyam   20  guj   66000
# 2   shivam   30   mh   47000
# 3  sundram   40   uk   52500


# if i want only those people theri age is grater that 10 and city is uk.
df = df[(df["age"] > 20 & (df["City"] == "uk"))]
print(df)


#       name  age City  salary
# 1   satyam   20  guj   66000
# 2   shivam   30   mh   47000
# 3  sundram   40   uk   52500







