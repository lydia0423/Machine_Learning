#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#types of mode(can use multiple mode at the same time by using plus sign(+)):
    #r(read):can only read the file content
    #w(write):will empty the file if the file is not empty and it is start at the begining of the file and write over it. If the file is not exist, it will create it.
    #a(append): if the file already has the content, it will start at the end of th econtent and continue wrting without empty the file
    #t(text):default mode when r,w and a
    #b(binary):

def main(): 
    f = open('lines.txt', 'r')
    for line in f:
        #rstrip: will return a copy of the string with trailing whitespace removed.
        print(line.rstrip())

if __name__ == '__main__': main()
