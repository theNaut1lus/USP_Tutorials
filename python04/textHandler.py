#!/bin/python3

#define a function to read and show the data from a file
def read_text(file):
    f = open(file,"r")
    print(f.read())
    f.close()

#Define a function to write text to a file
def write_text(data,file):
    f = open(file,"a+")
    f.write(data+"\n")
    f.close()

def run():
    file = input("File: ")
    data = input("Data: ")
    write_text(data,file)
    read_text(file)
run()