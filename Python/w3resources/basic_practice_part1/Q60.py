
#?60. Write a Python program to calculate the hypotenuse of a right angled triangle. 


from math import sqrt

a = float(input("Please enter the base of the triangle: "))
b = float(input("Please enter the height of the triangle: "))
c =  round(sqrt(a**2 + b**2), 2)
print("The hypotenuse of the right triangle = %d cm" % c)
