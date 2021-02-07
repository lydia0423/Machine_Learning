#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

from decimal import *

x = 7
print('x is {}'.format(x))
#type() is a built-in function to print the type of a value or variable
print(type(x))

#String types
#can use 3 quotes (single or double) to put the string in multiple line which including the space between it
x = '''

seven

'''
print('x is {}'.format(x))
print(type(x))

#string is an object
x = 'seven'.capitalize()
print('x is {}'.format(x))
print(type(x))

#can specify the positional arguments in the format method by using index number
x = 'seven {1} {0}'.format(8,9)
print('x is {}'.format(x))
print(type(x))

#can specify the positional arguments in the format method by using index number and operators
x = 'seven {1:<9}{0:>9}'.format(8,9)
print('x is {}'.format(x))
print(type(x))

#can put the leading zero, the numbers of zero depends on the space has been defined in {}
#the zero will be matched between each other
x = 'seven "{1:<09}" "{0:>09}"'.format(8,9)
print('x is {}'.format(x))
print(type(x))

#use f string to replace .format(), which only available after python 3.6
a = 8
b = 9
x = f'seven {a} {b}'
print('x is {}'.format(x))
print(type(x))

#Numeric types(integer and float)
x = 7
print('x is {}'.format(x))
print(type(x))

#get the answer in float
x = 7 / 3
print('x is {}'.format(x))
print(type(x))

#get the answer that able to fit between division of 7 and 3
x = 7 // 3
print('x is {}'.format(x))
print(type(x))

#get the remainder by using modulo
x = 7 % 3
print('x is {}'.format(x))
print(type(x))

#why the answer is not equal to zero because of the precision of the floating point processor inside the computer but it is not correct
#to solve it by import the modules
a = Decimal('.10')
b = Decimal('.30')
x = a + a + a - b
print('x is {}'.format(x))
print(type(x))

#Boolean type- used for logical values and expressions
x = True
print('x is {}'.format(x))
print(type(x))

#return bool results
x = 7 > 5
print('x is {}'.format(x))
print(type(x))

#return none type - used for absence value
x = None
print('x is {}'.format(x))
print(type(x))

#True and False conditions
#the results will be False if there is 0 , empty string and None type
x = 0
print('x is {}'.format(x))
print(type(x))

if x:
    print("True")
else:
    print("False")

#Tuple
x = (1, 2, 3, 4, 5)
print('x is {}'.format(x))
print(type(x))

#Tuple able to accept different types of data
x = (1, 'two', 3.0 , [4, 'four'], 5)
print('x is {}'.format(x))
print(type(x))

#id() return a unique identifier for each object
x = (1, 'two', 3.0 , [4, 'four'], 5)
y = (1, 'two', 3.0 , [4, 'four'], 5)
print('x is {}'.format(x))
print(type(x))
print(id(x))
print(id(y))

#return the same id as there are the same object
x = (1, 'two', 3.0 , [4, 'four'], 5)
y = (1, 'two', 3.0 , [4, 'four'], 5)
print('x is {}'.format(x))
print(type(x))
print(id(x[0]))
print(id(y[0]))

#checking whether x[0] and y[0] is the same object by using is
if x[0] is y[0]:
    print("Yes")
else:
    print("No")

#determine the type of the object by using isinstance
x = (1, 'two', 3.0 , [4, 'four'], 5)

if isinstance(x, tuple):
    print("Yes, it is tuple")
elif isinstance(x, list):
    print("Yes, it is list")
else:
    print("No")


