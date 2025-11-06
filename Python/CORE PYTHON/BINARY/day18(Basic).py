# w = write
# r = read
# a = append
# r+ = read and write

# to Open a file ->
a = open('file.txt','w')

# read data
str = input('Enter a text :')

# write data
a.write(str)

# closing data
a.close()