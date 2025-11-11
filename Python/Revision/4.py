# list
a = ['atharv']
print(type(a))

# string
a1 = "atharv"
print(type(a1))

# def function is used to reduce repeatations in python
def cal(x,y):
    print(x+y)
    print(x-y)
    print(x/y)
cal(12,9)        

# Using Range function
# print 1 to 5 using range function
for x in range(1,6):
    print(x)

# print table of 2
for x in range(2,22,2):
    print(x)

# print table of 2 in reverse
for x in range(20,1,-2):
    print(x)
    
# using break statement in range function
for x in range(1,9):
    if(x == 5):
        break
    print(x)

# using continue statement in range function
for x in range(1,9):
    if(x==5):
        continue
    print(x)
    
# dictionary
info = {
    "fn":"atharv",
    "ln":"penter"
}
print(type(info))

# print fn and ln using dictionary
info1 = {
    "fn":"atharv",
    "ln":"penter"
}
print(info["fn"])
print(info["ln"])
print(info1)

# update the value in dictionary
info1["fn"] = "anjali"
print(info1)

# print all keys
for x in info1.keys():
    print(x)
    
# print all values
for x in info1.values():
    print(x)

# set
a3 = {11,33,44}
print(type(a3))

# different methods in set
# 1.intersection
setA = {1,2,3,4}
setB = {4,3,6,7}
setC = setA.intersection(setB)
print(setC)

# 2. difference
setD = {1,2,3,4}
setE = {4,3,6,7}
setF = setD.intersection(setE)
print(setF)

# symmertic difference
setA1 = {1,2,3,4}
setB1 = {4,3,6,7}
setC1 = setA1.intersection(setB1)
print(setC1)

# list comprehension
# expression : loop : condition/statement
# print age using list comprehension
byear = [1999,2000,2001,2002,2003]
age = [2025 - x for x in byear]
print(age)

# simple way to get age using for loop
# by = [1999,2000,2001,2002,2003]
# age = []
# for x in by:
#     age = 2025 - x
#     by.append(age)
# print(age)

# print above 40 marks using list comprehension
marks = [11,45,77,45,33,79]
above40 = [x for x in marks if x > 40]
print(above40)

# class 
class person:
    # constructor
    def __init__(self,fn,ln):
        # properties
        self.firstname = fn
        self.lastname = ln
    
    # methods
    def displayName(self):
        print(self.firstname + self.lastname)
atharv = person("atharv"," penter")
atharv.displayName()

# using class variable in class
class name:
    # class variable
    country = "India"
    # constructor
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
        
    # properties
    def displayName(self):
        print(self.firstname + self.lastname)
    
    @classmethod
    def changeCountry(cls):
        cls.changeCountry = "Bharat"

atharv1 = name("atharv"," penter")
atharv.displayName()

# inherotance
# single level inheritance
class Student:

     def __init__(self,fn,ln):
         self.firstName = fn 
         self.lastName = ln

     def displayName(self):
         print(self.firstName + self.lastName)

class Teacher(Student):
    
     def __init__(self, fn, ln,sl):
         super().__init__(fn, ln)
         self.salary = sl

     def displaySalary(self):
         print(self.salary)
atharv  = Teacher("atharv"," penter",10000)
print(atharv)

# multi-line inheritance
class grandfather:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    
    def displayGname(self):
        print(self.firstname + self.lastname)
        
class father(grandfather):
    def __init__(self,fn,ln,ffn):
        super().__init__(fn,ln)
        self.fname = ffn
        
    def displayFname(self):
         print(self.fname + self.lastname)

class son(father):
    def __init__(self,fn,ln,ffn,sfn):
        super().__init__(fn,ln,ffn)
        self.sname = sfn
        
    def displaySname(self):
        print(self.sname + self.lastname)

atharv3 = son("Narayan","penter","avinash","atharv")
print(atharv3)

# multiple inheritance
# class father:
#     def __init__(self,fn,ln):
#         self.firstname = fn
#         self.lastname = ln
    
#     def displayFname(self):
#         print(self.firstname + self.lastname)
        
# class mother(father):
#     def __init__(self,fn,ln,mfn):
#         super().__init__(fn,ln)
#         self.mname = mfn
        
#     def displayMname(self):
#          print(self.mname + self.lastname)
         
# class son(father,mother):
#     def __init__(self,fn,ln,ffn,sfn):
#         super().__init__(fn,ln,ffn)
#         self.sname = sfn
        
#     def displaySname(self):
#         print(self.sname + self.lastname)
        
# atharv4 = son("avinash","penter","chhaya","atharv")
# print(atharv4)

