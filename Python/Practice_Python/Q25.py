
#?In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.
#?This time, we’re going to do exactly the opposite. You, the user, will have in your head a number 
#?between 0 and 100. The program will guess a number, and you, the user, will say whether it is too high, 
#?too low, or your number.

#?At the end of this exchange, your program should print out how many guesses it took to get your number.
#?As the writer of this program, you will have to choose how your program will strategically guess. 
#?A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) 
#?until you hit the number. But that’s not an optimal guessing strategy. An alternate strategy might 
#?be to guess 50 (right in the middle of the range), and then increase / decrease by 1 as needed. 
#?After you’ve written the program, try to find the optimal strategy! 
#?(We’ll talk about what is the optimal one next week with the solution.)

import random

count = 0
stop = False

ans = random.randint(0, 100)
print(ans)

while(not stop):
    user = input("Is the number correct?: ")

    if user == "too low":
        #*randomly increase between 1 to 4
        ans += random.randint(1, 4)
        print(ans)  
        count += 1
    elif user == "too high":
        #*randomly decrease between 1 to 4
        ans -= random.randint(1, 4)
        print(ans)
        count += 1
    elif user == "yes":
        print("The number is correct")
        stop = True

print("The system has guess for {} times to get the correct number".format(count))

