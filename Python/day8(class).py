# What is class in python?
# class is blueprint of creating object 
class Person:
    #constructor
    def __init__(self,fn,ln):
        self.firstName = fn 
        self.lastName = ln
    
    def displaName(self):
        print(self.firstName + self.lastName)

amol2 = Person("amol","rao")
amol2.displaName()