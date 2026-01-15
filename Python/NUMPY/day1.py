# array
# print array using numpy
import numpy as np
a = np.array([1,2,3,4,5,6])
print(a)

# print array's type and dataType
import numpy as np
a1 = np.array([11,22,33,44,55])
print(a1)
print("Type: ",type(a1))
print("DataType:",a1.dtype)

# list
import numpy as np
list = [5,6,7,8,9]
print(type(list))

# Arithmetic operation using numpy
import numpy as np
a2 = np.array([10,20,30,40,50])
print("Array - Addition: ",a2 + 2)
print("Array - Subtraction: ",a2 - 2)
print("Array - Multiplication: ",a2 * 2)
print("Array - Division: ",a2 / 2)

# Arranging numpy
import numpy as np
a = np.zeros(5,dtype = int)  # 0 0 0 0 0 
a1 = np.zeros(5,dtype = bool) # false false false false false
print(a)
print(a1)

# 2D Array - Rows and Columns for Zeros
import numpy as np
a = np.zeros((3,3), dtype = int) # it will create 3x3 matrix
a1 = np.zeros((2,2),dtype = bool)
print(a)
print(a1)

# 2D Array - Rows and Columns for Ones
a2 = np.ones((3,3),dtype = int) # it will give all 1 in matrix
a3 = np.ones((2,2),dtype = bool) # return true in all matrix
print(a2)
print(a3)

# Arange function
import numpy as np
a = np.arange(10) # it will print 1 to 10 digits
print(a)

a1 = np.arange(2,21,2) # it will print table of 2 using arange function
print(a1)

a2 = np.arange(3,31,3).reshape(5,2) # it will table of 3 but in matrix format as it has been reshape
print(a2)

# Linspace function
import numpy as np
a = np.linspace(1,10,5) # used to create equal space between elements
print(a)

a1 = np.linspace(2,10,10)
print(a1)

# Accessing elements
import numpy as np
            #  0  1  2  3  4  5
a = np.array([10,20,30,40,50,60]) # printing index values
            # -6 -5 -4 -3 -2 -1      
print(a[1])
print(a[-1]) # print from reverse. It always starts from 1 not from 0

# Full function
import numpy as np
a = np.full((3,3),9) # it will print 3x3 matrix with 9 as the value
print(a)

a1 = np.array([10,20,30,40,50,60])
print(a1[1:5]) # 20,30,40,50
print(a1[:4]) # 10,20,30,40
print(a1[3:]) # 40,50,60
print(a1[::2]) # 10,30,50
print(a1[::-1]) # 60,50,40,30,20,10

# Slicing function
mat = np.array([
#    0  1  2
    [10,20,30], # 0
    [40,50,60], # 1
    [70,80,90]  # 2
])
#print(mat[row,col])
print(mat[0,2]) # 30
print(mat[1:3 , 0:2]) # 40,50  70,80
print(mat[1: , 0:]) # 40,50,60    
print(mat[:,:]) # prints all elements
print(mat[: , :1]) # 10,40,70
print(mat[1: , :1]) # 40,70
print(mat[-1,0])

# Modifying the Array
import numpy as np
a = np.array([5,10,15,20,25])
a[0] = 1
print(a)

# using slicing
a[1:3] = [2,3]
print(a)

# Exracting rows and columns
import numpy as np
a = np.arange(1,17).reshape(4,4)
print(a)

# printing first row
print(a[0 , :])

# printing first column
print(a[: , 0])

# last column
print(a[:,-1])

# Boolean Indexing
import numpy as np
a = np.array([10,20,30,40,50,60,70,80])
boolean_mask = a > 40
print(a[boolean_mask])

# FilterArray function
import numpy as np
a = np.array([10,20,30,40,50,60,70,80])
boolean_mask = a > 40
print(a[boolean_mask])
filterArray = a[boolean_mask]
print(filterArray)

mat = np.array([
    [10,20,30],
    [40,50,60]
])
w = mat[mat < 30]
print(w)

# fancy indexing->It allows you to pick specific elements, rows, or columns directly.
# Universal function ->
# addition, multiplication, substraction,division, mod,square Root,log etc.
import numpy as np
a = np.array([10,20,30,40])
a1 = np.array([50,60,70,80])
print(np.add(a,a1))
print(np.subtract(a,a1))
print(np.multiply(a,a1))
print(np.divide(a,a1))
print(np.sqrt(a1))
print(np.mod(a,a1))
print(np.exp(a1))
print(np.log(a))

# Rounding off and Absolute values
# Ceiling floor, Round, Absolute
# Ceiling floore -> ROunds each element upto the nearest integer.
import numpy as np
a = np.array([3.14,5.7,-8,1.1,10.91])
print(np.ceil(a))

# Floor -> Rounds each element down to the nearest integer.
a1 = np.array([3.14,2.67,-5.89,45.67])
print(np.floor(a1))

# Round -> Rounds elements to the nearest integer (or specified decimals).
a2 = np.array([3.14,2.67,-5.89,45.46])
print(np.round(a2))

# Absolute -> Returns the non-negative value of each element.
a3 = np.array([3.14,2.67,-5.89,45.46])
print(np.abs(a3))

# Aggregate functions ->
# Sum of all array, Mean, Median, Max-Min, Standard deviations.
import numpy as np
a = np.array([10,20,30,40,50,60])
sum = np.sum(a)
print(sum)

mat = (
    [10,20,30], #60
    [40,50,60]  #150
#    50,70,90 
    )
print(np.sum(mat))

# sum by rows -> axis = 1
row = np.sum(mat, axis = 1)
print(row)

# sum by cols -> axis = 0
col = np.sum(mat, axis = 0)
print(col)

# Mean
a2 = np.array([10,20,30,40,50])
print(np.mean(a2))

# Median
a3 = np.array([10,20,30,40,50])
print(np.median(a3))

# Min Max
a4 = np.array([10,20,30,40,50])
print(np.max(a4))
print(np.min(a4))

# Standard deviations
a5 = ([10,20,30,40,50])
print(np.var(a5))
print(np.std(a5))

# Array Sorting
import numpy as np
a = np.array([10,20,30,40,50])
sort = np.sort(a)
print(sort)

# Aggregate Sorting
arr = np.array([50,60,10,80,20])
arr2 = np.array([50,60,100,80,20])
indices = np.argsort(arr)
print(indices)
print(arr[indices])
print(arr2[indices])

# Searching
import numpy as np
a = np.array([10,20,30,40,50])
search = np.where(a > 30)
print(a[search])

# Searching with conditions
import numpy as np
a = np.array([10,20,30,40,50])
result = np.where(a > 30, "Pass","Fail")
print(result)

# counting non zeros ->
import numpy as np
a = ([22,0,49,0,0])
print(np.count_nonzero(a))