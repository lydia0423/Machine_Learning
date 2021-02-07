# 
# Example file for variables
#

# Declare a variable and initialize it
f = 0
print(f)

# # re-declaring the variable works
f = "abc"
print(f)


# # ERROR: variables of different types cannot be combined
print("this is a string" + str(123))


# Global vs. local variables in functions
def someFunction():
    global f #affect the f that outside the function
    f = "def"
    print(f)

someFunction()
print(f)

#del = delete
del f
print(f)

