
#printing a numpy array

import numpy as np #importing numpy library as np 
x=np.array([5,12,54,17]) #this is an one dimensional array mathematically we call it VECTOR
print (x)
print(x.shape) #it check how many elements in this one dimensional array
print(type(x))


#numpy MATRIX
matrix= np.array([
    [1,2,3],[5,6,7]
])
print(matrix) #print this 2x3 matrix
print(matrix.shape) #it check number of elements, here rows and coloumn 

#3D Arrays
z=np.array([
    [
        [2,3],[4,5] # this is a 2 dimensional array
        ],
    [
        [7,8], #when adds another layer of array it becomes 3D array
        [9,2]
        ]
    ])
print(z)
print(z.shape)

# Scalar - single number

# Vector - 1D

# Matrix - 2D



#Indexing
b=np.array([15,7,64,17,234,44])
print(b[2]) #print 2nd position number. List indexing starts from 0,here b[2]is 64
print(b[0])
print(b[4])

#Matrix Indexing
c=np.array([ 
            
        [1,2,3,7],
        [7,8,9,3],
        [11,15,19,17],
        [10,20,30,40]
        
        ])
print(c[1,1]) #indexing second row second element
print(c[3,2]) #indexing fourth row second element
print(c[3,2])


#Basic Arithmentic
d=np.array([5,7,4,3])
e=np.array([5,11,6,4])
print(d+e)
print(d-e)
print(d*e)

#IMPORTANT
#DOT Product
f=np.array([4,5,6])
g=np.array([7,8,9])
dot_result= np.dot(f,g)
print(dot_result)
#here 4x7 + 5x8 + 6x9 =122
#we need this in attention mechanism of Transformers

#Matrix Multiplication
g=np.array([[1,2],[3,4]])
e= np.array([[5,6],[7,8]])
mul_matrix = g@e
print(mul_matrix)

# 1×5 + 2×7 = 19
# 1×6 + 2×8 = 22
# 3×5 + 4×7 = 43
# 3×6 + 4×8 = 50

