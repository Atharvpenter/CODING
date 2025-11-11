import numpy as np
mat = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

print(mat[0:2,0:2])
print(mat[:,1])
print(mat[:,1:])
print(mat[0,1])
print(mat[2,2])
print(mat[-1,0])

# Modifying the array
arr = np.array([5,10,15,20])
arr[0] = 99
print(arr)
# using slicing
arr[1:3] = [111,222]

# Extracting rows and columns 
arr2 = np.arange(1,17).reshape(4,4)
print(arr2)
# first row
print(arr2[0,:])
# last column
print(arr2[:,-1])
print(arr2[1:3,1:3])

# Boolean indexing 
arr = np.array([10,20,30,40,50,60,70])
boolean_mask = arr > 40 # [False False False False  True  True  True]
# filtered operation
print(arr[boolean_mask])