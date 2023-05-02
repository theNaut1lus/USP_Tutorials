#Calculate the Pythagorean hypotenuse
#Calculate the distance between 2 points
#Calculate the displacement based on time, speed and acceleration

import math as m 

#return the hypotenuse from sides a and b
#functions with return value should not read from STDIN
#functions with return value should not read from argv
#functions with return value should not print
def hypotenuse(a,b):
    return m.sqrt(pow(a,2) + m.pow(b,2)) 

#procedure to show the hypotenuse
def showHypotenuse():
    a = int(input("a = "))
    b = int(input("b = "))
    print(hypotenuse(a,b)) 
    
def distance(x1,y1,x2,y2):
    return m.sqrt(pow((x2-x1),2)+m.pow((y2-y1),2))

#procedure to show the distance
def showDistance():
    x1 = int(input("x1 = "))
    y1 = int(input("y1 = "))
    x2 = int(input("x2 = "))
    y2 = int(input("y2 = "))
    print(distance(x1,y1,x2,y2)) 
    
#switcher menu to select execution path
def switch(choice):
    if choice == "h":
        showHypotenuse()
    elif choice == "d":
        showDistance()
    else:
        print("Unknown command!")
        
def run():
    choice = input("Command (h/d/x): ")
    while choice != "x":
        switch(choice)
        choice = input("Command (h/d/x): ")
    print("Thank you")
    
run()