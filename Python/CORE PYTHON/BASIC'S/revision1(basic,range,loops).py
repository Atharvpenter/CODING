# string
a = 'atharv'
print(type(a))

# list
b = [11,22,33]
print(type(b))

# tuple
c = 10,
print(type(c))

# set
d = {11,22}
print(type(d))

# Dictionary ------->
info = {
    'fn':'atharv',
    'ln':'penter',
    'age':22
}
print(type(info))

# print 1 to 5 using range --------->
for x in range(1,6):
    print(x)

# Print 1 to 5 using for loop and break statement ----->
for x in range(1,6):
    if(x==4):
        break
    print(x)
    
# Print 1 to 5 using for loop and continue statement ---->
for x in range(1,6):
    if(x==3):
        continue
    print(x)
    
