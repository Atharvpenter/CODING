# aggregate functions ->
# sum of all numbers ->
import numpy as np
arr = np.array([10,20,30,40,50])
sum = np.sum(arr)
print(sum)


mat = (
    [10,20,30], #60
    [40,50,60]  #150
#    50,70,90 
    )
print(np.sum(mat))

# Sum by Rows ->
row = np.sum(mat,axis = 1)
print(row)

# Sum by Cols ->
col = np.sum(mat,axis = 0)
print(col)

# Mean ->
arr1 = ([10,20,30,40,50])
print(np.mean(arr1))

mat1 = (
    [10,20,30],
    [40,50,60]
    )
print(np.mean(mat,axis = 0)) #COls
print(np.mean(mat,axis = 1)) #Rows

# Median ->
arr2 = ([10,20,30,40,50])
print(np.median(arr2))

# Max , Min
arr2 = ([10,20,30,40,50])
print(np.min(arr2))

arr3 = ([10,20,30,40,50])
print(np.max(arr3))

# Standard Deviation ->  sqrt of variance
arr4 = ([10,20,30,40,50])
print(np.var(arr4))
print(np.std(arr4))