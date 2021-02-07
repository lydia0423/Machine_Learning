
#?40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).



from math import sqrt


d1 = (3, 5)
d2 = (5, 7)

print("The distance between two points is " + repr(sqrt((d1[0] + d2[0])**2 + (d1[1] + d2[1])**2)))

