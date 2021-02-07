
#?43. Write a Python program to get OS name, platform and release information.

import os
import platform


print(os.uname())
print(platform.system())
print(platform.release())