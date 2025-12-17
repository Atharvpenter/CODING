# string
a = "atharv"
print(type(a))

# list
a1 = ["atharv","ram"]
print(type(a1))

# set
a2 = {11,22,33}
print(type(a2))

# dictionary
a3 = {
    "fn":"atharv"
}
print(type(a3))

# if there are repeatation in the code we use def function in python
def cal(x,y):
    print(x+y)
    print(x-y)
cal(8,4)

# for range
# print table of 2
for x in range(2,22,2):
    print(x)

# print table of 2 in reverse
for x in range(20,1,-2):
    print(x)
    
# print 1 to 10
for x in range(1,11):
    print(x)

# using break and continue statement using for range
# print 1 to 10 upto 5
for x in range(1,11):
    if(x == 6):
        break
    print(x)

# print 1 to 10 except 5
for x in range(1,11):
    if(x == 5):
        continue
    print(x)
    
# list comprehension
# print age
birthyear = [1999,2000,1987,2003,2006,2007,1995]
age = [2025 - x for x in birthyear]
print(age)

# print above60 marks
marks = [99,24,23,75,15,66,95,88,81,27,68,69,71,72,77,39]
above60 = [x for x in marks if x < 60]
print(above60)

# class 
class person:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
atharv = person("Atharv"," Penter")
atharv.displayName()

# class variable
class name:
    country = "India"
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
    @classmethod
    def changeCountry(cls):
        cls.changeCountry = "None"
atharv1 = name("Atharv"," Penter")
atharv1.displayName()
print(atharv1.country)
print(atharv1.changeCountry())

# inheritance
# single inheritance
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
atharv2 = teacher("atharv"," Penter", 10000)
atharv2.displayName()
atharv2.displaySalary()

# multiplevel inheritance
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
atharv3 = son("Narayan"," Penter","Avinash","Atharv")
atharv3.displayName()
atharv3.displayFname()
atharv3.displaySname()

# multiple inheritance
class father:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
class mother:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayMname(self):
        print(self.firstname + self.lastname)
class son(father,mother):
    def __init__(self, fn, ln,sfn):
        super().__init__(fn, ln)
        self.sname = sfn
    def displaySname(self):
        print(self.sname + self.lastname)
atharv4 = son("Chhaya"," Penter","Atharv")
atharv4.displayMname()
atharv4.displaySname()

# overloading
class cal:
    def add(self,a=0,b=0,c=0):
        return a+b+c
a = cal()
print(a.add(2))
print(a.add(3,5))
print(a.add(5,7))

# overriding
class animal:
    def sound(self):
        print("SOunds")
class dog(animal):
    def sound(self):
        print("Bark")
class cat(animal):
    def sound(self):
        print("Meow")
class rabbit(animal):
    pass
a = animal()
d = dog()
c = cat()
r = rabbit()
for animal in (a,d,c,r):
    animal.sound
    
# duck typing
class duck:
    def speak(self):
        print("Quack")
class human:
    def speak(self):
        print("Talk")
class cat:
    def speak(self):
        print("Meow")
def call_speak(obj):
    print(obj.speak())
z = duck()
h = human()
z1 = cat()
call_speak(z)
call_speak(h)
call_speak(z1)

# generators
def get_numbers():
    yield 1
    yield 2
    yield 3
    yield 4
gen = get_numbers()
print(gen)
e1 = next(gen)
print(e1)
print(next(gen))
print(next(gen))
print(next(gen))

# decorator
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("after")
    return wrapper
@my_decorator
def say_Hello():
    print("HELLO")
say_Hello()
    