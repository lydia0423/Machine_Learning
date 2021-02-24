
#?36. Write a Python program to add two objects if both objects are an integer type.

def add_nums(x, y):
    if not(isinstance(x, int) and (isinstance(y, int))):
        raise TypeError("Inputs must be integers")
    else:
        return x + y

print(add_nums(3, 5))
print(add_nums(3, "Hello"))