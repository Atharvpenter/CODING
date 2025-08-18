#Basic Operations in Python ---->
#Arithmatic Operations--->
#x = 10
#print(x)
 
#a = 10
#b = 20
#print(a+b)
#print(a-b)

#To avoid repeatation we use DEF, in JavaScript we use Function
def Calculator(x,y):
    print(x+y)
    print(x-y)
    print(x*y)
Calculator(21,9)
 
#what is string in python?
#it is a sequence of characters used to represent text
#Or we can say anything inside a single or double quote is a string.
a = 'atharv'
print(a)
print(type(a))

#boolean
w3 = True
print(w3)
print(type(w3))

#int
a1 = 10
print(a1)
print(type(a1))

#Logical Operators ---->
#AND
#only true - true --->true, all are False
print(2==2 & 3==3)
print(2==2 & 3==2)

#OR
#only False - False --->False, all are true
print(2==2 or 2==1)
print(2==1 or 1==2)

#Not
#it reverses all true become false and false become true.
print(not(1==1))
print(not(1==2))

# Various Methods of string ----->
#Upper -> used to capital all string
a = 'atharv'
b = a.upper()
print(b)

#lower -> Used lowerCase all string
b1 = a.lower()
print(b1)

#Capitalize -> Only capital first letter
b2 = a.capitalize()
print(b2)

#title
b3 = a.title()
print(b3)