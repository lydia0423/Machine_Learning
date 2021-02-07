
#?32. Write a Python program to get the least common multiple (LCM) of two positive integers.

from typing import NoReturn


def LCM(x, y):
    z = x * y
    for i in range(1, (z + 1)):
        if(i % x == 0 and i % y == 0):
            print("LCM is {}".format(i))
            break
    return LCM

print(LCM(3, 4))