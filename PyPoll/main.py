# dependencies
import os
import csv

# store filepath in a variable
csvpath = os.path.join('election_data.csv')

# create lists and variables
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
    # print(id_list[0:10])
    # print(len(id_list))
    # print(county_list[0:10])
    # print(len(county_list))
    # print(candidate_list[0:10])
    # print(len(candidate_list)) 
    
    # print title of analysis    
    print("Election Results \n-------------------------")
    
    # calc and print total votes
    total_votes = len(id_list)
    print(f"Total Votes: {total_votes}\n-------------------------")
    
    # calc unique candidate names
    for name in candidate_list:
        if name not in unique_list: 
            unique_list.append(name)

    for x in unique_list:
        vote_count = candidate_list.count(x)
        vote_list.append(vote_count)
        print(f"{x}: {format(((vote_count / total_votes) * 100), '.3f')}% ({vote_count})")
    
    print(f"-------------------------")
    print(f"Winner: {unique_list[vote_list.index(max(vote_list))]}\n-------------------------")

    # output all print statements to text file
    with open('PyPoll.txt', 'w') as f:
        #print("Election Results \n-------------------------")
        #print(f"Total Votes: {total_votes}\n-------------------------")
        for x in unique_list:
            vote_count = candidate_list.count(x)
            vote_list.append(vote_count)
            print(f"{x}: {format(((vote_count / total_votes) * 100), '.3f')}% ({vote_count})", file=f)
        print(f"-------------------------", file=f)
        print(f"Winner: {unique_list[vote_list.index(max(vote_list))]}", file=f)
        print(f"-------------------------", file=f)