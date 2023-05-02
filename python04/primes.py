#!/bin/python3
import random as ran
#Determine the prime numbers in a random list
#Save the primes to a text file

#define a function to generate a random list
def random_list(first,last,size):
    return ran.sample(range(first,last),size)

#check if a number is prime - use the none pattern
def is_prime(n):
    for e in range(2,n):
        if n%e == 0:
            return False
    return True

#Determine the prime numbers in a list - every pattern
def prime_list(numbers):
    primes = []
    for e in numbers:
        if is_prime(e):
            primes.append(e)
    return primes

#save the prime list to a text file
def save_to_file(file,data):
    handler = open(file,"a+")
    for line in data:
        handler.write(str(line))
        handler.write("\n")
    handler.close()

def run():
    first = int(input("First: "))
    last = int(input("Last: "))
    size = int(input("Size: "))
    numbers = random_list(first,last,size)
    print(numbers)
    primes = prime_list(numbers)
    file = input("File: ")
    save_to_file(file, primes)
run()

