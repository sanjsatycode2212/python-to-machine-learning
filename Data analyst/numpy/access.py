import numpy as np
# D2 = np.array([10,20,30,40,50,60])

# print(D2[0])
# print(D2[1])
# print(D2[2])
# print(D2[3])
# print(D2[4])
# print(D2[5])

# print("uper + he niche - he")

# print(D2[-1])
# print(D2[-2])
# print(D2[-3])
# print(D2[-4])
# print(D2[-5])




# slicing [start:stop:step]:-----------------<<<<<<<<<<<<<<>>>>>>>>

# D2 = np.array([10,20,30,40,50,60])
# print(D2[1:5])
# print(D2[:4])
# print(D2[::2])
# print(D2[::-1])

# D2 = np.array([10,20,30,40,50,60])
# print(D2[[0,2,5]])



# boolean masking(filtering):--------------

# D2 = np.array([10,20,30,40,50,60])
# print(D2[D2 > 30])


# Reshaping and manipulating a data :- --------------------

# D2 = np.array([10,20,30,40,50,60])
# reshape_D2 = D2.reshape(2,3)
# print(reshape_D2)    


# ravel() and flatten():-

# D2 = np.array([[[1,2,3],[4,5,6],[4,5,6]]])
# print(D2.ravel())  # only for view
# print(D2.flatten()) # convert in one dimention


# sum of two matrix using concatenate():-------



# D2 = np.array([1,2,3])
# D3 = np.array([4,5,6])

# new_arr = np.concatenate((D2,D3))
# print("this is new array which is creat using concatenate() :- ",new_arr)


# delete and element and matrix permanently usinf >>>delete()<<<----


# D2 = np.array([10,20,30,40,50,60])
# new_arr = np.delete(D2,2) # i want to delete 30 in this list.
# print(new_arr)


D2 = np.array([1,2,3])
D3 = np.array([4,5,6])
print(np.vstack((D2,D3)))  # row wise
print(np.hstack((D2,D3))) # column wise



# >>>>>>>>>>>> stacking.py <<<<<<<<<<<<<<,

D2 = np.array([1,2,3])
D3 = np.array([4,5,6])
print(np.vstack((D2,D3)))  # row wise
print(np.hstack((D2,D3))) # column wise


# [[1 2 3]
#  [4 5 6]]

# [1 2 3 4 5 6]




# split data in multiple form.


D2 = np.array([10,20,30,40,50,60])
print(np.split(D2,3))

#[array([10, 20]), array([30, 40]), array([50, 60])]