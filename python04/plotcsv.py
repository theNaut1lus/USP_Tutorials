import matplotlib.pyplot as plt
import csv
import collections 
import numpy as np

grades = [] # use this list to store the grades from CSV

with open('students.csv','r') as f:
    rows = csv.reader(f,delimiter=',')
    next(rows) #skip the header of the CSV file
    for row in rows:
        grades.append(row[3]) # collect the grades
        
counter = collections.Counter(grades)   #determine the frequency of grades
frequency = counter.values()
gradeset = np.unique(np.array(grades)) # collect the unique names (grades)

plt.pie(frequency,labels=gradeset, autopct='%.2f%%')
plt.title('Grades Distribution',fontsize = 20)
plt.legend(title='Grades:')
plt.show()