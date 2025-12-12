# string
a = "atharv"
print(type(a))

# set
a = {'atharv'}
print(type(a))

# list
a = ['at','aa']
print(type(a))

# many repeatation in code then use def function to reduce repeatations
def addition(x,y):
    print(x+y)
addition(3,9)

# using range
# print table of 2 using range
for x in range(2,22,2):
    print(x)
    
# print table of 2 in reverse
for x in range(20,1,-2):
    print(x)
    
# using break statement in loops
for x in range(1,9):
    if(x==7):
        break
    print(x)

# using continue statement in loops
for x in range(1,9):
    if(x==6):
        continue
    print(x)
    
# print age using loops# 
# by = [1999,2000,2001,2002,2003]
# age = []
# for x in by:
#     age = 2025 - x
#     by.append(age)
# print(age)
    
# dictionary
info ={
    "fn":"atharv",
    "ln":"penter"
}
print(type(info))
print(info)

# changing elements in dictionary
info["fn"] = "anjali"
print(info)

# list comprehension
# print ages
byear = [1998,1999,2000,2001,2002,2003,2004]
age = [2025 - x for x in byear]
print(age)

# print above30 & below30 marks
marks = [99,25,33,45,69,7,12,65,66,54,78,95,45,55]
above30 = [x for x in marks if x > 30]
below30 = [x for x in marks if x < 30]
print(above30)
print(below30)

# class 
class person:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
atharv = person("atharv"," penter")
atharv.displayName()

# using class variable
class name:
    country = "india"
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
    @classmethod
    def changeCountry(cls):
        cls.country = "bharat"
ap = name("Atharv"," Penter")
ap.displayName()
print(name.country)
print(name.changeCountry)

# inheritance
# single level inheritance
class student:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
class teacher(student):
    def __init__(self,fn,ln,sl):
        super().__init__(fn,ln)
        self.salary = sl
    def displaySalary(self):
        print(self.salary)
aap = teacher("atharv "," penter",111111)
aap.displayName()
aap.displaySalary()

# multilevel inheritance
class GrandeFather:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayGname(self):
        print(self.firstname + self.lastname)
class Father(GrandeFather):
    def __init__(self,fn,ln,ffn):
        super().__init__(fn,ln)
        self.fname = ffn
    def displayFname(self):
        print(self.fname + self.lastname)
class Son(Father):
    def __init__(self,fn,ln,ffn,sfn):
        super().__init__(fn,ln,ffn)
        self.sname = sfn
    def displaySname(self):
        print(self.sname + self.lastname)
app = Son("Narayan"," Penter","Avinash","Atharv")
app.displayGname()
app.displayFname()
app.displaySname()

# multiple inheritance
class father:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayFname(self):
        print(self.firstname + self.lastname)
class mother:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayMname(self):
        print(self.firstname + self.lastname)
class son(father,mother):
    def __init__(self,fn,ln,sfn,ffn,mfn):
        super().__init__(fn,ln,ffn,mfn)
        self.sname = sfn
    def displaySname(self):
        print(self.sname + self.lastname)
anp = son("Avinash"," Penter","Chhaya","Atharv")
anp.displayFname()
anp.displayMname()
anp.displaySname()