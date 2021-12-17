from randomwork import Randomwalk
import matplotlib.pyplot as plt 

random_work = Randomwalk()
random_work.fill_walk()

fig,ax = plt.subplots()
ax.scatter(random_work.x_values,random_work.y_values)
plt.show()