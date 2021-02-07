#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class bunny:
    def __init__(self, n):
        self._n = n

    def __repr__(self):
        return f"The number of bunnies is {self._n}"

    def __str__(self) :
        return f"The number of bunnies is {self._n}"
        
x = bunny(47)
#repr(string representation): will print the most possible form of an object
print(repr(x))


#container
x = (1, 2, 3, 4, 5)
y = reversed(x)
z = (6, 7, 8, 9, 10)
a = zip(x, z)

for b, c in a: print(f"{b} - {c}")

for i in y: print(i)

print(x)
print(y)

#to print the tuple value with index number
x = ('cat', 'dog', 'rabbit', 'velociraptor')
for i, v in enumerate(x):
    print(f'{i}: {v}')

#object and class function
x = 42
y = type(x)
#to verify the class of the value which will match the given class or not
z = isinstance(x, int)
#print the unique number of the object
a = id(x)

print(x)
print(y)
print(z)
print(a)




