import os
reclen = 20
n = size = os.path.getsize('MyBinary.bin')
f1 = open('MyBinary.bin','rb')
f2 = open('MyBinary1.bin','wb')
cityname = input("Enter the city which you have to delete -> ")
cityname = cityname + (reclen - len(cityname)) * " "
cityname = cityname.encode()

for i in range(n):
    str = f1.read(20)
    if str != cityname:
        f2.write(str)
f1.close()
f2.close()

os.remove('MyBinary.bin')
os.rename('MyBinary1.bin','MyBinary.bin')