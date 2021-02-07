#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#dictionary:
# -created using sequance of keywords
# -also known as associative array or hashed array
# -created using curly brackets
# -key : value

def main():
    #using dictionary constructor (more convenient)
    animals = dict(kitten= 'meow', puppy= 'ruff!', lion= 'grrr',
        giraffe= 'I am a giraffe!', dragon= 'rawr')
    #print keys
    for k in animals.keys():
        print(k)
    #search items by using key instaed of index
    print(animals["lion"])
    #change values
    animals["lion"] = "I'm a lion"
    #add new element
    animals["monkey"] = "haha"
    #search key by uisng the in operator
    print("lion" in animals)
    #search key by using conditional expression
    print("found!" if "lion" in animals else "nope!")
    #search for key that is not exist without ant exception
    print(animals.get("godzilla"))
    #normal way to create dictionary
    animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
        'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }
    print_dict(animals)

def print_dict(o):
    #for x in o: print(f'{x}: {o[x]}')
    #readable way to print keys and values
    for k, v in o.items(): 
        print(f"{k}: {v}")

if __name__ == '__main__': main()
