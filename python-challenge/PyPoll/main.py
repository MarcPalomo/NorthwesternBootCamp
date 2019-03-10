#import os
import os

# read the csv
import csv

csvpath = os.path.join("election_data.csv")

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)

    # create the list to place all candidates
    candidates = []

    # use a for-loop to go through each row and get the candidates to reference later
    for row in csvreader:
        
        # use the if to append the candidate list with unduplicated values
        if row[2] not in candidates:
            candidates.append(row[2])
    
    # I used the below to determine the unduplicated candidate list and the count of unduplicated candidates just as I was testing the code while I was going
    # One could use the print(candidates) and len(candidates) to identify how many variables need to be added in another election cycle with a different amount of candidates
    # I commented these out because I don't want them to print in my final product
    #print(candidates)
    #print(len(candidates))

    # set the new variables in order to reference in the next for-loop
    candidateA = candidates[0]
    candidateB = candidates[1]
    candidateC = candidates[2]
    candidateD = candidates[3]

# I restarted this with because I couldn't get the below for-loop to work in my previous line of code
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)

    #using the commented out prints above I can see there are only 4 candidates in this list.
    candidateA_votes = 0
    candidateB_votes = 0
    candidateC_votes = 0
    candidateD_votes = 0
    row_total = 0

    #run through the rows again and tally up all the votes and rows
    for rows in csvreader:
        row_total = row_total + 1
        if rows[2] == candidateA:
            candidateA_votes = candidateA_votes + 1
        elif rows[2] == candidateB:
            candidateB_votes = candidateB_votes + 1
        elif rows[2] == candidateC:
            candidateC_votes = candidateC_votes + 1
        elif rows[2] == candidateD:
            candidateD_votes = candidateD_votes + 1

    # set the percents
    percentA = (candidateA_votes / row_total) * 100
    percentB = (candidateB_votes / row_total) * 100
    percentC = (candidateC_votes / row_total) * 100
    percentD = (candidateD_votes / row_total) * 100

    #round to the 3rd decimal to match the convention required in the example picture
    percentAr = '{:.3f}'.format(round(percentA,3))
    percentBr = '{:.3f}'.format(round(percentB,3))
    percentCr = '{:.3f}'.format(round(percentC,3))
    percentDr = '{:.3f}'.format(round(percentD,3))

    # create a list to reference the winner
    percentages = [percentA, percentB, percentC, percentD]
    
    # identify the max percentage in the list to reference the winner
    winning_percentage = (max(percentages))

    # using the previous list of candidates and the referenced max value in the percentages list, identify the winner by matching the same number entry in both lists
    # you can definitely do this easily by eye since there are only 4 candidates by printing the percentages and candidates list; however, this allows us to perform the same function with a much larger list
    winning_candidate = candidates[percentages.index(max(percentages))]

    # print everything in the correct format
    print("Election Results")
    print("----------------------------")
    print("Total Votes: " + str(row_total))
    print(candidateA + ": " + str(percentAr) + "% (" + str(candidateA_votes) + ")")
    print(candidateB + ": " + str(percentBr) + "% (" + str(candidateB_votes) + ")")
    print(candidateC + ": " + str(percentCr) + "% (" + str(candidateC_votes) + ")")
    print(candidateD + ": " + str(percentDr) + "% (" + str(candidateD_votes) + ")")
    print("----------------------------")
    print("Winner: " + winning_candidate)
    print("----------------------------")

    #open a new file
    file = open("Marc_Palomo_election_summary.txt", "w")
    file.write("Election Results" + "\n" + 
        "----------------------------" + "\n" +
        "Total Votes: " + str(row_total) + "\n" +
        candidateA + ": " + str(percentAr) + "% (" + str(candidateA_votes) + ")" + "\n" +
        candidateB + ": " + str(percentBr) + "% (" + str(candidateB_votes) + ")" + "\n" +
        candidateC + ": " + str(percentCr) + "% (" + str(candidateC_votes) + ")" + "\n" +
        candidateD + ": " + str(percentDr) + "% (" + str(candidateD_votes) + ")" + "\n" +
        "----------------------------" + "\n" +
        "Winner: " + winning_candidate + "\n" +
        "----------------------------")
    file.close()