# What is overloading ?
# it uses same function/operator but it gives different behaviours.

# program to to add 4 numbers using overloading ---->
class Calculator:
     def addition(self,a = None,b = None,c=None,d=None):
         if a != None and b != None and c != None and d != None:
             print(a+b+c+d)
         elif a != None and b != None and c != None:
             print(a+b+c)
         elif a != None and b != None:
             print(a+b)
e = Calculator()
e.addition(12,4)
e.addition(12,4,3)
e.addition(12,4,3,4)
