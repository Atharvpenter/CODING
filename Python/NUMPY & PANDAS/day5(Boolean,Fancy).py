# Boolean indexing -> used to get boolean values

import numpy as np
arr = np.array([10,20,30,40,50,60,70,80])
bool_mask = arr > 40
print(bool_mask)
filterArray = arr[bool_mask]
print(filterArray)

# applying various conditions on boolean indexing
import numpy as np
arr = np.array([10,20,30,40,50,60,70,80])
# print arr>20 & arr<60
e = arr[(arr > 20) & (arr < 60)]
print(e)

mat = np.array([
    [10,25,30],
    [40,50,60],
    [70,85,90]
])

e1 = mat[mat<70]
print(e1)

# Fancy indexing ->It allows you to pick specific elements, rows, or columns directly.
             #  0  1  2  3  4  5   6
arr = np.array([10,20,30,40,50,60,70])
print(arr[[0,2,4]])

# print first row and last row
mat = np.array([
    [10,25,30],
    [40,50,60],
    [70,85,90]
])

print(mat[[0,2]])