import random 
import plotly.figure_factory as ff 
import pandas as pd 

"""
sum = []
for i in range(100):
     dice1 = random.randint(1,6)
     dice2 = random.randint(1,6)
     sum.append(dice1 + dice2)
fig = ff.create_distplot([sum] , ["Dice Answers"])
fig.show()
"""

data = pd.read_csv('./data.csv')

"""
heigth = data["Height(Inches)"]
heigthdata = heigth.tolist()
heigthgraph = ff.create_distplot([heigthdata] , ["Heigth"])
heigthgraph.show()
"""

weigth = data["Weight(Pounds)"]
weigthdata = weigth.tolist()
weigthgraph = ff.create_distplot([weigthdata],["Weigths"])
weigthgraph.show()