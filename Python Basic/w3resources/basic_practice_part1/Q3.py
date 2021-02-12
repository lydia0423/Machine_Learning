
#?3. Write a Python program to display the current date and time.
#?Sample Output :
#?Current date and time :
#?2014-07-05 14:34:14

import datetime

now = datetime.datetime.now()
#strftime = string from time (convert string to datetime format)
print("Current date and time {}".format(now.strftime("%Y-%m-%d %H:%M:%S")))