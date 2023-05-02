#!/bin/env python3
import math as m 
import statistics as stat 
import random as r 

#general read function 
def read(action):
    return input(action+": ")

def generate(first,last,howmany):
    return r.sample(range(first,last),howmany)

def createdict():
    names={}
    keys = r.sample(range(100,1000),4)
    for key in keys:
        names[key] = read("Name")
    return names

def sort(dicts):
    for key in dicts.keys():
        print("%s :: %s"%(key,dicts[key]))

def update(dicts,key,newvalue):
    dicts[key] = newvalue

def delete(dicts,key):
    del dicts[key]





























