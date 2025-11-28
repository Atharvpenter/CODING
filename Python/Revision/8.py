# string
a = "atharv"
print(type(a))

# list
a1 = ["atharv","ram","laxman"]
print(type(a1))

# dictionary
a2 = {
    "fn":"ap"
}
print(type(a2))

# set
a4 = {11,22,33,44}
print(type(a4))

# different methods in set
# 1. intersection
seta = {1,2,3,4,5,6}
setb = {2,8,6,5,7,9}
setc = seta.intersection(setb)
print(setc)

# 2.difference
setd = {1,2,3,4,5,6}
sete = {2,8,6,5,7,9}
setf = setd.intersection(sete)
print(setf)

# using range
# print table of 2 using range
for x in range(2,22,2):
    print(x)
    
# print table of 2 in reverse
for x1 in range(20,1,-2):
    print(x1)

# using break statement in range
# print 1 to 9 upto 6
for x in range(1,10):
    if(x == 7):
        break
    print(x)
    
# using continue statement in range
# print 1 to 9 except 6
for x in range(1,10):
    if(x == 6):
        continue
    print(x)

# list comprehension
# expression : loop : statement
# print age using list comprehension
birthyear = [1998,1999,2000,2001,2002,2003,2004,2005]
age = [2025 - x for x in birthyear]
print(age)

# print above 40 marks using list comprehension
marks = [40,39,25,87,48,55,79,12,99,23,41,65,91]
above40 = [x for x in marks if x > 40]
print(above40)

# print odd and even numbers using list comprehension
num = [1,2,3,4,5,6,7,8,9,10,11,12]
odd = [x for x in num if x % 2 != 0]
even = [x for x in num if x % 2 == 0]
print(even)
print(odd)

# class 
class person:
    # constructor
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    # methods
    def displayName(self):
        print(self.firstname + self.lastname)
atharv = person("atharv"," penter")
atharv.displayName()

# using class variables
class Person:
    country = "India"
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
    @classmethod
    def changeClass(cls):
        cls.country = "Bharat"
atharv1 = Person("atharv"," Penter")
atharv1.displayName()
print(atharv1.country)
print(atharv1.changeClass)

# inheritance
# 1. single level inheritance
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
    def displaysname(self):
        print(self.salary)
atharv2 = teacher("atharv"," penter", 15000)
atharv2.displaySname()
atharv2.displaysname()

# multi - level inheritance
class GrandFather:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayGname(self):
        print(self.firstname + self.lastname)
class Father(GrandFather):
    def __init__(self,fn,ln,ffn):
        super().__init__(fn,ln)
        self.fname = ffn
    def displayFname(self):
        print(self.fname + self.lastname)
class Son(Father):
    def __init__(self,fn,ln,sfn,ffn):
        super().__init__(fn,ln,ffn)
        self.sname = sfn
    def displaySname(self):
        print(self.sname + self.lastname)
atharv3 = Son("Narayan"," Penter","Avinash","Atharv")
atharv3.displayGname()
atharv3.displayFname()
atharv3.displaySname()

# multiple inheritaance
class Mother:
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln
    def displayName(self):
        print("Mother method called")
        print(self.firstName + self.lastName)
class Father:
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln       
    def displayName(self):
        print("Father method called")
        print(self.firstName + self.lastName)
class Son(Father,Mother):
    def __init__(self, fn, ln,ssn):
        super().__init__(fn, ln)
        self.sname = ssn
    def displaySname(self):
        print(self.sname + self.lastName)
atharv4 = Son("Chhaya"," Penter","Atharv")
# atharv4.displayFname()
atharv4.displaySname()
# atharv4.displayMname()

# binary
# to open a file we use
# a = open('file.txt','w')

# # read data we use
# str = input('Enter a text')

# # write data
# a.write(str)

# # close
# a.close()

# binary file creation
# encoding binary files
Reclen = 40
with open("MyBinary.bin","wb") as f:
    n = int(input("How many numbers you want to Print :- "))
    for x in range(n):
        city = input("Enter the name of city :- ")
        city = city + (40 - len(city)) * " "
        city = city.encode()
        f.write(city)
        
# decoding binary files
reclen = 20
with open('cities.bin','w') as f:
    n = int(input('Which record you want to read ?'))
    f.seek(reclen*(n-1))
    str = f.read(reclen)
    str = str.decode()
print(str)