# to reduce repeatations in code we use def function
def cal(x,y):
    print(x+y)
    print(x-y)
    print(x*y)
    print(x%y)
cal(7,4)

# string 
a = "atharv"
print(type(a))

# list 
a1 = ["atharv"]
print(type(a1))

# dictionary
info = {
    "fn":"atharv"
}
print(type(info))

# Using range function
# print table of 3 using range function
for x in range(3,33,3):
    print(x)
    
# print table of 3 in reverse
for x in range(30,2,-3):
    print(x)

# Using break and continue statements in range function
# print 1 to 8 upto 3
for x in range(1,9):
    if(x==4):
        break
    print(x)

# print 1 to 8 except 3
for x in range(1,9):
    if(x==3):
        continue
    print(x)
    
# list comprehension
# Calculate age using list comprehension
birthyear = [1999,2000,2001,2002,2003,2004]
age = [2025 - x for x in birthyear]
print(age)

# print odd and even numbers using list comprehension
numbers = [1,2,3,4,5,6,7,8,9,10]
even = [x for x in numbers if x % 2 == 0]
odd = [x for x in numbers if x % 2 != 0]
print(even)
print(odd)

# overriding
class cal():
    def add(self,a=0, b=0, c=0):
        return a+b+c
a = cal()
print(a.add(1))
print(a.add(3,4))
print(a.add(2,4,5))

# overloading
class animal():
    def sound(self):
        print("Animal sounds")
class dog(animal):
    def sound(self):
        print("Bark")
class cat(animal):
    def sound(self):
        print("Meow")
class rabbit(animal):
    pass
a=animal()
b=dog()
c=cat()
d=rabbit()
for animal in (a,b,c,d):
    animal.sound()
    
# duck typing - polymorphism
class duck:
    def speak(self):
        return "Quack Quack"
class human:
    def speak(self):
        return "Talk"
class cat:
    def speak(self):
        return "Meow Meow"
def call_speak(obj):
    print(obj.speak())
a = duck()
b = human()
c = cat()
call_speak(a)
call_speak(b)
call_speak(c)

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

# decorator
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper
@my_decorator
def say_hello():
    print("Hello")
say_hello()

# class
class person:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
a = person("atharv"," penter")
a.displayName()

# class variable
class name:
    country = "India"
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
    @classmethod
    def ChangeCountry(cls):
        cls.country = "Bharat"
a1 = name("Anjali"," Penter")
a1.displayName()
print(a1.country)
a1.ChangeCountry()
print(a1.country)

# inheritance
# single level inheritance
class father:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
class son(father):
    def __init__(self,fn,ln,sfn):
        super().__init__(fn,ln)
        self.sname = sfn
    def displaySname(self):
        print(self.sname + self.lastname)
ap = son("Avinash"," Penter","Atharv")
ap.displayName()
ap.displaySname()

# multi level inheritance
# class grandfather:
#     def __init__(self,fn,ln):
#         self.firstname = fn
#         self.lastname = ln
#     def displayGname(self):
#         print(self.firstname + self.lastname)
# class father(grandfather):
#     def __init__(self,fn,ln,ffn):
#         super().__init__(fn,ln)
#         self.fname = ffn
#     def displayFname(self):
#         print(self.fname + self.lastname)
# class son(father):
#     def __init__(self,fn,ln,ffn,sfn):
#         super().__init__(fn,ln,ffn)
#         self.sname = sfn
#     def displaySname(self):
#         print(self.sname + self.lastname)
# ap4 = son("Narayan"," Penter","Avinash","Atharv")
# ap4.displayGname()
# ap4.displayFname()
# ap4.displaySname()

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
    def __init__(self,fn,ln,sfn):
        super().__init__(fn,ln)
        self.sname = sfn
    def displaySname(self):
        print(self.sname + self.lastname)
ap5 = son("Chhaya"," Penter","Atharv")
ap5.displayMname()
ap5.displaySname()