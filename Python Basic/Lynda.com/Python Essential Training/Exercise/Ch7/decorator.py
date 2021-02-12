#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#decorator: 
# -a special type of function that returns a wrapper function
# -a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure
# -usually called before the definition of a function you want to decorate
# -It is advisable and good practice to always use functools.wraps when defining decorators in order to avoid lost of metadata
# -ensures that your code is DRY(Don't Repeat Yourself)

import time

def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print(f'Elapsed time: {(t2 - t1) * 1000} ms')
    return wrapper


@elapsed_time
def big_sum():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print(f'Big sum: {sum(num_list)}')

def main():
    big_sum()

if __name__ == '__main__': main()
