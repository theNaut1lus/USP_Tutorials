#Define a function that reads a number N from STDIN
#Define a function that determines the max N until -1 is entered
#Define a function that calculates the sum-series of N
#Define a function that calculates the factorial of N
#Define a main function that runs your program
import math as m
import random as r
import statistics as stat

def readValue(prompt):
    return int(input(prompt))

def generate(first,last,howmany):
    return r.sample(range(first,last),howmany) #select a population between first and last with size howmany

def calculateStats(*argv):
    mean = stat.mean(*argv)
    stdv = stat.stdev(*argv)
    variance = stat.variance(*argv)
    return mean,stdv ,variance
      
def main():
    n = readValue("N = ")
    first = readValue("First = ")
    last = readValue("Last = ")
    howmany = readValue("How Many = ")    
    mylist = generate(first,last,howmany)
    print(mylist)
    
    print("Max = {} ".format(max(mylist)))
    print("Sum Series({}) = {}".format(n,sum(mylist)))
    print("Factorial({}) = {}".format(n,m.factorial(n)))
    
    mean, stdv, variance = calculateStats(mylist)
    print("Mean = {:.2f} and STDV = {:.2f} and Variance = {:.2f} ".format(mean,stdv,variance))
    
main()