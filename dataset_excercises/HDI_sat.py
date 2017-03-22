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


# getting the human development dataset
filename = './human_development.csv'
array_of_stats = pd.read_csv(filename)
dd = array_of_stats.as_matrix()


# 1.Which country has the highest HDI (Human Development Index) and which has the lowest?
highest_HDI = np.max(dd[:,2])
print(highest_HDI) # in data set its 0.944
lowest_HDI = np.min(dd[:,2])
print(lowest_HDI)

for d in dd:
    if d[2] == highest_HDI:
        print("{} has the highest Human Development Index".format(d[1])) #country col 1
    if d[2] == lowest_HDI:
        print("{} has the lowest Human Development Index".format(d[1]))
        
        
# OUTPUT:
#0.9440000000000001
#0.348
#Norway has the highest Human Development Index
#Niger has the lowest Human Development Index


import ast # to parse string into float

# 2.Which country has raised its HDI the most, in the period 1990 to 2014?
 
filename2 = './historical_index.csv'
array_of_stats = pd.read_csv(filename2)
array_of_stats

growth = []
my_array = []
dd = array_of_stats.as_matrix()
for d in dd:
    if d[2] == '..' or d[3] == '..': # getting rid of ..
        d2 = 0
        result = d[8] - d2 #nr 8 =2014
        growth.append(result) # adding to growth array
        my_array.append(d[1])
        my_array.append(result)
    else:
        d2 = ast.literal_eval(d[2])
        result = d[8] - d2
        growth.append(result)
        my_array.append(d[1])
        my_array.append(result)
highest_increase = np.max(growth)

for e in my_array:
    if e == highest_increase:
        country = my_array.index(highest_increase) - 1
        print("{} has increased the most by {}".format(my_array[country], highest_increase))
        
# OUTPUT
#Liechtenstein has increased the most by 0.9079999999999999


# 3.Which country has the most satelites for military usage?

dd2 = data.as_matrix()
military = []
for d in dd2:
    if d[4] == 'Military':
        military.append(d)
military = np.array(military)
countries = np.unique(military[:,3])

my_array = []

for c in countries:
    for m in military:
        if m[3] == c:
            my_array.append(m)
    my_array_size = len(my_array)
    my_array = []
    print("{} has {} satelites for military use".format(c, my_array_size))
   
# 4.Wich country has the lightest satelite and how much does it weight?

dd = pd.DataFrame(dd).fillna(0.0) # makes NaN into 0
dd = np.array(dd)
new_array = []


def conv(val): # converting to floats ???
    if not val:
        return 0    
    try:
        return np.float64(val)
    except:        
        return np.float64(0)
#data = pd.read_csv(file, converters={'Users':conv,'Dry mass':conv})


for d in dd:
    if d[16] == 0.0: # if in row 16 is null, pass
        pass
    else:
        new_array.append(d)
new_array = np.array(new_array)
#pd.DataFrame(new_array)
n = new_array[:,16]
n
