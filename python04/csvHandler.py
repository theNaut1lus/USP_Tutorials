#!/bin/python3
import csv 

#define a function to read rows from a csv file
def read_csv(file):
    with open(file,"r") as f:
        csvReader = csv.reader(f)
        for row in csvReader:
            print(row)

def grade(mark):
    if mark >= 85:
        g = "HD"
    elif mark >= 75:
        g = "D"
    elif mark >= 65:
        g = "C"
    elif mark >= 50:
        g = "C"
    else:
        g = "Z"
    return g

#define a function to write a row to a csv file
def write_csv(file,ID,name,mark):
    with open(file,"a",newline='') as f:
        csvWriter = csv.writer(f)
        row = [ID,name,mark,grade(mark)]
        csvWriter.writerow(row)


def run():
    file = input("File: ")
    name = input("Name: ")
    ID = input("ID: ")
    mark = int(input("MarK: "))
    write_csv(file,ID,name,mark)
    read_csv(file)
run()