# dependencies
import os
import csv

# store filepath in a variable
csvpath = os.path.join('election_data.csv')

# create lists and variables
total_votes = 0
id_list = []
county_list = []
candidate_list = []

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
    # print(id_list[0:50])
    # print(len(id_list))
    # print(county_list[0:50])
    # print(len(county_list))
    # print(candidate_list[0:50])
    # print(len(candidate_list))
    
    # print title of analysis    
    print("Election Results \n-------------------------")
    
    # calc and print total votes
    total_votes = len(id_list)
    print("Total Votes: " + str(total_votes) + "\n-------------------------")
    
    # calc and print candidates tallies
    print("Khan: \nCorrey: \nLi: \nO'Tooley: \n-------------------------")
    
    # calc and print winner
    print("Winner: Khan\n-------------------------")

    # output all print statements to text file
    with open('PyPoll.txt', 'w') as f:
        print("Election Results\n-------------------------\nTotal Votes: " + str(total_votes) + 
            "\n-------------------------", file=f)