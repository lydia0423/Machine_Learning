#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#copy a image file
def main():
    infile = open('berlin.jpg', 'rb')
    outfile = open('berlin-copy.jpg', 'wb')
    while True:
        #we don't want read the whole file all together because we don't know how much memory is available in our system
        #by using 10240, we can limit the size of the file when we read and copy it
        buf = infile.read(10240) #10kbytes(very small in the system)
        if buf:
            outfile.write(buf)
            print('.', end='', flush=True)
        else: break
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()
