
#?21. Write a Python program to find whether a given number (accept from the user) is even or odd, 
#?print out an appropriate message to the user.

num = int(input("Please enter an integer: "))

if(num % 2 == 0):
    print("{} is even number".format(num))
else:
    print("{} is odd number".format(num))