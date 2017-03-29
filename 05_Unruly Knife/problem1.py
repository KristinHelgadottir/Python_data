import webget as wg
import pandas as pd

url = 'http://data.kk.dk/dataset/9070067f-ab57-41cd-913e-bc37bfaf9acd/resource/9fbab4aa-1ee0-4d25-b2b4-b7b63537d2ec/download/befkbhalderkoencivst.csv'

#wg.download(url) uncomment it so it downloads the csv file

filename = url.split("/")[-1]

data_set = pd.read_csv(filename)