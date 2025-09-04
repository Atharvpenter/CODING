# add @ at end of the input
a = open("Myfile.txt","w")
print("Enter text :")
while str != '@':
    str = input()
    if str != '@':
        a.write(str + "\n")
a.close()
