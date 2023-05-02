#Read data from students.csv
#Write rows to students.csv

import csv 

def readCSV(file):
    with open(file,'r') as f:
        csvReader = csv.reader(f)
        for row in csvReader:
            print(row)
        
# with open('students.csv','r') as f:
#     csvReader = csv.reader(f)
#     for row in csvReader:
#         print(row)

def writeCSV(file,id,name,mark,grade):
    with open(file,'a',newline='') as f:
        csvWriter = csv.writer(f)
        row = [id,name,mark,grade]
        csvWriter.writerow(row)    
    
# with open('students.csv','a') as f:
#     csvWriter = csv.writer(f)
#     row = [123456,"Tim Cahill",50,'P']
#     csvWriter.writerow(row)

def grade(mark):
    if mark >= 85:
        g = "HD"
    elif mark >= 75:
        g = "D"
    elif mark >= 65:
        g = "C"
    elif mark >= 50:
        g = "P"
    else:
        g = "Z"
    return g
    
def run():
    file = input("File: ")
    id = int(input("ID: "))
    name = input("Name: ")
    mark = int(input("Mark: "))
    g = grade(mark)
    writeCSV(file,id,name,mark,g)
    readCSV(file)
    
run()