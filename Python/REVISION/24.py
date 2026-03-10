# string
a = "ath"
print(type(a))

# set 
a1 = {11,22,33}
print(type(a1))

# list
a2 = ["ar"]
print(type(a2))

# dictionary
info = {
    "fn":"ar"
}
print(type(info))

# range
# print 1 to 10
for x in range(1,11):
    print(x)
    
# print table of 2
for x in range(2,22,2):
    print(x)
    
for x in range(20,1,-2):
    print(x)
    
# using break and continue
for x in range(1,10):
    if(x==5):
        break
    print(x)
    
for x in range(1,10):
    if(x==5):
        continue
    print(x)
    
# list comprehension
birthyear = [1998,1999,2000,2001,2002,2003]
age = [2025 - x for x in birthyear]
print(age)

# class
class person:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
ap = person("atharv"," Penter")
ap.displayName()

# using class variable
class Person:
    country ="india"
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
    @classmethod
    def changeCountry(cls):
        cls.country = "bharat"
ap1 = Person("atharv"," Penter")
ap1.displayName()
print(ap1.country)
ap1.changeCountry()
print(ap1.country)

# overloading
class cal():
    def add(self,a=0,b=0,c=0):
        return a+b+c
a = cal()
print(a.add(1))
print(a.add(1,2))
print(a.add(1,2,3))

# overriding
class animal():
    def sound(self):
        print("Basic sounds...")
class dog(animal):
    def sound(self):
        print("Bark")
class cat(animal):
    def sound(self):
        print("Meow")
a = animal()
b = dog()
c = cat()
for animal in (a,b,c):
    animal.sound
    
# duck typing
class duck():
    def speak(self):
        print("quack")
class dog():
    def speak(self):
        print("BArk")
class cat():
    def speak(self):
        print("meow")
def call_speak(obj):
    obj.speak()
aa = duck()
bb = dog()
cc = cat()

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
ap2 = son("Avinash"," Penter","Atharv")
ap2.displayName()
ap2.displaySname()

# multi level inheritance
class grandfather:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
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
ap3 = son("Narayan"," Penter","Avinash","Atharv")
ap3.displayName()
ap3.displayFname()
ap3.displaySname()

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
ap4 = son("Chhaya"," Penter","Atharv")
ap4.displayMname()
ap4.displaySname()

# generators
def get_numbers():
    yield 1
    yield 2
    yield 3
    yield 4
gen = get_numbers
print(gen)
e = next(gen)
print(e)
print(next(gen))
print(next(gen))
print(next(gen))

# decorators
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return
@my_decorator
def say_hello():
    print("Hello")
say_hello