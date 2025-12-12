# string
a = "atharv"
print(type(a))

# list
a1 = ['atharv']
print(type(a1))

# set 
a2 = {11,22,33,44,55}
print(type(a2))

# using range function
# print table of 2 
for x in range(2,22,2):
    print(x)
    
# print table of 2 in reverse
for x in range(20,1,-2):
    print(x)
    
# dictionary
info = {
    "fn":"atharv"
}
print(type(info))

# using list comprehension
# print age
birthyear = [1999,2000,2001,2002,2003,2004,2005]
age = [2025 - x for x in birthyear]
print(age)

# using break statement in range function
# print 1 to 10 upto 6
for x in range(1,11):
    if(x == 7):
        break
    print(x)
    
# print 1 to 10 except 6
for x in range(1,11):
    if(x == 6):
        continue
    print(x)
    
# class 
class person:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
atharv = person("atharv"," penter")
atharv.displayName()

# using class variable in class
class name:
    country = "india"
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
    @classmethod
    def changeCountry(cls):
        cls.country = "None"
atharv1 = name("atharv"," penter")
atharv1.displayName()
print(atharv1.country)
print(atharv1.changeCountry())

# inheritance
# single inheritance
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
atharv2 = son("Avinash"," Penter","Atharv")
atharv2.displayName()
atharv2.displaySname()

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
atharv3 = son("Narayan"," Penter","Avinash","Atharv")
atharv3.displayGname()
atharv3.displayFname()
atharv3.displaySname()

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
atharv4 = son("Chhaya"," Penter","Atharv")
atharv4.displayMname()
atharv4.displaySname()

# overloading
class cal:
    def add(self,a=0,b=0,c=0):
        return a + b + c
a = cal()
print(a.add(1))
print(a.add(1,9))
print(a.add(1,9,9))

# overriding
class animal:
    def sound(self):
        print("animal makes sound")
class dog(animal):
    def sound(self):
        print("Bark")
class cat(animal):
    def sound(self):
        print("meow")
a= animal()
d=dog()
c=cat()
a.sound()
d.sound()
c.sound()

# duck typing
class dog:
    def sound(self):
        print("Bark")
class cat:
    def sound(self):
        print("Meow")
def make_sound(animal):
    print(animal.sound())
a=dog()
b=cat()
make_sound(a)
make_sound(b)

# Generators
def get_number2():
    yield 1
    yield 2
    yield 3
    yield 4
gen = get_number2()
print(gen)
e1 = next(gen)
print(e1)
print(next(gen))
print(next(gen))
print(next(gen))

# decorator
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

