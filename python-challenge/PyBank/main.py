#import os
import os

# read the csv
import csv

csvpath = os.path.join("budget_data.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)

     

    # start start all the variables at 0 since the header will get skipped
    row_total = 0
    
    profit_losses = 0

    current_amount = 0

    last_amount = 0

    # create the list to place all the revenues in order to reference as the max, min, and average
    revenue_change = []
    months = []

    # use a for-loop to go through each row and add them all up since each row is a unique value in reference to column 1
    for row in csvreader:
        current_amount = int(row[1])
        profit_losses = profit_losses + current_amount
        if row_total != 0:
            revenue_change.append(current_amount - last_amount)

        last_amount = current_amount
        row_total = row_total + 1
        months.append(row[0])
    revenue_average = sum(revenue_change) / len(revenue_change)
    revenue_average_round = round(revenue_average, 2)

    # print my total rows
    print("Financial Analysis")
    print("-------------------------------")
    print("Total Months: " + str(row_total))
    print("Total: $" + str(profit_losses))
    print("Average Change: $" + str(revenue_average_round))
    print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "($" + str(max(revenue_change))+ ")")
    print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "($" + str(min(revenue_change))+ ")")
    
    

    #open the new file
    file = open("Marc_Palomo_budget_summary.txt", "w")
    file.write("Financial Analysis" + "\n" +
        "-------------------------------" + "\n" +
        "Total Months: " + str(row_total) + "\n" + 
        "Total: $" + str(profit_losses) + "\n" +
        "Average Change: $" + str(revenue_average_round) + "\n" +
        "Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "($" + str(max(revenue_change))+ ")" + "\n" +
        "Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "($" + str(min(revenue_change))+ ")")
    file.close()