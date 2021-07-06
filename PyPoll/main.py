#import dependencies
import os
import csv

# Path to collect data from the Resources folder
pypoll_csv = os.path.join('PyPoll','Resources','election_data.csv')

with open(pypoll_csv, 'r') as csvfile:
    
    csvreader = csv.DictReader(csvfile, delimiter=',')

    #rows = list(csvreader)
    #totalrows = len(rows)

    votes = []

    for row in csvreader:
        candidate_name = row['Candidate']
        votes.append(candidate_name)

    print("Total Votes:",len(votes))

    candidate_list = ["Khan", "Correy","Li","O'Tooley"]
    vote_max = 0
    vote_winner = ""
    for candidate in candidate_list:
        vote_count = votes.count(candidate)
        vote_percentage = (vote_count/len(votes))*100
        if vote_count > vote_max:
            vote_max = vote_count
            vote_winner = candidate

        print(candidate,vote_count,vote_percentage)
        

print("Winner:",vote_winner)





















#Print to both the terminal and a txt file

#Print ( ---, file=open("output.txt", "a"))--six times for each print statement

