# Open a text file and write strings from STDIN
# Open that file and read line by line to STDOUT

def writeText(file,data):
    f = open(file, "a")
    f.write(data+"\n")
    f.close()
    
# f = open("demo.txt", "a")
# s = input("String: ")
# f.write(s+"\n")
# f.close()

def readText(file):
    f = open(file, "r")
    print(f.read())
    f.close()

# f = open("demo.txt", "r")
# print(f.read())
# # for line in f:
# #     print(line)
# f.close()

def run():
    file = input("File: ")
    data = input("String: ")
    writeText(file,data)
    readText(file)

run()