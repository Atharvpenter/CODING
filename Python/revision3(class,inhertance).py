# Simple class ->
class person:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)
atharv = person("atharv"," penter")
atharv.displayName()

# Inheritance -->
# 1. Single level inheritance -->
class student:
    def __init(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayName(self):
        print(self.firstname + self.lastname)

class teacher(student):
    def __init__(self,fn,ln,sl):
        super().__init__(fn,ln)
        self.salary = sl
    def displayName(self):
        print(self.salary)

atharv1 = teacher("atharv","penter", 1000)
print(atharv1)

# 2. multi - level inheritance 
class Grandfather:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayGName(self):
        print(self.firstname + self.lastname)

class Father(Grandfather):
    def __init__(self,fn,ln,gfn):
        super().__init__(fn,ln)
        self.gname = gfn
    def displayFName(self):
        print(self.gname)
        
class Son(Father):
    def __init__(self,fn,ln,ffn,gfn):
        super().__init__(fn,ln,ffn)
        self.ffname = ffn
    def displaySName(self):
        print(self.ffname)

atharva = Son("Atharv","penter","avinash","narayan")
atharva.displayFName()
atharva.displayGName()
atharva.displaySName()

# 3. Multiple inheritance ->
class father:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
    def displayfName(self):
        print(self.firstname + self.lastname)

class mother:
    def __init__(self,fn,ln,mfn):
        super().__init__(fn,ln)
        self.mname = mfn
    def displaymName(self):
        print(self.fname + self.lastname)
        
class son(father,mother):
    def __init__(self,fn,ln,mfn,sfn):
        super().__init__(self,fn,ln)
        self.sname = sfn
    def displaysName(self):
        print(self.sname + self.lastname)

atharvv = son("avinash","penter","chhaya","atharv")
atharvv.displayfName()
atharvv.displaymName()
atharvv.displaysName()