# What is List in python?
# list is a collection of items which can be change or we can say mutable.
# anything inside square bracket is list
l = [11,22,33]
print(l)
print(type(l))

#string list ---->
names = ['Atharv','Shivam','Shreyash']
print(names)

# list store value by index
l1 = ['atharv','shivam','shreyash']
print(l1[0])

# update value in a list
l1[1] = 'aditya'
print(l1)

# Calculate length of list
print(len(l1))

for x in range(len(l1)):
    print(l1[x])
    
for item in l1:
    print(item)
    
