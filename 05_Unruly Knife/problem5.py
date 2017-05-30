from __future__ import division
import requests
import os
import csv
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
import collections
from pylab import *
import warnings
warnings.filterwarnings('ignore')
import matplotlib
matplotlib.use('Agg')



# if dataset does not exist locally, download it
if not os.path.exists(filename):
    response = requests.get(url, params={'downloadformat': 'csv'})

    if response.ok:
        with open(filename, 'wb') as f:
            f.write(response.content)

age_distribution = {}

with open(filename, encoding='latin-1') as file:
    reader = csv.reader(file)
    next(reader)  # skip headers

    for row in reader:
        age = int(row[2])
        persons = int(row[5])
        age_distribution.setdefault(age, 0)
        age_distribution[age] += persons

# create plot
plt.bar(list(age_distribution.keys()), list(age_distribution.values()), width=0.5, linewidth=0, align='center', color='blue')
plt.ticklabel_format(useOffset=False)
plt.title('Age distribution in Copenhagen', fontsize=12)
plt.xlabel('Ages', fontsize=10)
plt.ylabel('Amount of people', fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.savefig('age_distribution.png', bbox_inches='tight')
