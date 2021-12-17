import csv
import matplotlib.pyplot as plt
from datetime import datetime
file_name ='C:/Users/Ismail/Python Challange/Data Scienc/Python Crash Courses/Day Three/haye.csv'

## opening the file 
with open(file_name) as file_object :
    weather_data = csv.reader(file_object)
    headers = next(weather_data)
    print(headers)

## Print the index and the value of the headers 

for index, values in enumerate(headers):
     print(index,values)

### Printing the temperature data
temperature =[]
with open (file_name) as file_object:
    data_holder = csv.reader(file_object)
    header_row= next(data_holder)

    for row in data_holder:
        temperature_col = row[6]
        temperature.append(temperature_col)
    print(temperature)

##ploting the temperature data 

fig,ax = plt.subplots()
ax.set_title("July Temperature")
ax.set_ylabel("Temperature")
ax.plot(temperature)
##plt.show()

## Reading the dates

Dates =[]

with open(file_name) as dates :
    taarikh = csv.reader(dates)
    header = next(taarikh)

    for i in taarikh :
        date_col = i[3]
        Dates.append(date_col)
    print(Dates)

##plot the date 
fig,ax = plt.subplots()
ax.set_title("July Month")
ax.plot(Dates,Dates)
##plt.show()

plt.style.use("seaborn")
fig,ax = plt.subplots()
ax.plot(Dates,temperature)
plt.title(" Daily temperatures in July")
plt.xlabel('',fontsize=12)
fig.autofmt_xdate()
plt.ylabel("Temperature")
plt.show()