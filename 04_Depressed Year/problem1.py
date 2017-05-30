import pandas as pd
from bokeh.charts import Donut, Bar, show, vplot, Line, output_file

df = pd.read_csv("aviationdataset.csv", encoding ='latin1').fillna(0)
print("file loaded")

fatality_dict = {}
for phase in df['Broad.Phase.of.Flight'].unique():
     if phase != 0:
         fatality_dict.update({ phase : sum(df[df['Broad.Phase.of.Flight'] == phase]['Total.Fatal.Injuries']) / len(df[df['Broad.Phase.of.Flight'] == phase]) * 100})
x, y = zip(*sorted(fatality_dict.items()))
data = pd.Series(y, x)
pie_chart = Donut(data, plot_width=800, plot_height=800, title="How do the flight phases (ex. take off, cruise, landing..) contribute to fatalities?")

p = vplot(pie_chart)
show(p)
