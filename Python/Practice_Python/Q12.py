
#?Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) 
#?and makes a new list of only the first and last elements of the given list. 
#?For practice, write this code inside a function.

a = [5, 10, 15, 20, 25]
b = []

def find_num(aList):
    return [n for i, n in enumerate(aList) if i == 0 or i == len(aList) - 1]

print(find_num(a))




