# to avoid repeatations in py we use ->
def cal(x,y):
    print(x+y)
cal(12,3)

# Using Range function ->
# Print table of 3
for x in range(3,33,3):
    print(x)

# print table of 3 in reverse ->
for x in range(33,2,-3):
    print(x)
    
# using break statements in range ->
for x in range(1,9):
    if(x==5):
        break
    print(x)

# using continue statements in range ->
for x in range(1,9):
    if(x==5):
        continue
    print(x)
    
# string -> anything inside single or double quotes is a string
a = 'atharv'
print(type(a))

# calculate length
print(len(a))

# list -> anything inside square bracket is a list
a1 = [11,22,33]
print(type(a1))

# dictionary -> it is used to store key value pairs.
info = {
    "fn":"atharv",
    "ln":"penter",
    "age":22
}
print(info)
print(type(info))

# update dictionary ->
info["fn"] = 'anjali'
print(info)

# using range in dictionary ->
# keys
for x in info.keys():
    print(x)
    
# values
for x in info.values():
    print(x)
    
# set -> anything inside curly bracket is a set. unordered collection of elements.
set = {11,22,33}
print(set)
print(type(set))

# operations on sets ->
# intersection -> same
seta = {1,2,3,4}
setb = {2,3,6,7}
setc = seta.intersection(setb)
print(setc)

# difference -> not same in first set
setd = {1,2,3,4}
sete = {2,3,6,7}
setf = setd.difference(sete)
setg = sete.difference(setd)
print(setf)
print(setg)

# Symmetric difference ->
seth = {1,2,3,4}
seti = {2,3,6,7}
setj = seth.difference(seti)
print(setj)

# print age using loops ->
years = [1999,2000,2001,1998,1888,2003]
birthyear = []
for x in years:
    age = 2025-x
    birthyear.append(age)
    print(birthyear)

# calculate the sum of elements using loops ->
sum = [10,40,10]
total = 0
for x in sum:
    total = total + x
    print(total)

# list comprehension -->
# expression : loops : statements
# calculate age using list comprehension
year = [1999,2000,2001,1998,1888,2003]
byear = [2025 - x for x in year]
print(byear)

# calculate marks above50 using list comprehension ->
marks = [56,77,89,33,45,62,11,45,66]
above50 = [x for x in marks if x > 50]
print(above50)

# find odd even numbers using list comprehension ->
num = [1,2,3,4,5,6,7,8,9,10]
e = [x for x in num if x % 2 == 0]
o = [x for x in num if x % 2 != 0]
print(e)
print(o)

# print table of 2 using list comprehension ->
num = [1,2,3,4,5,6,7,8,9,10]
table = [x*2 for x in num]
print(num)

# class -> blueprint of creating objects.
class person :
    # constructor
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
        
    def displayName(self):
        print(self.firstname + self.lastname)

atharv = person("atharv"," penter")
atharv.displayName()

# using class variable in class ->
class PersonB:
    #class variable
    country = "India"
    #contructor
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    #methods,
    def displayName(self):
        print(self.firstname + self.lastname)
    # If i have to change country name of the class variable,
    @classmethod
    def changeCountry(cls):
        cls.country = "INDIA"
            
atharvB= PersonB("Atharv"," Penter")
atharvB.displayName()
print(atharvB.firstname)
print(atharvB.country)
PersonB.changeCountry()
print(atharvB.country)

# inheritance ->
# single-level inheritance ->
class student:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)

class teacher:
    def __init__(self,fn,ln,sl):
        super().__init__(fn,ln)
        self.salary = sl
    def displaySalary(self):
        print(self.salary)

atharv1 = ("atharv"," penter", 10000)
print(atharv1)

# multi-level inheritance ->
class GrandFather:
    #constructor
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
        
    def displayGName(self):
        print(self.firstname + self.lastname)
        
class Father(GrandFather):
    def __init__(self,fn,ln,ffn):
        super().__init__(fn,ln)
        self.Fname = ffn
    
    def displayFName(self):
        print(self.Fname + self.lastname)
        
class Son(Father):
    def __init__(self,fn,ln,ffn,sfn):
        super().__init__(fn,ln,sfn)
        self.sname = sfn
        
    def displaySName(self):
        print(self.sname + self.lastname)
        
atharv1 = Son("Narayan"," Penter"," Avinash"," Atharv")
atharv1.displayGName()
atharv1.displayFName()
atharv1.displaySName()

# multiple inheritance ->
class Father:
    #constructor
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
        
    def displayFname(self):
        print(self.firstname + self.lastname)
        
class Mother:
    def __init__(self,fn,ln,mfn):
        super().__init__(fn,ln)
        self.mname = mfn
    
    def displayMname(self):
        print(self.mname + self.lastname)

class Son(Father,Mother):
    def __init__(self,fn,ln,sfn):
        super().__init__(fn,ln,sfn)
        self.sname = sfn
    
    def displaySname(self):
        print(self.sname + self.lastname)
        
atharv2 = Son("Avinash","Penter","Chhaya","Atharv")
print(atharv2)
atharv2.displayFname()
atharv2.displayMname()
atharv2.displaySname()