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

single_people = {}

with open(filename, encoding='latin-1') as file:
    reader = csv.reader(file)
    next(reader)  # skip headers

    for row in reader:
        year = int(row[0])
        city_part = int(row[1])
        age = int(row[2])
        marital_status = row[3]
        gender = int(row[4])
        persons = int(row[5])

        if 1992 <= year <= 2015 and city_part in (1, 2, 3) and 18 <= age <= 30 and marital_status not in ('G', 'P'):
            single_people.setdefault(year, {})
            single_people[year].setdefault(city_part, {})
            single_people[year][city_part].setdefault(gender, {})
            single_people[year][city_part][gender].setdefault(age, 0)
            single_people[year][city_part][gender][age] += persons

plot_m_1_keys, plot_m_1_values = list(zip(*[(year, sum(single_people[year][1][1].values())) for year in single_people]))
plot_f_1_keys, plot_f_1_values = list(zip(*[(year, sum(single_people[year][1][2].values())) for year in single_people]))
plot_m_2_keys, plot_m_2_values = list(zip(*[(year, sum(single_people[year][2][1].values())) for year in single_people]))
plot_f_2_keys, plot_f_2_values = list(zip(*[(year, sum(single_people[year][2][2].values())) for year in single_people]))
plot_m_3_keys, plot_m_3_values = list(zip(*[(year, sum(single_people[year][3][1].values())) for year in single_people]))
plot_f_3_keys, plot_f_3_values = list(zip(*[(year, sum(single_people[year][3][2].values())) for year in single_people]))

# create plot 1
plt.bar(plot_m_1_keys, plot_m_1_values, width=0.5, linewidth=0, align='center', color='blue', label='Male')
plt.bar(plot_f_1_keys, plot_f_1_values, width=0.5, linewidth=0, align='center', color='red', alpha=0.8, label='Female')
plt.legend(loc='upper left', fontsize=10)
plt.ticklabel_format(useOffset=False)
plt.title('Distribution of single persons (ages 18-30) in city part 1 (years 1992-2015)', fontsize=10)
plt.xlabel('Years from 1992 to 2015', fontsize=10)
plt.ylabel('Single persons', fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.savefig('single_people_1.png', bbox_inches='tight')
plt.clf()


# create plot 2
plt.bar(plot_m_2_keys, plot_m_2_values, width=0.5, linewidth=0, align='center', color='blue', label='Male')
plt.bar(plot_f_2_keys, plot_f_2_values, width=0.5, linewidth=0, align='center', color='red', alpha=0.8, label='Female')
plt.legend(loc='upper left', fontsize=10)
plt.ticklabel_format(useOffset=False)
plt.title('Distribution of single persons (ages 18-30) in city part 2 (years 1992-2015)', fontsize=10)
plt.xlabel('Years from 1992 to 2015', fontsize=10)
plt.ylabel('Single persons', fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.savefig('single_people_2.png', bbox_inches='tight')
plt.clf()

# create plot 3
plt.bar(plot_m_3_keys, plot_m_3_values, width=0.5, linewidth=0, align='center', color='blue', label='Male')
plt.bar(plot_f_3_keys, plot_f_3_values, width=0.5, linewidth=0, align='center', color='red', alpha=0.8, label='Female')
plt.legend(loc='upper left', fontsize=10)
plt.ticklabel_format(useOffset=False)
plt.title('Distribution of single persons (ages 18-30) in city part 3 (years 1992-2015)', fontsize=10)
plt.xlabel('Years from 1992 to 2015', fontsize=10)
plt.ylabel('Single persons', fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=10)
plt.savefig('single_people_3.png', bbox_inches='tight')
plt.clf()