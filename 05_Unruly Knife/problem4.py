from __future__ import division
import requests
import os
import csv
from pprint import pprint
import matplotlib.pyplot as plt
import numpy as np
import collections
from pylab import *


def getFile(url):
    fname = url.split('/')[-1]

    if os.path.isfile(fname):
        print("File found.")
    else:
        response = requests.get(url, params={'downloadformat': 'csv'})
        if response.ok:  # status_code == 200:
            with open(fname, 'wb') as f:
                f.write(response.content)
        print('Downloaded {}'.format(fname))
    return fname


def plotPieChart(mydict, title_param='Change me..'):
    val_sum = sum(mydict.values())
    values = mydict.values()
    fractions = [val * 100 / val_sum for val in values]

    # make the plot
    figure(1, figsize=(7, 7))
    labels = mydict.keys()
    pie(fractions, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    title(title_param)
    figtext(.02, .1,
            "E=Widdow\nF=Divorced\nG=Maried\nL=Oldest living partner\nO=Dissolved partnership\nP=Registered partnership\nU=Unmarried")
    show()


# get file to work with
url = 'http://data.kk.dk/dataset/9070067f-ab57-41cd-913e-bc37bfaf9acd/resource/9fbab4aa-1ee0-4d25-b2b4-b7b63537d2ec/download/befkbhalderkoencivst.csv'
fname = getFile(url)

with open(fname) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    statuses_2000 = {}
    statuses_2015 = {}

    for row in reader:
        year = int(row[0])
        bydel = int(row[1])
        no_ppl = int(row[5])

        if bydel in [1, 2, 3]:
            status = row[3]

            if year == 2000:
                if status not in statuses_2000.keys():
                    statuses_2000[status] = no_ppl
                else:
                    statuses_2000[status] += no_ppl
            if year == 2015:
                if status not in statuses_2015.keys():
                    statuses_2015[status] = no_ppl
                else:
                    statuses_2015[status] += no_ppl

    plotPieChart(statuses_2000, 'Marital statuses in 2000')
    plotPieChart(statuses_2015, 'Marital statuses in 2015')
    # print(statuses_2000)
    # print(statuses_2015)