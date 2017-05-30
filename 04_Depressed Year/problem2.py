import pandas as pd
import operator
from bokeh.charts import Donut, Bar, show, vplot, Line, output_file

df = pd.read_csv("aviationdataset.csv", encoding ='latin1').fillna(0)
print("file loaded")

df['Location'] = df['Location'].apply(lambda word: str(word)[-2:])
us_states = df.loc[df['Country'] == 'United States']['Location'].unique()

injury_dict = {}
for state in us_states:
    injury_dict.update({ state : sum(df[df['Location'] == state][cat]) for cat in ['Total.Fatal.Injuries', 'Total.Serious.Injuries', 'Total.Minor.Injuries']} )
result_dict = dict(sorted(injury_dict.items(), key=operator.itemgetter(1), reverse=True)[:5])
x, y = zip(*sorted(result_dict.items()))
data = pd.Series(y, x)
bar2 = Bar(data, title="Top 5 States Of Aviation Injuries", plot_width=400)

p = vplot(bar2)
show(p)