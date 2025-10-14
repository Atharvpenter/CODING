year = [1991,1993,2001,1999,2004]
birthyear = []
for x in year:
    age = 2025 - x
    birthyear.append(age)
    print(birthyear)
    
# We have another to find the birthyear that we can use filter() function.
marks = [39,50,55,90,88]
above40 = []
for x in marks:
    mark = x > 40
    above40.append(mark)
    print(above40)
    
# Sum of array
num = [11,22,33,44,55]
total = 0
for x in num:
    total = total + x
    print(total)
    
# List Comprehension -->
# it can be written as [expression : loop : Condition]

years = [2002,2003,2004,2005]
birthyears = [2024 - x for x in years]
print(birthyears)

Marks = [33,44,55,77]
above40 = [x for x in Marks if x > 40]
print(above40)

even = [1,2,3,4,5,6,7,8,9,10]
e = [x for x in even if x % 2 == 0]
o = [x for x in even if x % 2 != 0]
print(e)
print(o)

nums = [1,2,3,4,5,6,7,8,9,10]
table2 = [x*2 for x in nums]
print(table2)

w = [1,2,3,4,5,6,7,8]
r = [x*3 for x in w]