import numpy as np
import scipy.linalg as la
A = np.array([[1,2],[3,4]])
X = np.array([5,11])

I = np.array([[1,0],
              [0,1]])
lamda = 1
L = lamda*I
eigvalue = la.det(A-L)
print(eigvalue)

a = (A-lamda*I)@X
print(a)

