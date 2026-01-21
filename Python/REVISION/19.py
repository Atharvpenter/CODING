# string
a = "atharv"
print(type(a))

# list
a1 = ["atharv","penter"]
print(type(a1))

# set 
# types of set are transection,difference,symmetric difference
a2 = {11,22,33,44,55}
print(type(a2))

# dictionary
a3 = {
    "fn":"atharv"
}
print(type(a3))

# using def function to reduce code repeatations
def cal(x,y):
    print(x+y)
    print(x-y)
cal(4,6)

# Using Range function
# print 1 to 10 using range function
for x in range(1,11):
    print(x)

# print table of 2 using range function
for x in range(2,22,2):
    print(x)
    
# Using Break and conditional statements
for x in range(2,22,2):
    if(x==12):
        break
    print(x)

for x in range(2,22,2):
    if(x==14):
        continue
    print(x)

# print table of 2 in reverse
for x in range(20,1,-2):
    print(x)
    
# list comprehension
# calculate age using list comprehension
birthday = [1998,1999,2000,2001,2002,2003,2004]
age = [2025 - x for x in birthday]
print(age)

# print odd and even using list comprehension
num = [1,2,3,4,5,6,7,8,9]
even = [x for x in num if x % 2 == 0]
odd = [x for x in num if x % 2 != 0]
print(even)
print(odd)

# overriding
class cal():
    def add(self,a=0,b=0,c=0):
        return a+b+c
a = cal()
print(a.add(1))
print(a.add(1,2))
print(a.add(1,2,3))

# overloading
class animal():
    def sound(self):
        print("Animal Sounds")
class dog(animal):
    def sound(self):
        print("Bark")
class cat(animal):
    def sound(self):
        print("Meow")
class rabbit(animal):
    pass
a = animal()
b = dog()
c = cat()
d = rabbit()
for animal in (a,b,c,d):
    animal.sound()

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
class name:
    country = "INDIA"
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
    @classmethod
    def ChangeCountry(cls):
        cls.country = "BHARAT"
ap1 = name("Anjali"," Penter")
ap1.displayName()
print(ap1.country)
ap1.ChangeCountry()
print(ap1.country)

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

# decorators
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