# What is Duck Typing ?
# if an object has the necessary methods and attributes to perform a certain operation,
# Python will treat it as expected type,actual class or inheritance hierarchy.



class Dog:
    # method
    def sound(self):
        print("Bow Bow")
class Human:
    def sound(self):
        print("Hi hello")
class Cat:
    def sound(self):
        print("meow meow")
# function
def callAnimal(obj):
    obj.sound()

a = Dog()
b = Human()
c = Cat()
callAnimal(a)
callAnimal(b)
