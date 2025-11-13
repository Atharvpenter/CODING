# string
a = 'atharv'
print(type(a))

# list 
a1 = [11,22,33]
print(type(a1))

# set
a3 = {11,22,33}
print(type(a3))

# dictionary
info = {
    "fn":"atharv"
}
print(type(info))

# if there is to many repeatations in python the we use DEF function
def Cal(x,y):
    print(x+y)
    print(x-y)
    print(x*y)
Cal(4,8)

# using range function
# print 1 to 6 using range function
for x in range(1,7):
    print(x)

# print table of 2
for x in range(2,22,2):
    print(x)
    
# print table of 2 in reverse
for x in range(18,1,-2):
    print(x)

# using break and continue statements in range function
# print 1 to 9 except 4
for x in range(1,10):
    if(x == 4):
        continue
    print(x)

# print 1 to 9 but stop at 6
for x in range(1,10):
    if(x == 7):
        break
    print(x)
    
# change elements in a dictionary
info1 = {
    "fn":"atharv"
}
print(info1)
info1["fn"] = "anjali"
print(info1)

# different methods in sets
# intersection
set1 = {1,2,3,4,5}
set2 = {3,4,2,6,8}
set3 = set1.intersection(set2)
print(set3)

# difference
set4 = {5,6,7,8,9}
set5 = {1,3,4,5,9}
set6 = set4.difference(set5)
print(set6)

# list comprehension ->
# expression loop condition
# print age using list comprehension
birthyear = [1998,1999,2000,2001,2002,2003]
age = [2025 - x for x in birthyear]
print(age)

# print marks above 30
marks = [40,55,22,45,67,77]
above30 = [x for x in marks if x > 30]
print(above30)

# class->
class person:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
atharv = person("atharv"," penter")
atharv.displayName()

# use class variable 
class name:
    # class variable
    country = "INDIA"
    # constructor
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
    @classmethod
    def changeCountry(cls):
        cls.country = "BHARAT"
atharv1 = name("ram","sham")
atharv1.displayName()
print(name.country)
print(name.changeCountry())

# inheritance
# single-level inheritance
class student:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displaySname(self):
        print(self.firstname + self.lastname)
class teacher(student):
    def __init__(self,fn,ln,sl):
        super().__init__(fn,ln)
        self.salary = sl
    def displaySSname(self):
        print(self.salary)
atharv2 = ("atharv"," Penter",100000)
print(atharv2)

# multi-level inheritance
# multiple inheritance
