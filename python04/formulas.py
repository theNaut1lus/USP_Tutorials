#!/bin/python3

import math as m

#determine the hypothenuse of a triangle 
def hypothenuse(a,b):
    return m.sqrt(pow(a,2)+pow(b,2))

def show_hypothenuse():
    a = int(input("a = "))
    b = int(input("b = "))
    print(f'Hypothenuse = {hypothenuse(a,b)} ')

#determine the distance between (x1,y1) and (x2, y2)
def distance(x1,x2,y1,y2):
    return m.sqrt(pow(x1-x2,2)+pow(y1-y2,2))

def show_distance():
    x1 = int(input("X1 = "))
    y1 = int(input("Y1 = "))
    x2 = int(input("X2 = "))
    y2 = int(input("Y2 = "))
    print(f'Distance = {distance(x1,x2,y1,y2)} ')

#calcuate the distance based on speed and time
def position(v,t):
    return v*t 

def show_position():
    v = int(input("v = "))
    t = int(input("t = "))
    print(f'Position = {position(v,t)} ')

def switch(choice):
    if choice == "h":
        show_hypothenuse()
    elif choice == "d":
        show_distance()
    elif choice == "p":
        show_position()
    else:
        print("Unknown choice")

def main():
    choice = input("Choice(h/d/p/x): ")
    while(choice != "x"):
        switch(choice)
        choice = input("Choice(h/d/p/x): ")
    print("Thank you")
    
main()