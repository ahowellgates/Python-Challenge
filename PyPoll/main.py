#import dependencies
import os
import csv

# Path to collect data from the Resources folder
pypoll_csv = os.path.join('PyPoll','Resources','election_data.csv')

with open(pypoll_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.DictReader(csvfile, delimiter=',')

    #rows = list(csvreader)
    #totalrows = len(rows)

votes = []

for row in csvreader:
     candidate_name = row['Candidate']
     votes.append(candidate_name)

print(len(votes))

















#Print to both the terminal and a txt file

#Print ( ---, file=open("output.txt", "a"))--six times for each print statement

