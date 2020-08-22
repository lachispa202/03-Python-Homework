# PyPoll Homework
# 
# Import the os module
# Import the csv reader

import os
import csv

# Path to read the election_data.csv file

csvpath = os.path.join("..", "Resource", "election_data.csv")

# Variables for the number of votes. Equals number of rows, excluding header. 
votes_ID = []

# Creating a dictionary for the different candidates
name = []
election_candidate = dict()

# Read csv file using the CSV module

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# To skip top row (ie header row) in csv file and print it out
    csv_header = next (csvreader)
    print(f"CSV Header: {csv_header}")

# Read each row of data after the header
    for row in csvreader:
        # print(row)

# Calculation for total number of votes, based on number of Voter ID
        votes_ID.append(row[0])       
        total_votes=len(votes_ID)

# Candidate information including number of votes received by candidate
        name = row[2]
     
        if name not in election_candidate.keys():
            election_candidate[name]=1
        else:
            election_candidate[name] += 1
   
# To break down the results by candidate, number of votes, and percentage. Includes formatting. 
        candidate_name = ""
        for candidate in election_candidate.keys():
            candidate_name += '\n'.join([str(candidate) + ":    " + '{:.1%}'.format((election_candidate[candidate])/(total_votes)) + "  of vote received, with a total number of votes being: (" + str(election_candidate[candidate]) + ")", '\n'])

# Calculation to determine the winning of the election
        Winner = max(election_candidate.keys(), key =(lambda k: election_candidate[k]))

# # Output Summary, including number formatting
    print()
    print("Election Results")
    print("-----------------------------------------------")
    print("Total Votes:                      " + str(total_votes))
    print("-----------------------------------------------")
    print("Elections Results for Each Candidate:")
    print(candidate_name)
    print("-----------------------------------------------")
    print()
    print("Election Winner:")
    print( Winner)
    print("-----------------------------------------------")
# Sequence to export results
# Specify the file to write to
output_path = os.path.join("Election_Summary.txt")

with open("Election_Summary.txt", 'w') as text_file:

# # Write the following:
    text_file.write('\n')
    text_file.write("Election Summary")
    text_file.write('\n')
    text_file.write("-----------------------------------------------")
    text_file.write('\n')
    text_file.write("Total Votes:                      " + str(total_votes))
    text_file.write('\n')
    text_file.write("-----------------------------------------------")
    text_file.write('\n')
    text_file.write("Elections Results for Each Candidate:")
    text_file.write('\n')
    text_file.write((candidate_name))
    text_file.write('\n')
    text_file.write("-----------------------------------------------")
    text_file.write('\n')
    text_file.write("Election Winner:")
    text_file.write('\n')
    text_file.write( Winner)
    text_file.write('\n')
    text_file.write("-----------------------------------------------")
    text_file.write('\n')

# # End of program