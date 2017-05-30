import warnings

warnings.filterwarnings('ignore')

import csv
import matplotlib.pyplot as plt
import collections

filename = "befkbhalderkoencivst.csv"

with open(filename) as file:
    reader = csv.reader(file)
    headerrow = next(reader)

    counter_male = 0
    counter_female = 0
    counter_male_old = 0
    counter_female_old = 0
    distribution_male = {}
    distribution_female = {}
    distribution_male_old = {}
    distribution_female_old = {}
    for row in reader:
        male = 0
        male_old = 0
        female = 0
        female_old = 0
        arr = int(row[0])
        age = int(row[2])

        if int(row[4]) == 1:
            male = int(row[4])

            counter_male += 1
            if age >= 18 and age <= 30:
                if arr not in distribution_male.keys():
                    distribution_male[arr] = 1
                else:
                    distribution_male[arr] += 1

        if int(row[4]) == 2:
            female = int(row[4])

            counter_female += 1
            if age >= 18 and age <= 30:
                if arr not in distribution_female.keys():
                    distribution_female[arr] = 1
                else:
                    distribution_female[arr] += 1

        if int(row[4]) == 1:
            male_old = int(row[4])

            counter_male_old += 1
            if age >= 50:
                if arr not in distribution_male_old.keys():
                    distribution_male_old[arr] = 1
                else:
                    distribution_male_old[arr] += 1

        if int(row[4]) == 2:
            female_old = int(row[4])

            counter_female_old += 1
            if age >= 50:
                if arr not in distribution_female_old.keys():
                    distribution_female_old[arr] = 1
                else:
                    distribution_female_old[arr] += 1

    sorted_dict_male = collections.OrderedDict(sorted(distribution_male.items()))
    sorted_dict_female = collections.OrderedDict(sorted(distribution_female.items()))
    sorted_dict_male_old = collections.OrderedDict(sorted(distribution_male_old.items()))
    sorted_dict_female_old = collections.OrderedDict(sorted(distribution_female_old.items()))

    year_men = list((sorted_dict_male.keys()))
    total_age_men = list(sorted_dict_male.values())
    year_women = list((sorted_dict_female.keys()))
    total_age_women = list(sorted_dict_female.values())

    year_men_old = list((sorted_dict_male_old.keys()))
    total_age_men_old = list(sorted_dict_male_old.values())
    year_women_old = list((sorted_dict_female_old.keys()))
    total_age_women_old = list(sorted_dict_female_old.values())

    print(counter_male)
    print(year_men)
    print(total_age_men)
    print("----------")
    print(counter_female)
    print(year_women)
    print(total_age_women)
    print("----------")
    print(counter_male_old)
    print(year_men_old)
    print(total_age_men_old)
    print("----------")
    print(counter_female_old)
    print(year_women_old)
    print(total_age_women_old)

    plt.ticklabel_format(useOffset=False)
    plt.axis([1992, 2015, 0, 1500])
    title = 'Distribution of {} CPH Citizens from 1995 to 2015'
    plt.title(title, fontsize=12)
    plt.xlabel("Year", fontsize=10)
    plt.ylabel("How many of age 18 to 30", fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=10)

    plt.bar(year_women, total_age_women, width=0.5, linewidth=0, align='center', color='green')
    plt.show()

    plt.bar(year_men, total_age_men, width=0.5, linewidth=0, align='center')
    plt.ticklabel_format(useOffset=False)
    plt.axis([1992, 2015, 0, 1500])
    title = 'Distribution of {} CPH Citizens from 1995 to 2015'
    plt.title(title, fontsize=12)
    plt.xlabel("Year", fontsize=10)
    plt.ylabel("How many of age 18 to 30", fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=10)

    # plt.bar(year_women, total_age_women, width=0.5, linewidth=0, align='center', color='green')
    plt.show()

    plt.bar(year_men_old, total_age_men_old, width=0.5, linewidth=0, align='center', color='black')
    plt.ticklabel_format(useOffset=False)
    plt.axis([1992, 2015, 0, 3000])
    title = 'Distribution of {} CPH Citizens from 1995 to 2015'
    plt.title(title, fontsize=12)
    plt.xlabel("Year", fontsize=10)
    plt.ylabel("How many of age 18 to 30", fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=10)

    plt.show()

    plt.bar(year_women_old, total_age_women_old, width=0.5, linewidth=0, align='center', color='red')
    plt.ticklabel_format(useOffset=False)
    plt.axis([1992, 2015, 0, 3000])
    title = 'Distribution of {} CPH Citizens from 1995 to 2015'
    plt.title(title, fontsize=12)
    plt.xlabel("Year", fontsize=10)
    plt.ylabel("How many of age 18 to 30", fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=10)

    plt.show()
