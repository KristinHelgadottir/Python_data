#Find the three most populated city parts(BYDEL), in 1992, 2000 and 2015
import webget as wg
import pandas as pd

url = 'http://data.kk.dk/dataset/9070067f-ab57-41cd-913e-bc37bfaf9acd/resource/9fbab4aa-1ee0-4d25-b2b4-b7b63537d2ec/download/befkbhalderkoencivst.csv'

wg.download(url)

filename = url.split("/")[-1]

d = pd.read_csv(filename)
data_set = d.as_matrix()

years = [1992, 2000, 2015]
popultaion_dict = {}
popultaion_arr = []


for y in years:
    year_mask = data_set[:,0] == y
    for d in data_set[year_mask]:
        bydel = d[1]
        if bydel not in popultaion_dict.keys():
            popultaion_dict[bydel] = 1
        else:
            popultaion_dict[bydel] += 1
    popultaion_arr.append(popultaion_dict)
    popultaion_dict = {}
