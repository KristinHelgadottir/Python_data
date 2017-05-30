import os
import requests
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

url = 'http://data.kk.dk/dataset/9070067f-ab57-41cd-913e-bc37bfaf9acd/resource/9fbab4aa-1ee0-4d25-b2b4-b7b63537d2ec/download/befkbhalderkoencivst.csv'
filename = url.split('/')[-1]

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