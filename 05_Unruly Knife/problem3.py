#Find the three most populated city parts(BYDEL), in 1992, 2000 and 2015
import webget as wg
import pandas as pd
import operator as op

d = pd.read_csv(filename)
data_set = d.as_matrix()

years = [1992, 2000, 2015]
bydel = {'1': 'Indre By', '2': 'Østerbro', '3': 'Nørrebro', '4': 'Vesterbro/Kgs. Enghave', '5': 'Valby', '6': 'Vanløse', '7': 'Brønshøj-Husum', '8': 'Bispebjerg', '9': 'Amager Øst', '10': 'Amager Vest', '99': 'Udenfor inddeling'}
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

for p in popultaion_arr:
    sorted_p = sorted(p.items(), key=op.itemgetter(1), reverse=True)[:3]
    print(sorted_p)
