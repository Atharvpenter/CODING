# What is Lambda function ?
# it consists of arguements : expressions.
# In lambda function map,filter is used.



def add(x,y):
    return x + y
e = add(12,3)
print(e)

# Now using lambda funtion,
#add = lambda x,y : x+y
#e1 = add(22,3)
#print(e1)

#sub = lambda x,y : x-y
#e2 = sub(10,3)
#print(e2)

# print numbers using lambda function,
#numbers = [11,22,33,44,55,66]
#a = map(lambda x : x + 10, numbers)
#print(a)

marks = [22,54,645,33,45,113,445,76,30,66,55,98]
above40 = []
for x in marks:
    if x > 40:
        above40.append(x)
        print(above40)
        
a1 = filter(lambda x : x > 40 ,marks)
print(list(a1))

# Different operations using lambda functions,
names  = ["atharv","Abhishek","Ranvir","Shravan"]
capitalNames = []
for name in names:
    capitalNames.append(name.upper())
    print(capitalNames)
    
# another way to do this using list comprehension,
# expression:loop:condition
a2 = [name.upper for name in names]
print(a2)


# using lambda funtions,
a3 = map(lambda x : x.upper,name)
print(a3)