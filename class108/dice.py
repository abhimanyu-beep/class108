import random
import plotly.figure_factory as ff
import plotly.express as px
import csv
diceresult=[]
count=[]

for i in range(0,100):

    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    diceresult.append(dice1+dice2)
    count.append(i)
figure=ff.create_distplot([diceresult],["result"])
figure.show()
    
