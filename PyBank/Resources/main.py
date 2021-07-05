import os
import csv


csvpath = os.path.join("Pybank", "resources", "budget_data.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ",")
    print(csvreader)
    csv_reader = next(csvreader, None)

    dates = []
    profit_losses = []
    monthly_change = []

    print(f"header: {csv_header}")

    for row in csvreader:
        dates.append(row[0])
        profit_losses.append(row[1])
    print(len(dates))
    
    total_months = 0
    for month in dates:
        total_months += 1

    net_total = 0
    for row in profit_losses:
        net_total += int(row)

    for i in range(len(profit_losses)):
        monthly_change.append(int(profit_losses[i+1] - int(profit_losses[i]))
        #print(int(profit_losses[i+1])-int(profit_losses[i]))
        #print(i)
        #monthly_change.append(profit_losses[row=1]-profit_losses[row])