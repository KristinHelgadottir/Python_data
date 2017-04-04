#Create to pie-charts, showing the distribution of marital status' in bydel 1, 2 and 3 in year 2000 and 2015
import webget as wg
import pandas as pd
import operator as op

url = 'http://data.kk.dk/dataset/9070067f-ab57-41cd-913e-bc37bfaf9acd/resource/9fbab4aa-1ee0-4d25-b2b4-b7b63537d2ec/download/befkbhalderkoencivst.csv'

wg.download(url)

filename = url.split("/")[-1]

d = pd.read_csv(filename)
data_set = d.as_matrix()

years = [2000, 2015]
bydel = [1, 2, 3]
marital_status = []

for y in years:
    year_mask = data_set[:,0] == y
    for d in data_set[year_mask]:
        b = d[1]
        m = d[3]
        if b in bydel:
           marital_status.append(d)
print(marital_status)
            



