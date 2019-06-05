# dependencies
import os
import csv

# store filepath in a variable
csvpath = os.path.join('budget_data.csv')

# create empty lists
dates = []
profit = []
change = []

# read data into program
with open(csvpath,newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    # identifies header row
    header = next(csv_reader)

    # loops through rows to change columns into lists
    for row in csv_reader:
        dates.append(row[0])
        profit.append(int(row[1]))

    # following code checks if the lists were split correctly
    # print(dates)
    # print(profit)    

    total_months = len(dates)
    total_profit = sum(profit)
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(total_months))
    print("Total: $" + str(total_profit))

    # def mean(numbers):
    # avg = sum(numbers) / len(numbers)
    # return avg