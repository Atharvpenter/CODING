# string 
a = "atharv"
print(type(a))

# list
a1 = ["atharv","Kunal"]
print(type(a1))

# set
a2 = {11,22,33,44,55}
print(type(a2))

# dictionary
a3 = {
    "fn":"atharv"
}
print(type(a3))

# Using DEF function to reduce too many codes
def cal(x,y):
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
cal(4,8)

# Using Range function
# print table of 9 using range function
for x in range(9,99,9):
    print(x)
    
# print table of 9 in reverse
for x in range(90,8,-9):
    print(x)
    
# Using break and continue statements in range function
# Using break statement
# print 1 to 10 upto 8
for x in range(1,11):
    if(x == 9):
        break
    print(x)
    
# Using continue statement
for x in range(1,11):
    if(x == 8):
        continue
    print(x)
    
# set has four types 1.intersection 2.update_intersection 3.difference 4.symmetric_difference

# Using list comprehension
# expression : loop : statement
# print age using list comprehension
birthyear = [1999,2000,2001,2003,2004,2005,2006]
age = [2025 - x for x in birthyear]
print(age)

# print above 40 marks using list comprehension
marks = [55,77,10,23,6,97,22,35,100,46,29,76]
above40 = [x for x in marks if x > 40]
print(above40)

# print even odd numbers using list comprehension
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even = [x for x in numbers if x % 2 == 0]
odd = [x for x in numbers if x % 2 != 0]
print(even)
print(odd)

# class
class person:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
ap = person("Atharv"," Penter")
ap.displayName()

# using class variable in class
class Person:
    country = "INDIA"
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
    @classmethod
    def changeCountry(cls):
        cls.country = "None"
ap1 = Person("Anjali"," Penter")
ap1.displayName()
print(ap1.country)
print(ap1.changeCountry())

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
ap2 = son("Avinash"," Penter","Atharv")
ap2.displayFname()
ap2.displaySname()

# multi level inheritance
# class Grandfather:
#     def __init__(self,fn,ln):
#         self.firstname = fn
#         self.lastname = ln
#     def displayGname(self):
#         print(self.firstname + self.lastname)
# class Father(Grandfather):
#     def __init__(self,fn,ln,ffn):
#         super().__init__(fn,ln)
#         self.fname = ffn
#     def displayFname(self):
#         print(self.fname + self.lastname)
# class Son(Father):
#     def __init__(self,fn,ln,ffn,sfn):
#         super().__init__(fn,ln,ffn)
#         self.sname = sfn
#     def displaySname(self):
#         print(self.sname + self.lastname)
# atharv3 = Son("Narayan"," Penter","Avinash","Atharv")
# atharv3.displayGname()
# atharv3.displayFname()
# atharv3.displaySname()

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
# # ap4 = son("Chhaya"," Penter","Atharv")
# # ap4.displaySname()
# ap4.displayMname()

# overloading
class cal:
    def add(self,a = 0, b = 0, c = 0):
        return a + b + c
a = cal()
print(a.add(1))
print(a.add(3,9))
print(a.add(9,4,1))

# overriding
class animal:
    def sound(self):
        print("animals sounds")
class dog(animal):
    def sound(self):
        print("Bark")
class cat(animal):
    def sound(self):
        print("Meow")
a = dog()
b = cat()
for animal in (a,b):
    animal.sound
    
# duck typing
class duck:
    def speak(self):
        print("quack")
class dog:
    def speak(self):
        print("Bark")
class cat:
    def speak(self):
        print("Meow")
def call_speak(obj):
    print(obj.speak())
z = duck()
z1 = dog()
z2 = cat()
call_speak(z)
call_speak(z1)
call_speak(z2)

# generator
def get_number():
    yield 1
    yield 2 
    yield 3
    yield 4
gen = get_number()
print(gen)
e = next(gen)
print(e)
print(next(gen))
print(next(gen))
print(next(gen))

# decorate
def my_decorate(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper
@my_decorate
def say_hello():
    print("Hello")
say_hello()