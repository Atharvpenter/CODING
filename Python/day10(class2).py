# Program 1 ------>
class Person:
    #constructor
    def __init__(self,fn,ln):
        
        #properties, instance variable
        self.firstName = fn 
        self.lastName = ln
        
    #Methods
    def displayName(self):
        print(self.firstName + self.lastName)

atharv2 = Person("atharv"," penter")
atharv2.displayName()

# Program 2 ------>
class PersonB:
    #class variable
    country = "India"
    
    #contructor
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
        
    #methods,
    def displayName(self):
        print(self.firstname + self.lastname)
        
    # If i have to change country name of the class variable,
    @classmethod
    def changeCountry(cls):
        cls.country = "INDIA"
            
atharvB= PersonB("Atharv"," Penter")
atharvB.displayName()
print(atharvB.firstname)
print(atharvB.country)
PersonB.changeCountry()
print(atharvB.country)


#Program 2 --->
class Bank:
    #constructor 
    def __init__(self,fn,bal):
        #properties
        self.fullname = fn
        self.balance = bal
        self.transaction = []
        
        
    #Methods
    def deposit(self,amt):
        self.balance = self.balance + amt
        self.transaction.append(amt)
        return self.balance
    
    def withdrawl(self,amt):
        if amt < self.balance:
            self.balance = self.balance(-amt)
            self.transaction.appent(-amt)
            return self.balance
        else:
            print("insufficient Balance")
            
    def last5transactions(self):
        return self.transaction[-5:]
    
Atharv = Bank("Atharv Penter",200)
Shivam = Bank("Shivam More",400)
Atharv.deposit(50)
Atharv.deposit(80)
Atharv.deposit(40)
Atharv.deposit(30)
Atharv.deposit(20)
Atharv.deposit(10)
Atharv.deposit(10)
print(Atharv.last5transactions())