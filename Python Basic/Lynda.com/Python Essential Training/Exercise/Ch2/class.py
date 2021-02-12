#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#self: reference to the object
class Duck:
    sound = "Quack"
    walking = "Walks like a duck."

    def quack(self):
        print(self.sound)

    def walk(self):
        print(self.walking)

def main():
    #donald is an object
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == '__main__': main()
