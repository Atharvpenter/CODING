# array
# print array using numpy
import numpy as np
a = np.array([11,11,11,11])
print(a)

# print array's type and datatype
import numpy as np
a1 = np.array([11,22,33,44,55])
print(a1)
print("Type :",type(a1))
print("DataType :",a1.dtype)

# list
import numpy as np
list = [1,2,3,4,5]
print(type(list))

# Arithmetic operations using numpy
import numpy as np
a2 = np.array([10,20,30,405,00])
print("Array - Addition: ",a2 + 2)
print("Array - Subtraction: ",a2 - 2)
print("Array - Multiplication: ",a2 * 2)
print("Array - Division: ",a2 / 2)

# Arranging numpy
# zeros
import numpy as np
a = np.zeros(5,dtype = int)
a1 = np.zeros(3,dtype = bool)
print(a)
print(a1)

# 2D array
import numpy as np
a = np.zeros((3,3),dtype = int)
a1 = np.zeros((2,2),dtype = bool)
print(a)
print(a1)

# ones
import numpy as np
a = np.ones((3,3),dtype = int)
a1 = np.ones((2,2),dtype = bool)
print(a)
print(a1)

# Arrange function
# print 1 to 10
import numpy as np
a = np.arange(10)
print(a)

# print table of 2 using arange function
import numpy as np
a = np.arange(2,21,2)
print(a)

# print table of 2 in reverse
import numpy as np
a = np.arange(20,1,-2)
print(a)

# print table of 2 in 2D
a2 = np.arange(2,21,2).reshape(2,5)
print(a2)

# linspace function
import numpy as np
a = np.linspace(1,10,5)
print(a)

a1 = np.linspace(2,2,6)
print(a1)

# Accessing elements
import numpy as np
a = np.array([10,20,30,40,50,60])
print(a[1])

# full function
import numpy as np
a = np.full((3,3),9)
print(a)

a1 = np.array([10,20,30,40,50,60])
print(a1[1:5])
print(a1[:4])
print(a1[3:])
print(a1[::2])
print(a1[::-1])

# slicing function
mat = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
print(mat[0,2])
print(mat[1:3 , 0:2])
print(mat[1: , 0:])   
print(mat[:,:]) 
print(mat[: , :1]) 
print(mat[1: , :1]) 
print(mat[-1,0])

# boolean indexing
import numpy as np
a = np.array([10,20,30,40,50,60])
boolean_mask = a > 40
print(a[boolean_mask])

# filter array function
import numpy as np
a = np.array([10,20,30,40,50,60])
boolean_mask = a > 40
print(a[boolean_mask])
filterArray = a[boolean_mask]
print(filterArray)

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
print(np.ceil(a)) # [ 4.  6. -8.  2. 11.]

# Floor -> Rounds each element down to the nearest integer.
a1 = np.array([3.14,2.67,-5.89,45.67])
print(np.floor(a1)) # [ 3.  2. -6. 45.]

# Round -> Rounds elements to the nearest integer (or specified decimals).
a2 = np.array([3.14,2.67,-5.89,45.46])
print(np.round(a2)) # [ 3.  3. -6. 45.]

# Absolute -> Returns the non-negative value of each element.
a3 = np.array([3.14,2.67,-5.89,45.46])
print(np.abs(a3)) # [ 3.14  2.67  5.89 45.46]

# aggregate function
# sum of all array mean,median,max-min,standard deviations
import numpy as np
a = np.array([10,20,30,40,50])
sum = np.sum(a)
print(sum)

# mean
import numpy as np
a = np.array([10,20,30,40,50])
print(np.mean(a))

# median
import numpy as np
a = np.array([10,20,30,40,50])
print(np.median(a))

# MIN MAX
import numpy as np
a = np.array([10,20,30,40,50])
print(np.min(a))
print(np.max(a))

# standard deviations
import numpy as np
a = np.array([10,20,30,40,50])
print(np.var(a))
print(np.std(a))

# Array Sorting
import numpy as np
a = np.array([10,20,30,40,50])
a1 = np.array([60,70,80,90,100])
indices = np.argsort(a)
print(indices)
print(a[indices])
print(a1[indices])

