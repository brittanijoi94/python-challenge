#import poll

import os
import csv

#working directory 

csvpath = os.path.join("Pypoll", "resources", "election_data.csv")
with open(csvpath) as csvfile
    csvreader = csv.reader(csv_file, delimiter=',')
    print(csvreader)
   

    #declaring variables 
    votes = []
    county = []
    candidates = []
    khan = []
    correy = []
    li = []
    otooley = []

    for row in csvreader:
        votes.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

        #vote count
        total_votes = (len(votes))
        print(total_votes)

        #votes by person
        for candidate in candidates:
            if candidate == "Khan":
                khan.append(candidates)
                khan_votes = len(khan)
            elif candidate == "correy"
                correy.append(candidates)
                correy_votes = len(khan)
            elif candidate == "li"
                li.append(candidates)
                li_votes = len(li)
            else canidates == "otooley"
                otooley.append(candidates)
                otooley_votes = len(otooley)
        print(khan_votes)
        print(correy_votes)
        print(li_votes)
        print(otooley_votes)
        
        #percentages 
        khan_percent = round(((khan_votes/total_votes) * 100 ), 2)
        correy_percent = round(((khan_votes/total_votes)* 100 ), 2)
        li_percent = round(((li_votes/total_votes)* 100 ), 2)
        otooley_percent = round(((otooley_votes/total_votes)* 100 ), 2)
        print(khan_percent)
        print(correy_percent)
        print(li_percent)
        print(otooley_percent)
        
#winner

if khan_percent > max(correy_percent, li_percent, otooley_percent)
    winner = khan
elif correy_percent > max(khan_percent, li_percent, otooley_percent)
    winner = correy
elif li_percent > max(khan_percent, correy_percent, otooley_percent)
    winner = li
else otooley > max(khan_percent, correy_percent, li_percent)
    winner = otooley

#Print

print("Election Results")
print("---------------") 
print("Total Votes: {total_votes}")
print("----------------")
print("khan: {khan_percent}% ({khan_votes})")
print("correy: {correy_percent}% ({correy_votes})")
print("li: {li_percent}% ({li_votes})")
print("otooley: {otooley_percent}% ({otooley_votes})")
print("----------------")
print("winner")
print("-----------------")