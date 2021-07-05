import os
import csv


csvpath = os.path.join("Pybank", "resources", "budget_data.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ",")
    csv_reader = next(csvreader, None)

    dates = []
    profit_losses = []
    monthly_change = []

    for row in csvreader:
        dates.append(row[0])
        profit_losses.append(row[1])
    
    total_months = 0
    for month in dates:
        total_months += 1

    net_total = 0
    for row in profit_losses:
        net_total += int(row)

    for i in range(len(profit_losses)):
        monthly_change.append(str(profit_losses[i+1]-profit_losses[i]))
        print(monthly_change)


    