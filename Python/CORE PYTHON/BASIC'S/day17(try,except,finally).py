# To Avoid Erros we can used different methods like
# Try() Contains the code that might raise an exception.
# Except() Catches and handles the error.
# finally() Contains code that always executes, no matter what.

# A single try block can be followed by several except block ---- True
# mutilple except blocks can be used to handle multiple exceptions ---- True
# we cannot write except block without try block ---- True
# we can write  a try block without except block ---- True
# else and finally blocks are not compulsory ----True
# When ther is no exception else block is executed after try block ---- True
# Finally block is always executed  ---- True




# Program 1 ------->
print("Hello")
try:
    numA = int(input("Enter a number A: "))
    numB = int(input("Enter a number B: "))
    print(numA/numB)
except ZeroDivisionError:
    print("It is an Error.")
print("Bye")


 