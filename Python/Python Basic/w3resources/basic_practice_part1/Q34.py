
#?34. Write a Python program to sum of two given integers. However, 
#?if the sum is between 15 to 20 it will return 20.

def sum_num(x, y):
    total = x + y
    if total in range(15, 30):
        return 20
    else:
        return total

print(sum_num(10, 5))
print(sum_num(20, 89))
