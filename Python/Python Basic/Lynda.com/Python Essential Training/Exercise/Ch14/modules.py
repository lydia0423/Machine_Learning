#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#information about operating system
import os
#information about system
import sys
import random
import datetime


def main():
    v = sys.version_info
    print('Python version {}.{}.{}'.format(*v))
    a = os.name
    print(a)
    b = os.getenv('PATH')
    print(b)
    #get current working directory
    c = os.getcwd()
    print(c)
    #get a random number that generate by the system with 25 bytes long
    d = os.urandom(25)
    print(d)
    #get a random number between certain range
    e = random.randint(1, 1000)
    print(e)
    #shuffle the number in the list as the list is mutable
    f = list(range(25))
    print(f)
    random.shuffle(f)
    print(f)
    #datetime module
    now = datetime.datetime.now()
    print(now)
    #get each component as an individual part
    print(now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)

if __name__ == '__main__': main()
