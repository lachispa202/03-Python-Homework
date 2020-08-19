# Import the os module
# Import the csv reader

import os
import csv

# Path to read the budget_data.csv file

csvpath = os.path.join("..", "Resource", "budget_data.csv")

# Variables for the number of months. Equals number of rows, excluding header. 
months = []
total_months = 0

# Variables for the program
profit_loss = []
total_profit_loss = 0

# Vaiable for monthly change (ie monthly change = current month - previous month) and average_change for the dataset 
monthly_change = []
total_monthly_change = 0
average_change = 0

# Read csv file using the CSV module

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

# To skip top row (ie header row) in csv file and print it out
    csv_header = next (csvreader)
    # print(f"CSV Header: {csv_header}")

# Read each row of data after the header
    for row in csvreader:
        # print(row)

# Calculation for number of months
        months.append(row[0])       
        total_months=len(months)

# Calculation for the the total profits 
        profit_loss.append(float(row[1]))
        total_profit_loss =sum(profit_loss)
 
# Calculation for the monthly change and average monthly change (where i is for current month and i-1 is previous month)
    for i in range(1,len(profit_loss)):
        monthly_change.append(profit_loss[i]-profit_loss[i-1])    

        total_monthly_change = sum(monthly_change)   
            
        average_change = total_monthly_change/len(monthly_change)

# Calculation for the greatest increase and greatest decrease in monthly change. 
        greatest_increase_profits = max(monthly_change)
        greatest_decrease_profits = min(monthly_change)

# Identifying the month of greatest increase and greatest decrease in monthly change. 
        greatest_increase_profits_date = str(months[monthly_change.index(max(monthly_change))])
        greatest_decrease_profits_date = str(months[monthly_change.index(min(monthly_change))])

# Output Summary, including number formatting
    print()
    print("Summary of Financial Analysis")
    print("-----------------------------------------------")
    print("Total Months:                      " + str(total_months))
    print("Total:                           $ " + '{:,.2f}'.format(total_profit_loss))
    print("Average Change:                  $" + '{:,.2f}'.format(average_change))
    print("Greatest Increase in Profits:    $ " + '{:,.2f}'.format(greatest_increase_profits) + "  in month " + (str(greatest_increase_profits_date)))
    print("Greatest Decrease in Profits:    $" + '{:,.2f}'.format(greatest_decrease_profits) + "  in month " + (str(greatest_decrease_profits_date)))
    print("-----------------------------------------------")

# Sequence to export results
# Specify the file to write to
output_path = os.path.join("Financial_Summary.txt")

with open("Financial_Summary.txt", 'w') as text_file:

# Write the following:
    text_file.write('\n')
    text_file.write("Summary of Financial Analysis")
    text_file.write('\n')
    text_file.write("-----------------------------------------------")
    text_file.write('\n')
    text_file.write("Total Months:                      " + (str(total_months)))
    text_file.write('\n')
    text_file.write("Total:                           $ " + '{:,.2f}'.format(total_profit_loss))
    text_file.write('\n')
    text_file.write("Average Change:                  $" + '{:,.2f}'.format(average_change))
    text_file.write('\n')
    text_file.write("Greatest Increase in Profits:    $ " + '{:,.2f}'.format(greatest_increase_profits) + "  in month " + (str(greatest_increase_profits_date)))
    text_file.write('\n')
    text_file.write("Greatest Decrease in Profits:    $" + '{:,.2f}'.format(greatest_decrease_profits) + "  in month " + (str(greatest_decrease_profits_date)))
    text_file.write('\n')
    text_file.write("-----------------------------------------------")
    text_file.write('\n')

# End of program