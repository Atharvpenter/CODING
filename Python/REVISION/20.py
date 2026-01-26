# string 
a = "atharv"
print(type(a))

# list
a1 = ["atharv","anjali"]
print(type(a1))

# set
a2 = {11,22,33,44}
print(type(a2))

# dictionary
info = {
    "fn":"atharv"
}
print(type(info))

# using def function to avoid repeatations in the code
def cal(x,y):
    print(x+y)
cal(1,9)

# using range function
# print 1 to 10 using range function
for x in range(1,11):
    print(x)
    
# print table of 9
for x in range(9,99,9):
    print(x)

# print table of 9 in reverse
for x in range(90,8,-9):
    print(x)

# using break and continue statements in range
# print 1 to 10 upto 8
for x in range(1,11):
    if(x==9):
        break
    print(x)

# print 1 to 10 except 8
for x in range(1,11):
    if(x==8):
        continue
    print(x)
    
# list comprehension
# calculate age using list comprehension
by = [1998,1999,2000,2001,2002,2003]
age = [2025 - x for x in by]
print(age)

# calculate age using range
by1 = [1998,1999,2000,2001,2002,2003]
age = []
for x in by1:
    a = 2025 - x
    age.append(a)
    print(age)

# print odd n even using list comprehension
number = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even = [ x for x in number if x % 2 == 0]
odd = [ x for x in number if x % 2 != 0]
print(even)
print(odd)

# overriding
class cal():
    def add(self,a=0,b=0,c=0):
        return a+b+c
a = cal()
print(a.add(1))
print(a.add(1,4))
print(a.add(4,5,6))

# overloading
class animal():
    def sound(self):
        print("Basic sounds....")
class dog(animal):
    def sound(self):
        print("Bark")
class cat(animal):
    def sound(self):
        print("Meow")
class rabbit(animal):
    pass
an = animal()
d = dog()
c = cat()
r = rabbit()
for animal in (an,d,c,r):
    animal.sound()
    
# duck typing
class duck:
    def speak(self):
        print("Quack Quack")
class human:
    def speak(self):
        print("Talk")
class cat:
    def speak(self):
        print("Meow Meow")
def call_speak(obj):
    obj.speak()
z = duck()
z1 = human()
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
ap = person("ata","pp")
ap.displayName()

# using class variable in class
class person:
    country = "INDIA"
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
    @classmethod
    def changeCountry(cls):
        cls.country = "BHARAT"
ap1 = person("ata","pp")
ap1.displayName()
print(ap1.country)
ap1.changeCountry()
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
