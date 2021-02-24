#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#all function will return the value
def main():
    kitten()

def kitten():
    print('Meow.')

#any default args must after the common args which means they need to be at the end of the lists


def main():
    x = kitten()
    print(x) #it will return none as the kitten() don't have the return fucntion

def kitten():
    return 'Meow.'

#call by value
#mutable object might be changed but it will affect on the caller
def main():
    x = 5
    kitten(x)
    print("in main: x is {x}")

def kitten(a):
    print('Meow.')
    print(a)

#return value
def main():
    x = kitten()
    print(type(x),x)

def kitten():
    print('Meow.')
    return dict(x = 42, y = 45, z = 46)

#__name___ : a special variable name which will return the current name of the module
#if this file has been imported in another as a module, this name would have the name of the module
if __name__ == '__main__': main()
