
#?Take two lists, say for example these two:
#?a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#?b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#?and write a program that returns a list that contains only the elements that are common between the lists 
#?(without duplicates). Make sure your program works on two lists of different sizes.

#?Extras:
#?Randomly generate two lists to test this
#?Write this in one line of Python (don’t worry if you can’t figure this out at this point - 
#?we’ll get to it soon)

#Solution 1
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for i in b:
    if i in a and i in b:
        c.append(i)

print(set(c))

#Solution 2
import random

randomlistA = []
randomlistB = []
c = []

for i in range(0,5):
    a = random.randint(1,30)
    b = random.randint(1,30)
    randomlistA.append(a)
    randomlistB.append(b)

print(randomlistA)
print(randomlistB)

for i in randomlistB:
    if i in randomlistA and i in randomlistB:
        c.append(i)

print(set(c))

#Solution 3
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print ("")
def common(a,b):
    c=[x for x in b if x in a]
    return set(c)

l2 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
l3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print (common(a,b))



