# Encode ------->
Reclen = 40
with open("MyBinary.bin","wb") as f:
    n = int(input("How many numbers you want to Print :- "))
    for x in range(n):
        city = input("Enter the name of city :- ")
        city = city + (40 - len(city)) * " "
        city = city.encode()
        f.write(city)


# Decode -------> 
reclen = 20
with open('cities.bin' , 'rb') as f:
    n = int(input('which record you want to read ?')) #3
    f.seek(reclen*(n-1))
    str = f.read(reclen)
    str = str.decode()
print(str)


# Encode ->
reclen = 20
with open('binary.bin','wb') as f:
    n = int(input("How many number of city you want to print -> "))
    for i in range(n):
        city = input("Enter the city name -> ")
        city = city + (20 - len(city)) * " "
        city = city.encode()
        f.write(city)
        

# Decode ->
reclen = 20
with open('binary.bin' , 'rb') as f:
    n = int(input('which record you want to read ?')) #3
    f.seek(reclen*(n-1))
    str = f.read(reclen)
    str = str.decode()
print(str)