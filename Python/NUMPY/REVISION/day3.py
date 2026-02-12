# array
# print array using numpy
import numpy as np
a = np.array([1,2,3,4])
print(a)

# print array's type and datatypes
import numpy as np
a = np.array([11,22,33,44])
print(a)
print("type :",type(a))
print("Dtype :",a.dtype)

# arithmetic operations using numpy
import numpy as np
a = np.array([1,2,3,4,5,6,7,8,9])
print("Array - Addition :", a + 2)
print("Array - substraction :", a - 2)
print("Array - multiplication :", a * 2)
print("Array - division :", a / 2)

# arranging numpy
# zeros
import numpy as np
a = np.zeros(5,dtype = int)
a1 = np.zeros(3,dtype = bool)
print(a)
print(a1)

# 2D Array
import numpy as np
a = np.zeros((3,3),dtype = int)
a1 = np.zeros((2,2),dtype = bool)
print(a)
print(a1)

# ones
import numpy as np
a = np.ones((3,3),dtype=int)
a1 = np.ones((2,2),dtype=bool)
print(a)
print(a1)

# Arrane function
# print 1 to 10
import numpy as np
a = np.arange(10)
print(a)

# print table of 2
import numpy as np
a = np.arange(2,22,2)
print(a)

# print it in reverse
import numpy as np
a = np.arange(20,1,-2)
print(a)

# arange in 2D
import numpy as np
a = np.arange(2,22,2).reshape(2,5)
print(a)

# linspace function
import numpy as np
a = np.linspace(1,10,5)
print(a)

# accessing elements
import numpy as np
a = np.array([10,20,30,40,50,60,70,80,90])
print(a[2])

# full function
import numpy as np
a = np.full((3,3),9)
print(a)

# Rounding off and absolute values
# ceiling floor , Round Absolute
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
