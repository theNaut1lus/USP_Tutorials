#!/bin/python3
import math as m

#read a radius from STDIN
#calculate the perimeter, area, volume for a radius r
#display the result in the main function

#def function_name(parameters):  (function must be a verb)
#    //code

#def function_name(paramters):   (function name should be a noun)
#   //code
#   return value(s)

#read and return the  radius
def radius(prompt):
    return float(input(prompt))

#function to calculate and return 3 gemotrical values
def geo_values(radius):
    perimeter = 2*m.pi*radius 
    area = m.pi*m.pow(radius,2)
    volume = (4/3)*m.pi*m.pow(radius,3)
    return perimeter, area,volume

#main function will call the above
def main():
    r = radius("Radius: ")
    p, a, v = geo_values(r)
    print(f'Perimeter = {p}')
    print(f'Area = {a}')
    print(f'Volume = {v}')
main()