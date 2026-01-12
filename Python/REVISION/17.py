# Strings
a = "atharv"
print(type(a))

# list
a1 = ["atharv","kunal","akhil"]
print(type(a1))

# set
a2 = {11,22,33,44}
print(type(a2))

# dictionary
a3 = {
    "fn":"atharv"
}
print(type(a3))

# using def function to reduce the repeatations in the code
def cal(x,y):
    print(x+y)
    print(x-y)
    print(x*y)
    print(x/y)
cal(4,9)

# using range function
# print table of 5 using range function
for x in range(5,55,5):
    print(x)
    
# print table of 5 in reverse
for x in range(50,4,-5):
    print(x)
    
# using break and continue statement in loops
# print 1 to 10 upto 4
for x in range(1,11):
    if(x==5):
        break
    print(x)
    
# print 1 to 10 except 4
for x in range(1,11):
    if(x==4):
        continue
    print(x)
    
# list comprehension
# calculate age using list comprehension
birthyear = [1998,1999,2000,2001,2002,2003,2004,2005]
age = [2025 - x for x in birthyear]
print(age)

# print odd and even using list cpmprehension
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even = [x for x in numbers if x % 2 == 0]
odd = [x for x in numbers if x % 2 != 0]
print(even)
print(odd)

# overriding
class cal:
    def add(self,a=0,b=0,c=0):
        return a+b+c
a = cal()
print(a.add(1))
print(a.add(1,2))
print(a.add(8,3,4))

# overloading
class animal:
    def sound(self):
        print("Basic")
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
class human:
    def speak(self):
        print("hello")
class cat:
    def speak(self):
        print("Meow")
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
e1 = next(gen)
print(e1)
print(next(gen))
print(next(gen))
print(next(gen))

# decorator
def my_decorate(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper
@my_decorate
def say_hello():
    print("hello")
say_hello()

# class
class person:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
ap = person("atharv"," penter")
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
    def ChangeCountry(cls):
        cls.country = "None"
ap1 = Person("Anjali"," Penter")
ap1.displayName()
print(ap1.country)
print(ap1.ChangeCountry())

# inheritance
# single inheritance
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

# multilevel inheritance
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
ap4 = son("Narayan"," Penter","Avinash","Atharv")
ap4.displayGname()
ap4.displayFname()
ap4.displaySname()

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