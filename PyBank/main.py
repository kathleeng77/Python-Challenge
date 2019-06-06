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
    # print(dates, len(dates), profit, len(profit))
    
    # loop to calc monthly_change and append all to change_list 
    for i in range(1, len(profit)):
        # you must subtract 2nd number from 1st number in these 3 situations:
        # if numbers are both positive, if numbers are both negative,
        # if 1st number is positive and 2nd number is negative
        if (profit[i] and profit[i-1] > 0) or (profit[i] and profit[i-1] < 0) or (profit[i] < 0 and profit[i-1] > 0):
            monthly_change = profit[i] - profit[i-1]
            change_list.append(monthly_change)
        # you must subtract 1st number from 2nd number: if 2nd number is positive and 1st number is negative 
        elif profit[i] > 0 and profit[i-1] < 0:
            monthly_change = profit[i-1] - profit[i]
            change_list.append(monthly_change)
   
    # following only to check correctness of list and length of list
    # print(change_list, len(change_list))

    # find greatest increase and decrease in profits and their indices
    maxProfit = max(change_list)
    minProfit = min(change_list)
    indexOf_maxProfit = change_list.index(maxProfit)
    indexOf_minProfit = change_list.index(minProfit)
    
    # calc total months and total profit
    total_months = len(dates)
    total_profit = sum(profit)
    
    # define average function and calc avg_change
    def mean(numbers):
        avg = sum(numbers) / len(numbers)
        return avg
    avg_change = mean(change_list)

    # print title of analysis, total months, total profit, avg_change with correct decimals, greatest increase and decrease
    print(f"Financial Analysis\n----------------------------\nTotal Months: {str(total_months)}")
    print(f"Total: ${str(total_profit)}\nAverage Change: ${str(format(avg_change, '.2f'))}")
    print(f"Greatest Increase in Profits: {dates[indexOf_maxProfit+1]} (${str(maxProfit)})")
    print(f"Greatest Decrease in Profits: {dates[indexOf_minProfit+1]} (${str(minProfit)})")
    
    # output all print statements to text file
    with open('Finance.txt', 'w') as f:
        print(f"Financial Analysis\n----------------------------\nTotal Months: {str(total_months)}", file=f)
        print(f"Total: ${str(total_profit)}\nAverage Change: ${str(format(avg_change, '.2f'))}", file=f)
        print(f"Greatest Increase in Profits: {dates[indexOf_maxProfit+1]} (${str(maxProfit)})", file=f)
        print(f"Greatest Decrease in Profits: {dates[indexOf_minProfit+1]} (${str(minProfit)})", file=f)