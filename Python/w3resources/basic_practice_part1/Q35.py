
#?35. Write a Python program that will return true if the two given integer values are 
#?equal or their sum or difference is 5.

def sum_num(x, y):
    if x == y or abs(x-y) == 5 or (x+y) == 5:
        return True
    else:
        return False

print(sum_num(7, 2))
print(sum_num(3, 2))