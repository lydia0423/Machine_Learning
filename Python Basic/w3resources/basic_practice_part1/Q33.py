
#?33. Write a Python program to sum of three given integers. However, 
#?if two values are equal sum will be zero.

def sum_num(x, y, z):
    total = x + y + z
    if(x + y == total or y + z == total or x + z == total):
        return "zero"
    else:
        return total

print(sum_num(2, 2, 2))
print(sum_num(3, 1, 0))
        