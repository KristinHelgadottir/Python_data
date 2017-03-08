import os #os module
import webget
import pprint
import csv
from urllib.parse import urlparse
import pandas as pd
import numpy as np # to initialize a one-dimensional NumPy array

url = 'https://raw.githubusercontent.com/DaMexicanJustice/frantic_midnight/master/data%20sets/vgsales.csv'
def download(url):
    webget.download(url)
    return os.path.basename(urlparse(url).path)

filename = './vgsales.csv'
stats_df = pd.read_csv(filename)
dd = stats_df.as_matrix() # making data file as matrix


#Which platform is the most popular in the regions NA, EU and Japan?
region = {1: 'North America', 2: 'Europe Union', 3: 'Japan'}
pl_mask = (dd[:,2]) # ---------------- TODO platform mask
# getting all the sales from NA, EU and JP
na_keys = np.unique(dd[:,6]) 
eu_keys = np.unique(dd[:,7]) 
jp_keys = np.unique(dd[:,8]) 

msg = 'The highest sales in {} is {} on platform {}'
print(msg.format(region[1], na_keys.max(), pl_mask))
print(msg.format(region[2], eu_keys.max(), pl_mask))
print(msg.format(region[3], jp_keys.max(), pl_mask))


# How big a share of the global sales does the US sales cover?
na_sales_mask = (dd[:,6])
global_sales_mask =(dd[:,10])
na_sum = np.sum(na_sales_mask)
global_sum = np.sum(global_sales_mask)
covarage = int(round(na_sum / global_sum *100))
print("North America covers the {}% of the global sales".format(covarage))


# Which game genre is the most popular in 2012?
year_mask = (dd[:,3] == 2012)
g = np.max(dd[year_mask][:,4])
msg = 'Most popular game genre in 2012 is {}'
print(msg.format(g))


# Which publisher has the most titles in top 100?-----------TODO
publisher_row = (dd[:,5])
name_row = (dd[:,1])
rank_row = (dd[:,0])
top_100 = rank_row[0:100]

top_pub = np.array()
# text = '{} publisher has the most titles in top 100'
# print(text.format(df.max()))
print(top_pub)

