# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Set variable
votes = []
candidates = []
candidate_names = []
numbers_of_votes = []
percents_of_votes = []
# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
     # Read the header row first
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        #Add all votes/Ballot ID into a list
        votes.append(row[0])
        #Add all candidates (all value in column 3 in csv file) into a list
        candidates.append(row[2])
    # Calculate total number of votes cast
    total_votes = len(votes)
    # Sort all names in the list in ascending order
    candidates.sort()
    
    # Loop through candidates (all value in column 3 in csv file) list
    for x in range (1, total_votes):
        # Find the differnt names
        if candidates[x] != candidates[x - 1]:
             # Add different candidate names into a list but the last name will be missing
            candidate_names.append(candidates[x-1])
    # Add the last candidate names into the list
    candidate_names.append(candidates[total_votes-1])
   
    # Loop through candidates name list
    for x in range (len(candidate_names)):
        # Calculate the votes of each candidates
        vote_count = candidates.count(candidate_names[x])
        # Calculate the percentages of votes of each candidates
        vote_percent = vote_count / total_votes * 100
        # Add the numbers of votes of each candidates into a list
        numbers_of_votes.append(vote_count)
        # Add the percentages of votes of each candidates into a list
        percents_of_votes.append(round(vote_percent, 3))
  
    # Find the highest number of votes
    highest_votes = max(numbers_of_votes)
    # Find the winner who has the most votes
    winner = candidate_names[numbers_of_votes.index(highest_votes)]

# Print the results
print("Election Results")
print("-----------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------")

for x in range (len(candidate_names)):
    print(f"{candidate_names[x]}: {percents_of_votes[x]}% ({numbers_of_votes[x]})")

print("-----------------------------")
print(f"Winner: {winner}")
print("-----------------------------")