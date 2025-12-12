# Sorting ->

import numpy as np
arr = np.array([11,99,33,44,22,55,88])
e = np.sort(arr)
print(e)

# 2D array sorting ->
mat = np.array([
    [1,5,7],
    [2,3,8]
    ])
print(np.sort(mat,axis=1)) # rows
print(np.sort(mat,axis=0)) # columns

# Aggregate Sorting ->
arr = np.array([50,60,10,80,20])
arr2 = np.array([50,60,100,80,20])
indices = np.argsort(arr)
print(indices)
print(arr[indices])
print(arr2[indices])

# Searching ->
                # 0 1  2  3  4  5  6
arry = np.array([10,20,30,40,50,60,70])
i = np.where(arry > 30)
print(i)
print(arry[i])

# Searching with conditions ->
arr = np.array([10,20,30,44,56,78,66])
result = np.where(arr > 60,"Pass","Fail")
print(result)

# counting non zeros ->
arry = ([22,0,49,0,99,87])
print(np.count_nonzero(arr))

print(np.any(arr > 70))
# all
print(np.all(arr > -1))
