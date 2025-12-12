# SET ----------------->>>>>>>>
# Using for loop in set ------>
set = {11,22,33,44}
for x in set:
    print(x)
    
# Different methods in Set --------->
# 1. InterSection ->
setA = {11,22,33}
setB = {22,44,66,33}
setC = setA.intersection(setB)
setD = setB.intersection(setA)
print(setC)
print(setD)

# 2. Intersection_update ->
setE = setA.intersection_update(setB)
print(setE)

# 3. Difference ->
setF = setA.difference(setB)
print(setF)

# 4.Symmetric difference ->
setG = setA.symmetric_difference(setB)
print(setG)

# Class ----------------------->>>>>>>>>>>
class person:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
atharv = person("atharv ","penter")
atharv.displayName()

# class 2 ->
class two:
    country = "Bharat"
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
    def ChangeCountry(cls):
        cls.country = "India"
atharv = two("Ram ","Sham")
atharv.displayName()
print(atharv.firstname)
print(atharv.country)

# List Comprehension ---------->
# [ Expression : Loop : Condition ]
# print above 40 marks using list comprehension ->
Marks = [33,44,55,77]
above40 = [x for x in Marks if x > 40]
print(above40)

# print age
birthyear = [ 2004,2009,1999,1987,1954,1965,2001,2021,1904]
age = [ 2025 - x for x in birthyear ]
print(age)

# Odd Evem
num = [1,2,3,4,5,6,7,8,9,10]
even = [ x for x in num if x % 2 == 0]
odd = [ x for x in num if x % 2 != 0]
print(even)
print(odd)

# Table of 2
numb = [1,2,3,4,5,6,7,8,9,10]
tableOf2 = [x * 2 for x in numb]
print(tableOf2)

# Table of 8
numbe = [1,2,3,4,5,6,7,8,9,10]
tableOf8 = [ x * 8 for x in numbe ]
print(tableOf8)

# birthday calculate
birthyear = [ 2000,2003,1999,1997,1998 ]
age = [ 2025 - x for x in birthyear]
print(age)

# Calculate marks
marks = [ 55,99,98,77,16,20,33,48,82]
upto = [ x for x in marks if x > 60]
print(upto)

# Calculate cgpa
cgpa = [8, 9, 5, 6, 8, 5,7]
aclass = [x for x in cgpa if x > 7]
print(cgpa)

