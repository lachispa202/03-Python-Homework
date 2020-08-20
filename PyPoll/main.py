# PyPoll Homework
# 
# Import the os module
# Import the csv reader

import os
import csv

# Path to read the election_data.csv file

csvpath = os.path.join("..", "Resource", "election_data.csv")

# Variables for the number of votes. Equals number of rows, excluding header. 
votes = []

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
        votes.append(row[0])       
        total_votes=len(votes)

# Candidate information including number of votes received
        name = row[2]
        
        if name not in election_candidate.keys():
            election_candidate[name]=1
        else:
            election_candidate[name] += 1
   

        candidate_name = ""
        for candidate in election_candidate.items():
            candidate_name += '\n'.join([candidate_name, str(candidate) + str(election_candidate[candidate]) + " ) "]),'\n'
            # candidate_name += '\n'.join([candidate_name, str(candidate) + '{:.1%}'.format(election_candidate/total_votes)]),'\n'
            
            # percent_votes = (election_candidate/total_votes)

            # percent_votes_formated = '{:.1%}'.format(percent_votes)
            
            # candidates_information += '\n'.join([(candidate_name) + "      " + (percent_votes_formated) + "     ( "   + " )"'\n'])
            # ] +  '{:,.2f}'.format(election_candidate) +        + '{:,.2f}'.format(election_candidate) + 
            # candidate_name = '\n'.join([str(candidate) + "     ( "   + " )"'\n'])
            # percent_votes = '\n'.join(election_candidate/total_votes)'\n'

        Winner = max(election_candidate.keys(), key =(lambda k: election_candidate[k]))

# Calculation to get the votes per candidate


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
# # Sequence to export results
# # Specify the file to write to
# output_path = os.path.join("Financial_Summary.txt")

# with open("Financial_Summary.txt", 'w') as text_file:

# # Write the following:
#     text_file.write('\n')
#     text_file.write("Summary of Financial Analysis")
#     text_file.write('\n')
#     text_file.write("-----------------------------------------------")
#     text_file.write('\n')
#     text_file.write("Total Months:                      " + (str(total_months)))
#     text_file.write('\n')
#     text_file.write("Total:                           $ " + '{:,.2f}'.format(total_profit_loss))
#     text_file.write('\n')
#     text_file.write("Average Change:                  $" + '{:,.2f}'.format(average_change))
#     text_file.write('\n')
#     text_file.write("Greatest Increase in Profits:    $ " + '{:,.2f}'.format(greatest_increase_profits) + "  in month " + (str(greatest_increase_profits_date)))
#     text_file.write('\n')
#     text_file.write("Greatest Decrease in Profits:    $" + '{:,.2f}'.format(greatest_decrease_profits) + "  in month " + (str(greatest_decrease_profits_date)))
#     text_file.write('\n')
#     text_file.write("-----------------------------------------------")
#     text_file.write('\n')

# # End of program