
#?Create a program that asks the user to enter their name and their age. 
#?Print out a message addressed to them that tells them the year that they will turn 100 years old.

#?Extras:
#?Add on to the previous program by asking the user for another number and printing out that many 
#?copies of the previous message. (Hint: order of operations exists in Python)
#?Print out that many copies of the previous message on separate lines. 
#?(Hint: the string "\n is the same as pressing the ENTER button)

name = str(input("Please enter your name: "))
age = int(input("Please enter your age: "))
times = int(input("How many times would you like to print your name and age: "))

for i in range(times):
    print("Your name is {} and your age is {}. You still have {} years to turn 100 years old".format(name, age, (100 - age)))