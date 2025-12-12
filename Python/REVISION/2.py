# Using for loops ->
# print table of 5
for x in range(5,55,5):
    print(x)

# print table of 5 in reverse 
for x1 in range(55,4,-5):
    print(x1)
    
# Using while loops
for x2 in range(1,9):
    if(x == 5):
        break
    print(x2)
    
# list ->
a = [11,222,23]
print(type(a))

# dictionary ->
info = {
    "fn":"atharv",
    "ln":"penter"
}
print(info)
print(type(info))

# Using loops in dictionary ->
info1 = {
    "fn":"atharv",
    "ln":"penter"
}
for x4 in info1.keys():
    print(x4)
    
for x5 in info.values():
    print(x5)

# Using set ->
set ={11,22,33}
print(type(set))

# different types of methods in set ->
# intersection -> print same elements 
setA = {1,2,3,4}
setB = {4,5,6,1}
setC = setA.intersection(setB)
print(setC)

# difference 
setD = {1,5,6}
setE = {2,6,8}
setF = setD.difference(setE)
print(setF)

# calculate age ->
year = [1998,2004,1889,1999,2001,2003]
byear = []
for x in year:
    age = 2025 - x
    byear.append(age)
    print(byear)
    
# calculate above 40 marks ->
marks = [19,25,36,40,98,75,46,81,44,22]
above40 = []
for x in marks:
    above40 = x < 40
    print(above40)
    
# Calculate sum ->
sum = [10,20,30]
total = 0
for x in sum:
    total = total + x
    print(total)
    
# List comprehension ->
# expression : loop : conditions
years = [1998,2004,1889,1999,2001,2003]
birthyear = [2025 - x for x in years]
print(birthyear)

# calculate above40 marks ->
mark = [19,25,36,40,98,75,46,81,44,22]
abovee40 = [x for x in mark if x < 40]
print(abovee40)

# find odd and even ->
num = [1,2,3,4,5,6,7,8,9]
e = [x for x in num if x % 2 == 0]
o = [x for x in num if x % 2 != 0]
print(e)
print(o)

# Class ->
class person :
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

# using class variables ->
class name:
    # class variable
    country = "India"
    # constructor
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
        
    def displayName(self):
        print(self.firstname + self.lastname)
    
    @classmethod
    def changeCountry(cls):
        cls.country = "bharat"

atharv = name("atharv"," penter")
atharv.displayName()
print(atharv.country)
atharv.changeCountry()

# inheritance ->
# 1. single - level inheritance ->
# class Student:

#      def __init__(self,fn,ln):
#          self.firstName = fn 
#          self.lastName = ln

#      def displayName(self):
#          print(self.firstName + self.lastName)

# class Teacher(Student):
    
#      def __init__(self, fn, ln,sl):
#          super().__init__(fn, ln)
#          self.salary = sl

#      def displaySalary(self):
#          print(self.salary)
# atharv1  = Teacher("atharv"," penter",10000)
# print(atharv1)

# # multi - level inheritance ->
# class grandfather:
#     def __init__(self,fn,ln):
#         self.firstname = fn
#         self.lastname = ln
#     def displayGname(self):
#         print(self.firstname + self.lastname)

# class father:
#     def __init__(self,fn,ln,ffn):
#         super().__init__(fn,ln)
#         self.fname = ffn
#     def displayFname(self):
#         print(self.fname + self.lastname)

# class son:
#     def __init__(self,fn,ln,sfn,ffn):
#         super().__init__(fn,ln,ffn)
#         self.sname = sfn
#     def displaySname(self):
#         print(self.sname + self.lastname)
# atharv2 = ("Narayan"," Penter"," Avinash"," Atharv")

# # multiple inheritance ->
# class father:
#     def __init__(self,fn,ln):
#         self.firstname = fn
#         self.lastname = ln
        
#     def displayName(self):
#         print(self.firstname + self.lastname)
# class mother(father):
#     def __init__(self,fn,ln,mfn):
#         super().__init__(fn,ln)
#         self.mname = mfn
#     def displayMname(self):
#         print(self.mname + self.lastname)

# class son(father,mother):
#     def __init__(self,fn,ln,mfn,sfn):
#         super().__init__(fn,ln,mfn,sfn)
#         self.sname = sfn
#     def displaySname(self):
#         print(self.sname + self.lastname)
# atharv3 = ("avinash","penter","chhaya","atharv")
# atharv3.displayMname()

# abstraction ->
from abc import ABC,abstractmethod
class myclass(ABC):
    @abstractmethod
    def calculate(self,x):
        pass
class subclass(myclass):
    def calculate(self, x):
        return x *x*x
    def one(self):
        print("one is called....")
f = myclass
# f.calculate()
f.one()















