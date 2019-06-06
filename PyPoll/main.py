# dependencies
import os
import csv

# store filepath in a variable
csvpath = os.path.join('election_data.csv')

# create empty lists
id_list = []
county_list = []
candidate_list = []
unique_list = []
vote_list = []

# read data into program
with open(csvpath,newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    # identifies header row
    header = next(csv_reader)

    # loops through rows to split columns into lists
    for row in csv_reader:
        id_list.append(row[0])
        county_list.append(row[1])
        candidate_list.append(row[2])

    # following only to check if the lists were split correctly
    # print(id_list[0:10], len(id_list), candidate_list[0:10], (len(candidate_list))
  
    # calc unique candidate names
    for name in candidate_list:
        if name not in unique_list: 
            unique_list.append(name)

    # print title of analysis and calc/print total_votes
    total_votes = len(id_list)     
    print(f"Election Results\n-------------------------\nTotal Votes: {total_votes}\n-------------------------")
    
    # calc/print percentages and votes for all unique candidates and put into lists that can have same indices as the unique candidates
    for x in unique_list:
        vote_count = candidate_list.count(x)
        vote_list.append(vote_count)
        print(f"{x}: {format(((vote_count / total_votes) * 100), '.3f')}% ({vote_count})")

    # calc the index of the max votes to use as index of the unique candidate to cal winner
    print(f"-------------------------\nWinner: {unique_list[vote_list.index(max(vote_list))]}\n-------------------------")

    # output to text file (only one for loop had to be repeated so that it could print to txt file correctly even if candidate list changes)
    with open('PyPoll.txt', 'w') as f:

        # output title of analysis and total votes to txt file
        print(f"Election Results \n-------------------------\nTotal Votes: {total_votes}\n-------------------------", file=f)

        # calc percentages and votes for all unique candidates and output to txt file
        for x in unique_list:
            vote_count = candidate_list.count(x)
            vote_list.append(vote_count)
            print(f"{x}: {format(((vote_count / total_votes) * 100), '.3f')}% ({vote_count})", file=f)
        
        # output winner to txt file
        print(f"-------------------------\nWinner: {unique_list[vote_list.index(max(vote_list))]}\n-------------------------", file=f)