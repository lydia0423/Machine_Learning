#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#Expression: combinations of literals, identifiers and operators which will return a value
#Statements: line of code
#semicolon is not required in the Python at the end of the code but there is exception:
# print("Hello") ; print("World") semicolon can be used within two statement

import platform

version = platform.python_version()

print('This is python version {}'.format(version))
