#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# list: 
# -created using a pair of square brackets around a list of values seperated by commas
# -mutable (can add, delete and change values)

def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    print(game[1:5:2])
    #search index
    i = game.index('Paper')
    print(game[i])
    #add element in list
    game.append("Computer")
    #add element by defining the place in the list
    game.insert(0, "Water")
    #remove element from the list
    game.remove("Spock")
    #remove element from the end of the list and print out what has been removed
    x = game.pop()
    print(x)
    #remove element by using index
    game.pop(3)
    #or..
    del game[2]
    #remove element by slice
    del game[1:5]
    #join the list
    print(",".join(game))
    #count number of element
    print(len(game))
    print_list(game)

def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

#tuple:
# -like a list but it is immutable
# -created by uisng parentheses

def main():
    game = game = ( 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' )
    print_list(game)

def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': main()
