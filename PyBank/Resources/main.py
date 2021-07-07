import os
import csv


budget_data = os.path.join("Pybank", "resources", "budget_data.csv")

with open(budget_data) as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ",")
    
    csv_header = next(csvreader, None)

    dates = []
    profit_losses = []
    monthly_change = []
    revenue_change = []
    

    for row in csvreader:
        dates.append(row[0])
        profit_losses.append(int(row[1]))
    
    
    for x in range(1, len(profit_losses)):
        revenue_change.append((int(profit_losses[x]) - int(profit_losses[x-1])))

revenue_average = sum(revenue_change)/ len(revenue_change)

total_dates = len(dates)

greatest_increase = max(revenue_change)

greatest_decrease = min(revenue_change)

print("Financial Analysis")
print("----------------------")
print("total dates: " + str(total_dates))
print("Total: " + "$" + str(sum(profit_losses)))
print("Average change: " + "$" + str(revenue_average))
print("Greatest Increase in Profits: " + str(dates[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))
print("Greatest Decrease in Profits: " + str(dates[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))