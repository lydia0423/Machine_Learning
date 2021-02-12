
#?25. Write a Python program to check whether a specified value is contained in a group of values.
#?Test Data :
#?3 -> [1, 5, 8, 3] : True
#?-1 -> [1, 5, 8, 3] : False

list = [1, 5, 8, 3]
def find_value(n):
    if(n in list):
        return True
    else:
        return False

print(find_value(3))
print(find_value(-1))