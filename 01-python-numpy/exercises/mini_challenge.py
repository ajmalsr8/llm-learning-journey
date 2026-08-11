import numpy as np

A= np.array([[10,20],[5,10]])
B= np.array([[15,25],[6,8]])

#Matrix addition
print(np.array(A+B)) #also write print(A+B)

#Matrix Sub 
print(np.array(A-B))

#element wise matrix Multiplication
print(np.array(A*B))

#Matrix Multiplication
multiplication= A@B
print(multiplication)

print(A.shape)
print(B.shape)