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
maxProfit = 0
minProfit = 0
indexOf_maxProfit = 0
indexOf_minProfit = 0

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
    # print(len(dates))
    # print(profit)
    # print(len(profit))

    # print title of analysis    
    print("Financial Analysis")
    print("----------------------------")
    
    # calc and print total months
    total_months = len(dates)
    print("Total Months: " + str(total_months))
    
    # calc and print total profit
    total_profit = sum(profit)    
    print("Total: $" + str(total_profit))
    
    # loop to calc monthly_change and add to change_list
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

    # find greatest increase and decrease in profits
    maxProfit = max(change_list)
    minProfit = min(change_list)
    
    # check profit calc
    # print(maxProfit)
    # print(minProfit)
    
    # find index for max and min profit
    indexOf_maxProfit = change_list.index(maxProfit)
    indexOf_minProfit = change_list.index(minProfit)
    
    # check dates
    # print(dates[indexOf_maxProfit+1])
    # print(dates[indexOf_minProfit+1])
    
    # print greatest increase and decrease in profits
    print("Greatest Increase in Profits: " + dates[indexOf_maxProfit+1] + " ($" + str(maxProfit) +")")
    print("Greatest Decrease in Profits: " + dates[indexOf_minProfit+1] + " ($" + str(minProfit) +")")

    

