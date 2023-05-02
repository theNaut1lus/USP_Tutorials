#Read JSON data into a data dump
#Show the JSON data as string
import json 
import csv

def readJSON(file):
    f = open(file,'r')
    json_obj = json.load(f)
    f.close()
    return json_obj

def showJSON(object):
    print(json.dumps(object,indent=4))
    
def csvHandler(csvFile):
    f = open(csvFile,'r')
    reader = csv.DictReader(f)
    return reader

def csvList(reader):
    data = []
    for row in reader:
        data.append(row)
    return data

def saveJSON(jsonFile,dataList):
    f = open(jsonFile,'w+')
    f.write(json.dumps(dataList,indent=4))
    f.close()
    
def run():
    jsonFile = input("JSON File: ")
    csvFile = input("CSV File: ")
    reader = csvHandler(csvFile)
    data = csvList(reader)
    saveJSON(jsonFile,data)
    object = readJSON(jsonFile)
    showJSON(object)
    
run()
