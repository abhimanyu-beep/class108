import pandas as px 
import csv
import plotly.figure_factory as ff
df=px.read_csv("dt.csv")
figure=ff.create_distplot([df["Height(Inches)"].tolist()],["Height"],show_hist=False)
figure.show()