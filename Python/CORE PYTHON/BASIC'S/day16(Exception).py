# What is an Exception ?
# it is an error that occurs during compiling programs.
# It is a Runtime error
# Types are :- inbuilt, user-defined error.
# Inbuitl Error are predefined error by python like ZeroDivisionError etc.
# User-Defined Error are which are defined by the user itself.



# Compile-time Error -->  Are the syntax error in the program.
# It includes syntax error, type error etc.

# Program 1 -->
#a = 10
#b = 2
#if a > b:
#    print("a is greater")
#else:
#    print("b is greater")

# Run-time Error --->
# this are the error that occurs after code compiled.
# it includes zero division, value error etc.

# Program 2 --->
def divide(a,b):
    return a/b
    e = divide(10,0)
    print(e)
    

# Logical Error --->
# it is used when their is problem in logic of the program.

# Program 3 --->
def salary(sal):
    return sal * 3


# To Avoid Erros we can used different methods like
# Try() Contains the code that might raise an exception.
# Except() Catches and handles the error.
# finally() Contains code that always executes, no matter what.

# Program ------->
