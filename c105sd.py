import math
import csv
from os import times
import statistics 

with open("data.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0] 
def mean(data) :
    n = len(data)
    total = 0
    for x in data :
        total += float(x)
    mean = total/n
    return mean
    
squared_list = []
for i in data :
    a = int(i) - mean(data)
    a = a**2 
    squared_list.append(a)

sum = 0
for n in squared_list :
    sum = sum + n 
print(sum)
result = sum/(len(data) -1) 

std_deviation = math.sqrt(result) 
print(std_deviation) 
#std = statistics.stdev(file_data)
#print("sd using pre-defined function", std) 