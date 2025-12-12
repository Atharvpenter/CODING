# Universal function ->
# addition, multiplication, substraction,division, mod,square Root,log etc.

import numpy as np
arr1 = np.array([10,20,30])
arr2 = np.array([40,50,60])
print(np.add(arr1,arr2))
print(np.subtract(arr1,arr2))
print(np.multiply(arr1,arr2))
print(np.divide(arr1,arr2))
print(np.mod(arr1,3))
print(np.sqrt(arr1))
print(np.exp(arr1))
print(np.log(arr1))

# Rounding off and absolute values
# ceiling, floor, round, absolute
# ceiling -> Rounds each element up to the nearest integer.
arr = np.array([3.14,2.67,-5.89,45.67])
print(np.ceil(arr))

# floor -> Rounds each element down to the nearest integer.
arr2 = np.array([3.14,2.67,-5.89,45.67])
print(np.floor(arr2))

# round -> Rounds elements to the nearest integer (or specified decimals). 
arr2 = np.array([3.14,2.67,-5.89,45.46])
print(np.round(arr2,1))

# absolute -> Returns the non-negative value of each element.
arr2 = np.array([3.14,2.67,-5.89,45.46])
print(np.abs(arr2))
