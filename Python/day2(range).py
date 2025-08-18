# What is Range in Python?
# It is used to genarate sequence of numbers.

#Range can be written as,
# range(startIndex, EndIndex(which is not included), stepsize(distance between numbers))
# print 1 - 5 using range
for x in range(1,6):
    print(x)
    
#print 5 to 1
for x in range(5,0):
    print(x)
    
#print table of 2
for x in range(2,22,2):
    print(x)
    
#print table of 5
for x in range(5,55,5):
    print(x)
    
#print table of 5 in reverse
for x in range(50,4,-5):
    print(x)
    
#Using Break statements
for x in range(1,6):
    if(x==3):
        break
    print(x)
        