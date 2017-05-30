import pandas as pd
from bokeh.charts import Donut, Bar, show, vplot, Line, output_file
from tqdm import tqdm

df = pd.read_csv("aviationdataset.csv", encoding ='latin1').fillna(0)
print("file loaded")

cols = ['Event.Date', 'Total.Fatal.Injuries']
workframe = df[cols]
twenty_year_fatalities = {}
this_year = 2017

for idx, row in tqdm(workframe.iterrows()):
    temp_stamp = int(row['Event.Date'][:4])
    if row['Total.Fatal.Injuries'] == '0' or temp_stamp < this_year - 20:
        continue
    if temp_stamp in twenty_year_fatalities.keys():
        twenty_year_fatalities[temp_stamp] += row['Total.Fatal.Injuries']
    else:
        twenty_year_fatalities.update({temp_stamp:row['Total.Fatal.Injuries']})
twenty_year_stats = []

for k, v in twenty_year_fatalities.items():
    twenty_year_stats.append((k,v))
twenty_year_stats.sort(reverse=False)

result_df = pd.DataFrame(twenty_year_stats, columns=['Year', 'Fatalities'])

result_dict = {}
for row in result_df.itertuples():
    result_dict.update({ row[1] : row[2]})

mx, my = zip(*sorted(result_dict.items()))
result_data = pd.Series(my, mx)
chart = Line(result_data, title="Fatal Injury Distribution", legend="top_right", ylabel='Number of Fatalities', xlabel='Year')

p = vplot(chart)
show(p)