# What is abstraction ?
# It is used to make the code more usable and easy 
# We can also create Objects of abstraction class.
# Abstraction is useful when multiple classes share common behavior.



# Program 1 --->
from abc import ABC , abstractmethod
class myclass(ABC):
    @abstractmethod
    def calculate(self,x):
        pass

class subclassA(myclass):
    def calculate(self, x):
        return x * x * x
    def One(self):
        print("One is called...")

class subclassB(myclass):
    def calculate(self, x):
        return x * x
    def Two(self):
        print("Two is called...")

#f = subclassA
#f.calculate()
#f.Two()

# Program 2 ---->
from abc import ABC , abstractmethod
class shape(ABC):
    # constructor
    def __init__(self,color):
        self.color = color
        
@abstractmethod
class area(shape):
    pass

class circle(shape):
    def __init__(self,color,radius):
        super().__init__(color)
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius

class square(shape):
    def __init__(self,color,radius):
        super().__init__(color)
        self.radius = radius
        
    def area(self):
        return self.radius * self.radius  
    
a = circle("red",2)
b = square("yellow",5)
print(a.radius)
print(b.radius)
a.area()