# Which weapon is most used by men?
males = (dd[:,15] == "Male")
weapon1 = np.max(dd[:,20][males])
print('Weapon most used by Males: {}'.format(weapon1))

# Which weapon is most used by women?
females = (dd[:,15] == "Female")
weapon = np.max(dd[:,20][females])
print('Weapon most used by Females: {}'.format(weapon))

# Which ethnicity is it most common for the victims and perpetrators to be?
victim_ethnicity = np.max(dd[:,14])
perpetrators_ethnicity = np.max(dd[:,18])        
print('The most common ethnicity of the victims are {} and for the perpetrators are {}'.format(victim_ethnicity, perpetrators_ethnicity))

# oldest victim
oldest_victim = np.max(dd[:,12])
print('The oldest victim ever was {} years old'.format(oldest_victim))
# youngest victim
youngest_victim = np.min(dd[:,12])
print('The youngest victim ever was {} years old'.format(youngest_victim))

# what is the averige age of victim?
import csv #making sure it can read csv
filename = 'database.csv' # naming the csv file object
with open(filename) as file_object: #getting/opening the csv
    reader = csv.reader(file_object) # returns reader object that reads lines in file
    header_row = next(reader) # first getting the headers line and so on/next

    for i, v in enumerate(header_row): # starting from headers row
        print(i, v)

    age_sum = 0
    age_count = 0
    for row in reader: # reading rows from headers_row reader
        age_sum += int(row[12]) # taking age from row 12 and adding it to the total sum
        age_count = age_count + 1
        
    average_age = age_sum / age_count # calculating avertage by dividing total sum with total count
    print("Average age: " + str(average_age))

    
