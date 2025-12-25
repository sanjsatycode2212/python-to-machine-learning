import numpy as np
import pandas as pd

df = pd.read_csv("C:\\Users\\satyam_07\\Downloads\\practice.csv")
print(df)

# # print(df.head())

# # print(df.columns)
# # Unnamed: 4    128976
# # Unnamed: 5    128976
# # Unnamed: 6    128975

# # print(df.info())

# print(df.isnull().sum())

# # df1 = df.drop(["Unnamed: 4","Unnamed: 5","Unnamed: 6"],axis=1)
# # print(df1)


# groupby function :-------

# print(df.groupby("Category")["Amount"].sum())


# print(df.groupby("Date")["Amount"].sum())

# # we can multiple columns in group by.....

# print(df.groupby(["Category","Date"])["Amount"].sum())


## >>>>>>>>>>>>  aggrigation <<<<<<<<<<<<<<<

# aggregation :- aggrefation mens mmultiple chizo ko ek sath combine kr ek result nikalne ka

print(df["Amount"].agg(["sum","mean","median","min","max","count","std"]).astype(int))


