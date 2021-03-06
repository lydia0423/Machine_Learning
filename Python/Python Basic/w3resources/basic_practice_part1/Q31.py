
#?31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

def greatest_common_divisor(x, y):
    gcd = 1
    if x % y == 0:
        return y
    
    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break  
    return gcd

print(greatest_common_divisor(12, 17))
print(greatest_common_divisor(4, 6))