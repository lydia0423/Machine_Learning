#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#Blocks do not have the scope so that the variable defined inside 
#the block but it still can be call outside the block as they are still in the same scope

x = 42
y = 73

if x < y:
    print('x < y: x is {} and y is {}'.format(x, y))
elif x > y:
    print('x < y: x is {} and y is {}'.format(x, y))
else:
    print("x and y are the same")


    
