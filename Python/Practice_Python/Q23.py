
#?Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. 
#?One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of 
#?happy numbers up to 1000.

#?(If you forgot, prime numbers are numbers that can’t be divided by any other number. 
#?And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia. 
#?The explanation is easier with an example, which I will describe below.)

prime = []
happy = []
c = []

open_file = open('PrimeNumber(Q23).txt', 'r')
p = open_file.readlines()
for i in p:
    prime.append(i.rstrip())

open_file = open('HappyNumber(Q23).txt', 'r')
h = open_file.readlines()
for i in h:
    happy.append(i.rstrip())

def overlap(a,b):
    c = [x for x in b if x in a]
    return set(c)


print(overlap(prime, happy))


