# Finding --->

#import os
#reclen = 20
#size = os.path.getsize('MyBinary.bin')
#n = int(size/reclen)
#with open('MyBinary.bin','r+b') as f:
#    name = input("Enter city name ")
#    name = name + (20 - len(name)) * " "
#    name = name.encode()
    
#    position = 0
#    found = False
#    for i in range(n):
#        f.seek(position)
#        str = f.read(20)
#        if str == name:
#            found = True
#            print("City name found...")
#            position = position + reclen
#            if not found:
#                print("Not Found...")

# Updating ---->
import os
reclen = 20
size = os.path.getsize('MyBinary.bin')                
n = int(size/reclen)
with open('MyBinary.bin','r+b') as f:
    name = input("Enter City name ->")
    name = name + (reclen - len(name))* " "
    name = name.encode()
    #Updating ->
    newname = input("Enter new name -> ")
    newname = newname + (reclen- len(newname))* " "
    newname = newname.encode()
    
    position = 0
    found =  False
    for i in range(n):
        f.seek(position)
        str = f.read(reclen)
        if str == name:
            found = True
            f.seek(-20,1)
            f.write(newname)
            position = position + reclen
            if not found:
                print("not found")