# what is dictionary?
# is used to store data by key-value pairs.
info = ['atharv','penter',22]
print(info) 
print(type(info))

# Dictionary can be written as -->
info1 = {
    "fn":"atharv",
    "ln":"penter",
    "age":22
}
print(info1)
print(type(info1))
      
# does dictionary store value by index? --- NO
# does dictionary stores duplicate values? --- YES

info2 = {
    "fn":"atharv",
    "ln":"penter",
    "age":22
}
print(info2['fn'])
print(info2['age'])

# we can update dictionary ,
info2['fn'] = 'Ram'
print(info2)
print(len(info2))

# using loop in dictionary.
info3 = {
    "fn":"atharv",
    "ln":"penter",
    "age":22
}
for x in info3:
    print(x,info2[x])
    
for x in info3.keys():
    print(x)

for x in info3.items():
    print(x)