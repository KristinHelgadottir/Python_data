# importing all the nececary libraries

import os # os module
import webget
import csv
from urllib.parse import urlparse
import pandas as pd # read data from a csv file, making dataframe object
import numpy as np # to initialize a one-dimensional NumPy array

# downloading dataset using webget
sat_url = "https://github.com/stinaanita/python_data/blob/master/database.csv"
#def download(sat_url):
    #webget.download(sat_url)
    #return os.path.basename(urlparse(sat_url).path)
file = 'satdata.csv'
data = pd.read_csv(file)
