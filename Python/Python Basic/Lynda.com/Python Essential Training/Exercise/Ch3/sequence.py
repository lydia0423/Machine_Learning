#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#the list is mutable which means it is changeable
#for loop is sequencing through the list
x = [ 1, 2, 3, 4, 5 ]
for i in x:
    print('i is {}'.format(i))

#reassign the one of the element in x list
x = [ 1, 2, 3, 4, 5 ]
x[2] = 42
for i in x:
    print('i is {}'.format(i))

#the list with round bracket is known as tuple which is immutable
x = ( 1, 2, 3, 4, 5 )
for i in x:
    print('i is {}'.format(i))

#can create the sequence by using range which will end with the last number you specify
x = range(5)
for i in x:
    print('i is {}'.format(i))

#can create the starting point and ending point in range
x = range(5, 10)
for i in x:
    print('i is {}'.format(i))

#can specify the step by in the third parameter
#this will step by 5
x = range(5, 50, 5)
for i in x:
    print('i is {}'.format(i))

#range is immutable
#to solve that can add list() before the range so that it is mutable
x = list(range(5))
x[2] = 42
for i in x:
    print('i is {}'.format(i))

#create a searchable dictionary(mutable)
#return a tuple of each items with the key and value
x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
#indicate that key three has the value of 42
x['three'] = 42
for k, v in x.items():
    print('k: {}, v: {}'.format(k, v))