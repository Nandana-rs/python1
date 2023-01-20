import csv

# open the csv file
with open('nrs.csv' , 'r') as file:
    # create a csv reader
    reader = csv.reader(file)

    # Iterate over the rows of the csv file
    for row in reader:
        # print the row as a list of strings
        print(row)