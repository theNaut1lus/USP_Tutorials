# simulate CPU usage readings randomly
# plot the CPU usage using a bar graph

import random as ran
import matplotlib.pyplot as plt

n = int(input("Number of CPUs = "))

usage = {} # dictionary to store cpu-usage
cpu = "CPU"

i = 1
while i <= n:
    currentCPU = cpu+str(i)  # dictionary keys (CPU<integer>)
    usage[currentCPU] = ran.randint(1,100) #random CPU usage values
    i += 1

X = range(len(usage))
Y = list(usage.values())
labels = list(usage.keys())

plt.bar(X,Y,tick_label=labels,width=0.4,color='green')
plt.show()