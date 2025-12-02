# string 
a = "atharv"
print(type(a))

# dictionary
info ={
    "fn":'atharv'
}
print(type(info))

# set
a1 = {10,20,30}
print(type(a1))

# for loop
# print table of 2 using range
for x in range(2,22,2):
    print(x)
    
# reverse
for x in range(20,1,-2):
    print(x)
    
# 1 to 9 except 7
for x in range (1,10):
    if(x == 7):
        break
    print(x)

for x in range(1,10):
    if(x == 7):
        continue
    print(x)

# age using list comprehesion
birthyear = [2006,2007,2000,2001,1999,2003]
age = [2025 - x for x in birthyear]
print(age)

# above 30
marks = [24,30,32,44,50,39,88,78,65,62,63]
above30 = [x for x in marks if x > 30]
print(above30)

# class
class person:
    # constructor
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
atharv = person("atharv"," penter")
atharv.displayName()

# class using class variable
class name:
    # class variable
    country = "India"
    # contructor
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
    @classmethod
    def changeCountry(cls):
        cls.country = "Bharat"
atharv1 = name("atharv"," penter")
atharv1.displayName()
print(atharv1.country)
print(atharv1.changeCountry())

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
    def displaySname(self):
        print(self.salary)
atharv2 = teacher("atharv"," penter", 10000)
atharv2.displayName()
atharv2.displaySname()

# multilevel inheritance
class grandfather:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
class father(grandfather):
    def __init__(self,fn,ln,ffn):
        super(). __init__(fn,ln)
        self.fname = ffn
    def displayFname(self):
        print(self.fname + self.lastname)
class son(father):
    def __init__(self,fn,ln,sfn,ffn):
        super().__init__(fn,ln,ffn)
        self.Sname = sfn
    def displaySname(self):
        print(self.Sname + self.lastname)
atharv3 = son("Narayan"," Penter","Avinash","Atharv")
atharv3.displayName()
atharv3.displayFname()
atharv3.displaySname()

# multiple inheritance
# class father:
#     def __init__(self,fn,ln):
#         self.firstname = fn
#         self.lastname = ln
#     def displayFname(self):
#         print(self.firstname + self.lastname)
# class mother:
#     def __init__(self,fn,ln):
#         self.firstname = fn
#         self.lastname = ln
#     def displayMname(self):
#         print(self.firstname + self.lastname)
# class son(father,mother):
#     def __init__(self,fn,ln,sfn):
#         super().__init__(fn,ln)
#         self.sname = sfn
#     def displaySname(self):
#         print(self.sname + self.lastname)
# # atharv4 = son("Avinash"," Penter","Chhaya","Atharv")
# # atharv4.displayFname()

