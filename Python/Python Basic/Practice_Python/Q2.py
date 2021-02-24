
#?Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message 
#?to the user. Hint: how does an even / odd number react differently when divided by 2?
#?Extras:
#?If the number is a multiple of 4, print out a different message.
#?Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
#?If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num = int(input("Please enter a number to check whether it is even or odd number: "))
check = int(input("Please enter a number to check whether it is divided evenly by the input number: "))

if num % 4 == 0:
    print("{} is multiple of 4".format(num))
elif num % 2 == 0:
    print("{} is even number".format(num))
else:
    print("{} is odd number".format(num))

if(num % check == 0):
    print("{} is divided evenly by {}".format(num, check))
else:
    print("{} is not divided evenly by {}".format(num, check))