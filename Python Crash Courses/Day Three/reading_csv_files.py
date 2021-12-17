
##Reading CSV File using read method 
import datetime
import matplotlib.pyplot as plt
from datetime import datetime

file_name ='C:/Users/Ismail/Python Challange/Data Scienc/Python Crash Courses/Day Three/data.csv'
with open(file_name) as file_object:
 reader = file_object.read()
 ######print(reader)


## using csv library
import csv
from os import read
##empty_list =[]
with open(file_name) as file_object :
     reader = csv.reader(file_object)
     header_row= next(reader)
     ##empty_list.append(header_row)
     print(header_row)
##Printing the index of the headers 

for index,header_name in enumerate (header_row):
    ## enumureate function allows you to return both index of each item and the value of the list 
    print(index,header_name)

## Reading temperature colum data


temperature =[]
with open (file_name) as file_object:
    data_holder = csv.reader(file_object)
    header_row= next(data_holder)

    for row in data_holder:
        temperature_col = int(row[7])
        temperature.append(temperature_col)
    print(temperature)

## plotting the data into graph 
fig,ax = plt.subplots()
ax.set_title("Daily Temperature")
ax.set_ylabel("Temperature")
ax.set_xlabel("")
ax.plot(temperature)
plt.show()
