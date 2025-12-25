# Find shape of the data mean how many >> ROWS << and >> COLUMNS << in this dataset.

import numpy as np

D2 = np.array([[1,2,3],
               [4,5,6]])
print("this is a shape of this matrix  :-" , D2.shape)

# output :-
# this is a shape of this matrix  :- (2, 3)


# # Find >> size << of dataset and matrix 

D2 = np.array([[1,2,3],
               [4,5,6]])
print("this is a size of this matrix  :- ",D2.size)

# output :-
# this is a size of this matrix  :-  6


# Find dimension of this matrix and the dataset.

D2 = np.array([[[1,2,3],[4,5,6],[4,5,6]]])
D3 = np.array([[[[1,2,3],[4,5,6],[4,5,6],[4,5,6]]]])
D4 = np.array([[1,2,3],[4,5,6]])

print("this is a dimention of this matrix  :- ",D2.ndim)
print("this is a dimention of this matrix  :- ",D3.ndim)
print("this is a dimention of this matrix  :- ",D4.ndim)

# output :-

# this is a dimention of this matrix  :-  3
# this is a dimention of this matrix  :-  4
# this is a dimention of this matrix  :-  2



# >>> ------------------------------------------------------<<<<<<




# check data type of this list or dataset.

D2 = np.array([[[1,2,3],[4,5,6],[4,5,6]]])
print("this is data type of this data or matrix :- ",D2.dtype)

# output :- 
# this is data type of this data or matrix :-  int64



D2 = np.array([[1.0,2.1,1.0,3.0]])

change_data_type = D2.astype(int)
print("this is a integer list of float list :- ",change_data_type)
print(" here convert data float  to  int :-",change_data_type.dtype)
               
# output :- 
# this is a integer list of float list :-  [[1 2 1 3]]
#  here convert data float  to  int :- int64


# mathmetical calculation in numpy:-

D2 = np.array([[[1,2,3],[4,5,6],[4,5,6]]])

print("sum :- ",D2+5)
print("multiplication :- ",D2*5)
print("exponential :- ",D2**5)
print("divide :- ",D2/5)
print("modules :- ",D2%5)
print("minus :- ",D2-5)


# aggregation functions:-

D2 = np.array([10,20,30,40,50,60])

# print(np.sum(D2))
# print(np.mean(D2))
print(np.min(D2))
print(np.max(D2))
# print(np.str(D2))
# print(np.var(D2))
