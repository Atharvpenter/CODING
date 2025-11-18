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
demo = {
    "fn":"atharv",
    "ln":"penter"
}
print(type(demo))

# if there is repeatation in the program we use DEF function 
def cal(x,y):
    print(x+y)
    print(x-y)
cal(1,9)

# Range
# print table of 2 using range
for x in range(2,22,2):
    print(x)
    
# print table of 2 in reverse
for x in range(18,1,-2):
    print(x)
    
# using break and continue statements in range
for x in range(1,10):
    if(x == 6):
        break
    print(x)
    
for x in range(1,10):
    if(x == 6):
        continue
    print(x)

# set has different methods in it
# intersection
st1 = {1,2,6,5}
st2 = {2,6,5,7,8}
st3 = st1.intersection(st2)
print(st3)

# difference
st1 = {1,2,6,5}
st2 = {2,6,5,7,8}
st3 = st1.difference(st2)
print(st3)

# list comprehension
# print age using list comprehension
byear = [2000,2001,2002,2003,2004,2005,2006]
age = [2025 - x for x in byear]
print(age)

# class
class student:
    # constructor
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
atharv = student("atharv"," penter")
atharv.displayName()
print(type(atharv))

# using class variable 
class me:
    country = "india"
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
    @classmethod
    def changeCounty(cls):
        cls.country = "bharat"
atharv1 = me("atharv"," Penter")
print(atharv1.country)
print(atharv1.changeCounty)

# inheritance 
# single line inheritance
class std:
    def __init__(self,fn,ln):
        self.firstaname = fn
        self.lastname = ln
    def displaySnamr(self):
        print(self.firstaname + self.lastname)
class teach(std):
    def __init__(self,fn,ln,sl):
        super().__init__(fn,ln)
        self.salary = sl
    def displayTname(self):
        print(self.salary)
atharv2 = teach("atharv"," penter", 10000)
print(atharv2)

    
