Reclen = 40
with open("MyBinary.bin","wb") as f:
    n = int(input("How many numbers you want to Print :- "))
    for x in range(n):
        city = input("Enter the name of city :- ")
        city = city + (40 - len(city)) * " "
        city = city.encode()
        f.write(city)
        
reclen = 20
with open('cities.bin' , 'rb') as f:
    n = int(input('which record you want to read ?')) #3
    f.seek(reclen*(n-1))
    str = f.read(reclen)
    str = str.decode()
print(str)