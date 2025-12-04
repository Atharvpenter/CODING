# string
a = "atharv"
print(type(a))

# dictionary
info = {
    "fn":"atharv"
}
print(type(info))

# print table of 2 
for x in range(2,22,2):
    print(x)
    
for x in range(20,1,-2):
    print(x)

# print age 
# birthyear = [1999,2000,2001,2002,2003,2004,2005,2006]
# age = []
# for x in birthyear:
#     a = 2025 - x
#     age.append(a)
#     print(age)
    
# using list comprehension
birthyear1 = [1999,2000,2001,2002,2003,2004,2005,2006]
age = [2025 - x for x in birthyear1]
print(age)

# using for loops with break statement and continue statement
for x in range(1,11):
    print(x)
    
# using break
for x in range(1,11):
    if(x == 8):
        break
    print(x)
    
# using continue
for x in range(1,11):
    if(x == 7):
        continue
    print(x)
    
# list 
a1 = [11,22,33]
print(type(a1))

# set
a2 = {1,2,3,4,5}
print(type(a2))

# class
class person:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayname(self):
        print(self.firstname + self.lastname)
atharv = person("atharv"," penter")
atharv.displayname()

# using class variable
class name:
    country = "India"
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
    @classmethod
    def changeCountry(cls):
        cls.country ="None"
atharv1 = name("atharv"," penter")
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
atharv2 = teacher("atharv","penter", 15555)
atharv2.displayName()
atharv2.displaySalary()

# *args
def add(*args):
    print(args)
    total = 0
    for x in args:
        total = total - x
    return total
e = add(1,26,98,5)
print(e)

# *kwargs
def addCit(**kwargs):
    print(kwargs)
    kwargs['city'] = 'pune'
    kwargs.update({"lang":"marathi"})
    return kwargs
e1 = addCit(fn="a",ln="p")
print(e1)

# overloading 
class cal:
    def add(self,a=0,b=0,c=0):
        return a + b + c
a = cal()
print(a.add(1))
print(a.add(1,2))
print(a.add(1,2,3))

# overriding
class animal:
    def sound(self):
        print("Basic generic sound :")
class Dog(animal):
    def sound(self):
        print('Bark')
class Cat(animal):
    def sound(self):
        print('meow meow')
class rabbit(animal):
    pass
a = animal()
b = Dog()
c = Cat()
d = rabbit()
for animal in (a,b,c,d):
    animal.sound()  
    
# polymorphism
# Duck typing
class Duck:
    def speak(self):
        print("Quack Quack")
class Human:
    def speak(self):
        print("hello hi")     
class Cat:
    def speak(self):
        print("Meow")
def call_speak(obj):
    print(obj.speak())
duckA = Duck()
humanB = Human()
catC = Cat()
call_speak(duckA)
call_speak(humanB)
call_speak(catC)

# generators
# decorators
# A generator is a special type of function , which returns more than one value at a time
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

# decorators before functions run some statements
def my_decorate(func):
    def wrapper():
        print("before the function is called :")
        func()
        print("after a function is called")
    return wrapper
@my_decorate
def say_hello():
    print("hello")
say_hello()

# int as parameter and int as return int 
def CalA(x,y):
    return x + y
e = CalA(12,3)
print(e)


# float as a parameter and function as return type 
def CalB(x,y):
    return x + y
f = CalB(12.5,12.10)
print(f)

# boolean as a parameter and boolean as return type
def canDrive(age, haveVehcile):
    if age >= 18 and haveVehcile:
        return True
    else:
        return False
f = canDrive(19,True)
print(f)

# string a parameter and string as return type 
def Greet(word):
    return "hello "+ word
g = Greet("chinmay")
print(g)

# list as a parameter and list as a return type 
city = ["pune","mumbai","bnaglore","kolkata"]
def addCity(lst):
    lst.append("nagpur")
    return lst
city2 = addCity(city)
print(city2)

# dict as a parameter and dict as a return type 

info = {
    "firstName":"chinmay",
    "lastName":"deshpande",
}
def addCity(info):
    info['city'] = 'pune'
    return info
e = addCity(info)
print(e)

# tuple as parameter and tuple as return type

numbers = (11,22,33)

def addToTuple(tupA):
    tupA = list(tupA)
    tupA.append(44)
    tupA = tuple(tupA)
    return tupA
f = addToTuple(numbers)
print(f)

# set as a parameter and set as a return type 
setA = {11,22,33}
def addToSet(setC):
    setC.add(55)
    return setC
k = addToSet(setA)
print(k)