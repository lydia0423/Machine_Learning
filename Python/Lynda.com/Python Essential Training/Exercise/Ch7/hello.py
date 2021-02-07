#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#decorator: a special type of function that returns a wrapper function
# def f1():
#     def f2():
#         print("this is f2")
#     return f2

# #f1 is a wrapper for f2 because call x to get the value defined in the f2
# x = f1()
# x()

#decorator
def f1(f):
    def f2():
        print("this is before the function call")
        f()
        print("this is after the function call")
    return f2

@f1 #decorator which will take the function thar defined directly after it
def f3():
    print("this is f3")
f3()
