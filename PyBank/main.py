# Import the os module
# Import the csv reader

import os
import csv

# Path to read the budget_data.csv file

csvpath = os.path.join("..", "Resource", "budget_data.csv")

# Read csv file using the CSV module

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# To skip top row (ie header row) in csv file and print it out
    csv_header = next (csvreader)
    print(f"CSV Header: {csv_header}")

 # Read each row of data after the header
    for row in csvreader:
        print(row)
    # Calculation for number of months
        total_months = csvreader.line_num - 1





# Output Summary
    print()
    print("Summary of Financial Analysis")
    print("-----------------------------------------------")
    print("Total Months:                    " + (str(total_months)))
    print("Total:")
    # print("Average Change:")
    # print("Greatest Increase in Profits:")
    # print("Greatest Decrease in Profits:")

    print("-----------------------------------------------")

 
