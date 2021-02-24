#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#to know more about the error
import sys 

def main():
    try:
        x = 0/6
    except ValueError:
        print("I caught a ValueError")
    except ZeroDivisionError:
        print("Don\'t divide by zero")
    except:
        print(f'Unknown Error: {sys.exc_info()[1]}')
    else:
        print("Good Job")
        print(x)

if __name__ == '__main__': main()