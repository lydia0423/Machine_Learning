#!/usr/bin/env python3 -- Shebang Line: allow a script to be invoked from the command line, #! must be the first two byte in the file(first 2 char and at the first line)
# Copyright 2009-2017 BHG http://bw.org/

#can specify mulitple import in one import statements
import platform

print('This is python version {}'.format(platform.python_version()))
