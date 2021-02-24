#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#set:
# -unordered list of unique values
# -indicate with curly brackets
# -does not allow duplicate elements

def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print_set(a)
    print_set(b)
    #sort the results
    print_set(sorted(a))
    print_set(sorted(b))
    #check elements in set a but not in set b by using "-" 
    print_set(a - b)
    #check elements in set a or in set b or both by using "|"
    print_set(a | b)
    #check elements not in a and b
    print_set(a ^ b)
    #check elements in a and b
    print_set(a & b)


def print_set(o):
    print('{', end = '')
    for x in o: print(x, end = '')
    print('}')

if __name__ == '__main__': main()
