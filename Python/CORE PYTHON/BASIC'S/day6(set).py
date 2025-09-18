# What is Set?
# Unordered collectoin of elements.
# Set does not store duplicate elements.... it prints last entry.
# Set does not store values by index....
# it can be mutable , change....
# anything inside curly bracket {} is called as set.


#Set = {11,22}
#print(Set)
#print(type(Set))

#set = {11,22,22,44,55}
#print(set)

# Using for loop in Set --->
#setA = {11,22,33,44,55}
#for x in setA:
 #   print(x)
    
# Different methods in Sets ---->
# INTERSECTION -> Is used to find common elements in two sets

#setA = {11,22,33}
#setB = {22,44,66,33}
#setC = setA.intersection(setB)
#setC = setB.intersection(setA)
#print(setC)


#INTERSECTION_UPDATE --> Is used to update the set keeping common elements.
#setA.intersection_update(setB)
#print(setC)

#DIFFERENCE --> it is used to find one element that are common in other set.

setD = {11,22,33,44}
setE = {11,88,44,99}
setF = setD.difference(setE)
print(setF)

#SYMMETRIC_DIFFERENCE --> it removes common elments.

setR = {11,22,33}
setQ = {33,44,55}
# setE = setR.symmetric_difference(setQ)
# print(setE)
setR.symmetric_difference_update(setQ)
print(setR)

