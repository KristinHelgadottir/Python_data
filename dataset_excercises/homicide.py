import csv #making sure it can read csv

filename = 'database.csv' # naming the csv file object

with open(filename) as file_object: #getting/opening the csv
    reader = csv.reader(file_object) # returns reader object that reads lines in file
    header_row = next(reader) # first getting the headers line and so on/next

    for i, v in enumerate(header_row): # starting from headers row
        print(i, v)

    age_sum = 0
    age_count = 0
    for row in reader:
        age_sum += int(row[12])
        age_count = age_count + 1
        
    average_age = age_sum / age_count
    print("Average age: " + str(average_age))

    