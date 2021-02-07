#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    kitten('meow', 'grrr', 'purr')

#(*) is the variable length argument list, useful when have different number of arguments
def kitten(*args):
    #len: return the number of items in a container.
    if len(args):
        for s in args:
            print(s)
    else: print('Meow.')

if __name__ == '__main__': main()
