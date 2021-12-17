from landu import Die
import matplotlib.pyplot as plt
import plotly
from plotly import offline
die = Die()
results =[]
for i in range(1000) :
    result=die.roll()
    results.append(result)
 


frequences =[]
 
for value in range(1,die.num_dice+1):
    frequence= results.count(value)
    frequences.append(frequence)
    print(frequences)


##visualizing the dice numbers
 # Visualize the results.
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 1000 times',
        xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')