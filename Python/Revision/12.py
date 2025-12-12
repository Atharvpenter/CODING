# string
a = "hello"
print(type(a))

# list
a1 = ["ap","aap"]
print(type(a1))

# set
a2 = {11,22,33,44,55,66}
print(type(a2))

# dictionary
info ={
    "fn":"atharv"
}
print(type(info))

# for loops
# print table of 2
for x in range(2,22,2):
    print(x)
    
for x1 in range(20,1,-2):
    print(x1)
    
# print 1 to 9
for x2 in range(1,10):
    print(x2)

# print 1 to 9 upto 6
for x3 in range(1,10):
    if(x == 6):
        break
    print(x3)
    
# print 1 to 9 except 6
for x4 in range(1,10):
    if(x4 == 6):
        continue
    print(x4)

# print age 
# byear = [1999,2000,2001,2002,2003]
# age = []
# for x in byear:
#     a = 2025 - x
#     age.append(a)
#     print(age)
    
# using list comprehension
byear1 = [1999,2000,2001,2002,2003]
age = [2025 - x for x in byear1]
print(age)

# print above30 and below70 marks
marks = [19,52,99,87,23,55,4,47,66,72,69,81,94,93,57,64,22,11]
above30 = [x for x in marks if x < 30]
below70 = [x for x in marks if x > 70]
print(above30)
print(below70)

# class 
class person:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
atharv = person("atharv"," penter")
atharv.displayName()

# using class variable
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
# single level inheritance
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
atharv2 = teacher("atharv"," penter", 15000)
atharv2.displayName()
atharv2.displaySalary()

# multilevel inheritance
class Grandfather:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayGname(self):
        print(self.firstname + self.lastname)
class Father(Grandfather):
    def __init__(self,fn,ln,ffn):
        super().__init__(fn,ln)
        self.fname = ffn
    def displayFname(self):
        print(self.fname + self.lastname)
class Son(Father):
    def __init__(self,fn,ln,ffn,sfn):
        super().__init__(fn,ln,ffn)
        self.sname = sfn
    def displaySname(self):
        print(self.sname + self.lastname)
atharv3 = Son("Narayan"," Penter","Avinash","Atharv")
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
atharv4.displaySname()
atharv4.displayMname()

# overloading
class cal:
    def add(self,a=0,b=0,c=0):
        return a+b+c
a = cal()
print(a.add(1))
print(a.add(1,2))
print(a.add(1,2,3))

# overriding
class animal:
    def sound(self):
        print("Basic generic sounds....")
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
        print("quack")
class human:
    def speak(self):
        print("hello")
class cat:
    def speak(self):
        print("Meow")
def call_speak(obj):
    print(obj.speak())
a1 = duck()
a2 = human()
a3 = cat()
call_speak(a1)
call_speak(a2)
call_speak(a3)

# generator
def get_numbers3():
    yield 1
    yield 2
    yield 3
    yield 4

gen = get_numbers3()
print(gen)
e1 = next(gen)
print(e1)
print(next(gen))
print(next(gen))
print(next(gen))

# decorate
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