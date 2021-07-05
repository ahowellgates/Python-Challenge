#import dependecies
import os
import csv
import datetime

# Path to collect data from the Resources folder
pybank_csv = os.path.join('PyBank','Resources','budget_data.csv')

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
    profit_difference = 0

    for row in csvreader:
        months += 1
        current_profit = int(row['Profit/Losses'])
        net_profit += current_profit
        if months >1:
            profit_difference = current_profit - last_profit
            changes_profit += profit_difference

       
        last_profit = current_profit

        if profit_difference > greatest_increase:
            greatest_increase = profit_difference
            
        if profit_difference < greatest_decrease:
            greatest_decrease = profit_difference


print(months, file=open("output.txt", "a"))
print(net_profit, file=open("output.txt", "a"))
print(changes_profit/(months-1), file=open("output.txt", "a"))
print(greatest_increase, file=open("output.txt", "a"))
print(greatest_decrease, file=open("output.txt", "a"))








