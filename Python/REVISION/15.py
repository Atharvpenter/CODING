# string
a = "atharv"
print(type(a))

# list
a1 = ["atharv","OM"]
print(type(a1))

# set 
a2 = {11,22,33,44,55}
print(type(a2))

# dictionary
info = {
    "fn":"atharv"
}
print(type(info))

# usinf def function
def cal(x,y):
    print(x + y)
cal(4,4)

# using range function
# print table of 4 using range function
for x in range(4,44,4):
    print(x)
    
# print table of 4 in reverse
for x in range(40,3,-4):
    print(x)
    
# using break and continue statements in range function
# print 1 to 10 upto 6
for x in range(1,11):
    if(x==7):
        break
    print(x)

# print 1 to 10 except 6
for x in range(1,11):
    if(x == 6):
        continue
    print(x)
    
# list comprehension
# expression : loop : condition
# print age using list comprehension
birthyear = [1998,1999,2000,2001,2002,2003,2004,2005,2006]
age = [2025 - x for x in birthyear]
print(age)

# class
class name:
    # constructor
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
atharv = name("Atharv"," Penter")
atharv.displayName()

# using class variable in class
class name1:
    country = "INDIA"
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
    @classmethod
    def ChangeCountry(cls):
        cls.country = None
atharv1 = name1("Anjali"," Penter")
atharv1.displayName()
print(atharv1.country)
print(atharv1.ChangeCountry())

# inheritance
# single level inheritance
class father:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayFname(self):
        print(self.firstname + self.lastname)
class son(father):
    def __init__(self,fn,ln,sfn):
        super().__init__(fn,ln)
        self.sname = sfn
    def displaySname(self):
        print(self.sname + self.lastname)
atharv2 = son("Avinash"," Penter","Atharv")
atharv2.displayFname()
atharv2.displaySname()

# multi level inheritance
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
atharv3 = son("Narayan"," Penter","Avinash","Atharv")
atharv3.displayGname()
atharv3.displayFname()
atharv3.displaySname()