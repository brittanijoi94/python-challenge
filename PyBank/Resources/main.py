import os
import csv


csvpath = os.path.join("Pybank", "resources", "budget_data.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ",")
    csv_reader = next(csvreader)

    dates = []
    profit_losses = []
    monthly_change = []

    for row in csvreader:
        dates.append(row[0])
        profit_losses.append(row[1])


    