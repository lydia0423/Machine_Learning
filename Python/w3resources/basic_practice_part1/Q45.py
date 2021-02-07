
#?45. Write a python program to call an external command in Python.

from subprocess import call

#*to print the file in the long list format with the format: file type,file permissions, 
#*number of hard links to the file, file owner, file group, file size, date and time, file name.
call(["ls", "-l"])