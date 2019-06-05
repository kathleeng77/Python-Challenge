# dependencies
import os
import csv

# store filepath in a variable
csvpath = os.path.join('budget_data.csv')

# create lists and variables
dates = []
profit = []
monthly_change = 0
change_list = []
avg_change = 0

# read data into program
with open(csvpath,newline='') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    
    # identifies header row
    header = next(csv_reader)

    # loops through rows to change columns into lists
    for row in csv_reader:
        dates.append(row[0])
        profit.append(int(row[1]))

    # following only to check if the lists were split correctly
    # print(dates)
    # print(profit)

    # print title of analysis    
    print("Financial Analysis")
    print("----------------------------")
    
    # calc and print total months
    total_months = len(dates)
    print("Total Months: " + str(total_months))
    
    # calc and print total profit
    total_profit = sum(profit)    
    print("Total: $" + str(total_profit))
    
    # make list of changes
    for i in range(1, len(profit)):
        if (profit[i] and profit[i-1] > 0) or (profit[i] and profit[i-1] < 0):
            monthly_change = profit[i] - profit[i-1]
            change_list.append(monthly_change)
        elif profit[i] < 0 and profit[i-1] > 0:
            monthly_change = profit[i] - profit[i-1]
            change_list.append(monthly_change)
        elif profit[i] > 0 and profit[i-1] < 0:
            monthly_change = profit[i-1] - profit[i]
            change_list.append(monthly_change)
   
    # following only to check correctness of list and length of list
    # print(change_list)
    # print(len(change_list))

    # define function to get average
    def mean(numbers):
        avg = sum(numbers) / len(numbers)
        return avg
    
    # calc and print avg_change with correct decimals
    avg_change = mean(change_list)
    print("Average Change: $" + str(format(avg_change, '.2f')))