#!/bin/env python3

import util as u 

def dictops():
    names = u.createdict()
    u.sort(names)
    key = int(u.read("Key"))
    value = u.read("Value")
    u.update(names,key,value)
    u.sort(names)
    key = int(u.read("Delete by Key"))
    u.delete(names,key)
    u.sort(names)

def main():
    circleops()
    dictops()

main()









