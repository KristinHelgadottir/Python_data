import pandas as pd
from bokeh.charts import Donut, Bar, show, vplot, Line, output_file
import operator

df = pd.read_csv("aviationdataset.csv", encoding ='latin1').fillna(0)
print("file loaded")

minor_dict = dict.fromkeys(df['Model'].unique(), 0)
serious_dict = dict.fromkeys(df['Model'].unique(), 0)
fatal_dict  = dict.fromkeys(df['Model'].unique(), 0)

for row in df.itertuples():
     minor, serious, fatal = [int(row[cat]) for cat in [24, 25, 26]]
     flight_model = row[16]

     minor_dict.update({ flight_model : minor_dict.get(flight_model) + minor})
     serious_dict.update({ flight_model : serious_dict.get(flight_model) + serious})
     fatal_dict.update({ flight_model : fatal_dict.get(flight_model) + fatal})

# Plotting
mx, my = zip(*sorted(minor_dict.items(), key=operator.itemgetter(1), reverse=True)[:5])
sx, sy = zip(*sorted(serious_dict.items(), key=operator.itemgetter(1), reverse=True)[:5])
fx, fy = zip(*sorted(fatal_dict.items(), key=operator.itemgetter(1), reverse=True)[:5])
minor_data = pd.Series(my, mx)
serious_data = pd.Series(sy, sx)
fatal_data = pd.Series(fy, fx)

minor_chart, serious_chart, fatal_chart = [Donut(data[0], plot_width=400, title=data[1] ,plot_height=400) for data in [[minor_data, 'Minor Data'], [serious_data, 'Serious Data'], [fatal_data, 'Fatal Data']]]

p = vplot(minor_chart, serious_chart, fatal_chart)
show(p)