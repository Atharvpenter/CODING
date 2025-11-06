# What is Inheritance ?
# It allows One class to inherit properties and methods of another class.
# Inheritance has 3 types which are Single-level, multi-level, Multiple inheritance.

# Program -->
# 1. Single-level Inheritance ----> it used to inherit only one time.
class Student:

     def __init__(self,fn,ln):
         self.firstName = fn 
         self.lastName = ln

     def displayName(self):
         print(self.firstName + self.lastName)

class Teacher(Student):
    
     def __init__(self, fn, ln,sl):
         super().__init__(fn, ln)
         self.salary = sl

     def displaySalary(self):
         print(self.salary)
atharv  = Teacher("atharv"," penter",10000)
print(atharv)


# 2. Multi-level inheritance ---> it used to inherit multiple classes.
# Program 3 ---->
class GrandFather:
    #constructor
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
        
    def displayGName(self):
        print(self.firstname + self.lastname)
        
class Father(GrandFather):
    def __init__(self,fn,ln,ffn):
        super.__init__(fn,ln)
        self.Fname = ffn
    
    def displayFName(self):
        print(self.fname + self.lastname)
        
class Son(Father):
    def __init__(self,fn,ln,ffn,sfn):
        super.__init__(fn,ln,ffn)
        self.sname = sfn
        
    def displaySName(self):
        print(self.sname + self.lastname)
        
atharv1 = Son("Narayan"," Penter"," Avinash"," Atharv")
atharv1.displayGName()
atharv1.displayFName()
atharv1.displaySName()

# 3. Multiple Inheritance --->
#Program -->
class Father:
    #constructor
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
        
    def displayFname(self):
        print(self.firstname + self.lastname)
        
class Mother:
    def __init__(self,fn,ln,mfn):
        super.__init__(fn,ln)
        self.mname = mfn
    
    def displayMname(self):
        print(self.mname + self.lastname)

class Son(Father,Mother):
    def __init__(self,fn,ln,mfn,sfn):
        super.__init__(fn,ln,mfn)
        self.sname = sfn
    
    def displaySname(self):
        print(self.sname + self.lastname)
        
atharv2 = Son("Avinash"," Penter"," Chhaya"," Atharv")
print(atharv2)
atharv2.displayFname()
atharv2.displayMname()
atharv2.displaySname()