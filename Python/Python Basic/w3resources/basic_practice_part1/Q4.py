
#?4. Write a Python program which accepts the radius of a circle from the user and compute the area.
#?Sample Output :
#?r = 1.1
#?Area = 3.8013271108436504

from math import pi

r = float(input("Please enter the radius of the circle: "))
print("r = {}".format(r))
print("Area = " + str(pi * r**2))