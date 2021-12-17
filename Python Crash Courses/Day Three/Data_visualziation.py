###Data visualization 

import matplotlib.pyplot as plt
data =[1,2,4,8,16,32,64]
fig,ax = plt.subplots()
ax = plt.plot(data)
plt.show()

import matplotlib.pyplot as plt
import numpy as npp
data =[1,2,4,8,16,32,64]
fig,ax = plt.subplots()
ax.set_title("Numbes by 2")
ax.set_xlabel("Value")
ax.set_ylabel("Output value")
ax.plot(data)
 
plt.show()

## Square data 
input_values =[1,2,3,4]
square = [1,4,9,16]

fig,ax = plt.subplots()
ax.plot(input_values,square)
plt.show()

##check avaliable plot styles 
plt.style.available

## 'tableau-colorblind1' Style
plt.style.use('tableau-colorblind10')
input_values =[1,2,3,4]
square = [1,4,9,16]

fig,ax = plt.subplots()
ax.plot(input_values,square)
plt.show()

##ploting single using scatter() function  
plt.style.use('tableau-colorblind10')
fig,ax = plt.subplots()
## scatter index 1for input_values and 1 square 
ax.scatter(2,4)

##using index 
plt.style.use('tableau-colorblind10')
fig,ax = plt.subplots()
input_values =[1,2,3,4]
square = [1,4,9,16]
ax.scatter(input_values[3],square[3])
plt.show()

##ploting series of points with scatter()
import matplotlib.pyplot as plt
input_values =[1,2,3,4]
square = [1,4,9,16]
plt.style.use('tableau-colorblind10')
fig,ax = plt.subplots()
ax.set_title("Ploting Series of points with scatter")
ax.set_xlabel("Values")
ax.set_ylabel("Square numbers")
ax.scatter(input_values,square)
 
plt.show()


## using loop to generate the square numbers 
input_values =range(1,20)
output_values = [i**2 for i in input_values]

input_values0 =range(1,10)
output_values0 = [i**2 for i in input_values0]
plt.style.use('tableau-colorblind10')
fig,ax = plt.subplots()
ax.set_title("Using for loop to generate square numbers")
ax.set_xlabel("Values")
ax.set_ylabel("Output")
ax.scatter(input_values,output_values,c='blue')
 
####ax.scatter(input_values,outp)
plt.show()