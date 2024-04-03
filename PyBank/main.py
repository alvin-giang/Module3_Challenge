# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Set variable
total_month = []
profit_losses= 0
monthly_profit_losses = []
monthly_change = []
months = []

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
     # Read the header row first
    csv_header = next(csvreader)
    # Read each row of data after the header
    for row in csvreader:
        # Add all months into a list
        total_month.append(row[0])
        # Calculate monthly changes
        profit_losses = profit_losses + int(row[1])
        # Add monthly profit/loss into a list
        monthly_profit_losses.append(row[1])
    
    # Loop through monthly profit/loss list
    for x in range (1, len(monthly_profit_losses)):
        # Calculate monthly changes
        previous_profit_losses = monthly_profit_losses[x-1]
        current_profit_losses = monthly_profit_losses[x]
        profit_losses_change = int(current_profit_losses) - int(previous_profit_losses)
        # Add monthly changes into a list
        monthly_change.append(profit_losses_change)
    
# Write a function that returns the arithmetic average for a list of numbers
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length
    
# Look for greatest increase/decrease changes using max/min method
greatest_increase = max(monthly_change)
greatest_decrease = min(monthly_change)

 #  Look for greatest increase/decrease month using index method
greatest_increase_month = total_month[monthly_change.index(greatest_increase) + 1]
greatest_decrease_month = total_month[monthly_change.index(greatest_decrease) + 1]

# Print the results
print ("Total Months: " + str(len(total_month)))
print ("Total: $" + str(profit_losses))
print ("Average Change: $" + str(round(int(average(monthly_change)),2)))
print (f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print (f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Specify the file to write to
output_path = os.path.join("Analysis", "Results.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as resultfile:

    # Initialise csv.writer
    csvwriter = csv.writer(resultfile)

    # Write the first row (column headers)
    csvwriter.writerow(['Total Month', 'Total', 'Average Change', 'Greatest Increase in Profits','Greatest Decrease in Profits'])

    # Write the second row
    csvwriter.writerow([len(total_month), '$' +str(profit_losses) , greatest_increase_month + ' ' + '$' + str(greatest_increase), greatest_decrease_month + ' ' + '$' + str(greatest_decrease)])
 