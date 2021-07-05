#import dependecies
import os
import csv
import datetime

# Path to collect data from the Resources folder
pybank_csv = os.path.join('Resources','budget_data.csv')

with open(pybank_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.DictReader(csvfile, delimiter=',')
    
    #rows = list(csvreader)
    #totalrows = len(rows)
    months = 0
    net_profit = 0
    current_profit = 0
    last_profit = 0
    changes_profit = 0
    greatest_increase = 0
    greatest_decrease = 0

    for row in csvreader:
        months += 1

    print(months)
















#Print to both the terminal and a txt file