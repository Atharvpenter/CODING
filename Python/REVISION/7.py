# to avoid repeatation in py we use def function
def cal(x,y):
    print(x +y)
    print(x - y)
cal(1,3)

# string
a = "string"
print(type(a))

# tuple
a1 = ("qq","ee","rr")
print(type(a1))

# list
a2 = [11,33]
print(type(a2))

# set
a3 ={11,22}
print(type(a3))

# dictionary
info ={
    "fn":"atarh"
}
print(type(info))

# using range function
# print table of 3 using range function
for x in range(3,33,3):
    print(x)
    
# print it in reverse
for x in range(30,2,-3):
    print(x)

# using break statement
for x in range(1,9):
    if(x == 7):
        break
    print(x)
    
for x in range(1,9):
    if(x == 6):
        continue
    print(x)

# list comprehension
# print age using list comprehension
birthyear = [1999,2000,2001]
age = [2025 - x for x in birthyear]
print(age)

# print odd even numbers using list comprehension
num = [1,23,56,56,97,65,24,67,77,91]
e = [x for x in num if x % 2 == 0 ]
o = [x for x in num if x % 2 != 0]
print(e)
print(o)

# class 
class person:
    # constructor
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    # method
    def displayName(self):
            print(self.firstname + self.lastname)
atharv = person("atharv"," penter")
atharv.displayName()

# change values
atharv.firstname = ("anjali")
atharv.displayName()

# inheritance
# single level
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
atharv1 = teacher("atharv"," penter", 10000)
print(atharv1)

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
atharv2 = son("narayan"," penter","avinash","atharv")
atharv2.displayFname()
atharv2.displayGname()
atharv2.displaySname()

# multiple inheritance
# class father:
#     def __init__(self,fn,ln):
#         self.firstname = fn
#         self.lastname = ln
#     def displayFame(self):
#         print(self.firstname + self.lastname)
# class mother(father):
#     def __init__(self,fn,ln,mfn):
#         super().__init__(fn,ln)
#         self.mname = mfn
#     def displayMname(self):
#         print(self.mname + self.lastname)
# class son(father,mother):
#     def __init__(self,fn,ln,mfn,sfn):
#         super().__init__(fn,ln,mfn)
#         self.sname = sfn
#     def displaySname(self):
#         print(self.sname + self.lastname)
# atharv3 = son("avinash"," penter","chhaya","atharv")
