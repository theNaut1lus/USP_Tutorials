#!/bin/python3
import statistics as stat
import random as rand

#define a function to generate a random list
def random_list(first,last,size):
    return rand.sample(range(first,last),size)

#define a function to return mean, stdv, variance
def stat_values(*argv):
    mean = stat.mean(*argv)
    stdv = stat.stdev(*argv)
    var = stat.variance(*argv)
    return mean, stdv, var

def main():
    first = int(input("First: "))
    last = int(input("Last: "))
    size = int(input("Size: "))
    numbers = random_list(first,last,size)
    print(numbers)
    m, s, v = stat_values(numbers)
    print(f'Mean = {m}')
    print(f'Stdev = {s}')
    print(f'Variance = {v}')

main()