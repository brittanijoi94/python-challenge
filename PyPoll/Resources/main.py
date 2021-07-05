#import poll

import os
import csv

#working directory 

csvpath = os.path.join("Pypoll", "resources", "election_data.csv")
with open(csvpath) as csvfile 
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header + next(csvreader)

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
                
        



