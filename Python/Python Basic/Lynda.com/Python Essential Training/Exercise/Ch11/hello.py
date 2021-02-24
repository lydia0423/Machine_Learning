#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#common to call method on literal string because string is first class object in Python
#can assign string as variable
print("Hello, World.".upper())

#able to subclass the string
class MyString(str):
    def __str__(self):
        return self[::-1]

s = MyString("Hello, World.")
print(s)

#casefold similar to lower but it remove all distinction even in unicode
print("Hello, World.".casefold())

#string is immutable
s1 = "Hello, World."
s2 = s1.upper()

print(id(s1))
print(id(s2))

#concatenate the string by using plus sign
s1 = "Hello, World."
s2 = "Hello, Everyone."

print(s1 + s2)

#concatenate the string by using single quote with space
s1 = 'Hello, World.' ' Hello, Everyone.'
print(s1)

#format the string with .format() and {}(placeholder)
x = 42
y = 73
#will take the arguments with the order (without any specification)
print("The number is {} {}".format(x, y))
#or.. named the placeholder with the variable
print("The number is {a} {b}".format(a = x, b = y))
#or.. named the placeholder by using positional arguments (which start at one)
print("The number is {1} {0}".format(x, y))
#formating instruction which preceded by the colon(:)
                    #right justify with 5 spaces
print("The number is {0: < 5} {1: > 5}".format(x, y))
                                #left justify with 5 spaces

#format the string with ,
x = 42 * 747 * 1000
print("The number is {:,}".format(x))

#format the decimal numbers, f stands for default decimal places
print("The number is {:.2f}".format(x))

#format the string to octact(o), hexadecimal(x), binary(b)
print("The number is {:b}".format(x))

#used f string to replace .format() (starting from Python 3.6 and above)
print(f"The number is {x}")