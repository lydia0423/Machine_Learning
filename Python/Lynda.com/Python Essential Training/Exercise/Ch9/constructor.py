#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Animal:
    #constructor by using __init__
    #the first arg is self which means it is an object method that references to itself
    def __init__(self, type, name, sound):
        #return the object variable in _name format (private variable but Python don't have it)
        self._type = type
        self._name = name
        self._sound = sound

    #another way to assign the paramter without following the orders
    def __init__(self, **kwargs):
        self._type = kwargs["type"] if "type" in kwargs else "kitten"
        self._name = kwargs["name"] if "name" in kwargs else "fluffy"
        self._sound = kwargs["sound"] if "sound" in kwargs else "rawr"

    def type(self):
        return self._type #accessor

    def name(self):
        return self._name

    def sound(self):
        return self._sound

def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an Animal')
    print('The {} is named "{}" and says "{}".'.format(o.type(), o.name(), o.sound()))


def main():
    a0 = Animal('kitten', 'fluffy', 'rwar')
    a1 = Animal('duck', 'donald', 'quack')
    #by using kwagrs
    a2 = Animal(type = "dog", name = "bert", sound = "wou")
    print_animal(a0)
    print_animal(a1)
    print_animal(a2)
    print_animal(Animal('velociraptor', 'veronica', 'hello'))

if __name__ == '__main__': main()
