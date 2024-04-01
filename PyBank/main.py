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
# Open the CSV using the UTF-8 encoding
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    for row in csvreader:
        total_month.append(row[0])
        profit_losses = profit_losses + int(row[1])
        monthly_profit_losses.append(row[1])
    
    for x in range (1, len(monthly_profit_losses)):
        previous_profit_losses = monthly_profit_losses[x-1]
        current_profit_losses = monthly_profit_losses[x]
        profit_losses_change = int(current_profit_losses) - int(previous_profit_losses)
        monthly_change.append(profit_losses_change)
    
    def average(numbers):
        length = len(numbers)
        total = 0.0
        for number in numbers:
            total += number
        return total / length
            
print (len(total_month))
print ("$" + str(profit_losses))
print ("$" + str(round(int(average(monthly_change)),4)))
print (max(monthly_change))
print (min(monthly_change))