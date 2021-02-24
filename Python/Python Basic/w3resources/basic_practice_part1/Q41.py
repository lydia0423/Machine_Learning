
#?41. Write a Python program to check whether a file exists.

import os.path

open("test.txt", "w")
print(os.path.isfile("test.txt"))