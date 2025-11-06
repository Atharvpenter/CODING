import numpy as np 
arr = np.full((3,3),9)
print(arr)

# program 2
q1 = np.arange(10)
print(q1)
print(np.arange(5,15))
print(np.arange(0,21,2))

#                0  1  2  3  4  5  6  7
arr = np.array([10,20,30,40,50,60,70,80])
#               -8 -7 -6 -5 -4 -3 -2 -1
print(arr[1:5])
print(arr[:4])
print(arr[3:])
print(arr[::2])
print(arr[::-1])

# Slicing of 2D array 
mat = np.array([
 #   0   1 2
    [10,20,30], #0
    [40,50,60], #1
    [70,80,90]  #2
])

#    row
#print(mat[row,col])
print(mat[1:3,0:2])
print(mat[1:,0:])
print(mat[:,:])
print(mat[:,:1])
print(mat[1:,:1])