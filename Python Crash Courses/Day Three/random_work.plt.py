import pandas as pd
import matplotlib.pyplot as plt
from random import choice
class Randomwalk :
    def __init__(self,num_points =500):
        
        ##initializing the attribute
        self.num_points =num_points
        self.x_values =[0]
        self.y_values =[0]
        
    def fill_work(self):
        while len(self.x_values) < self.num_points:
            x_direction =choice([1,-1])
            x_distance =[0,1,2,3,4]
            x_step = x_direction * x_distance
            y_direction = choice([1,-1])
            y_distance =[0,1,2,3,4]
            y_step = y_direction *y_distance

            if x_step == 0 and y_step ==0: 
                continue
            x =self.x_values[-1] +x_step
            y= self.y_values[-1]+y_step
            self.x_values.append(x)
            self.y_values.append(y)
input_values =[1,2,3]
squares = [1,2,9]

