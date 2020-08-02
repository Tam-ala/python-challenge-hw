import csv

# Make a path to csv
csvpath = "Resources/election_data.csv"

# Save results in lists and dictionaries. Keep count of votes.
total_votes = 0
max_votes = 0
candidate_list = []
candidate_votes = {}
candidate_percentage = {}

# Open csv and skip the header
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    
    # Create a for loop to tally results
    for row in csvreader:
        candidate = row[2]
        total_votes += 1
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            candidate_votes[candidate] = 0
            candidate_percentage[candidate] = 0

        # Get the percentage of each votes per candidate
        candidate_votes[candidate] += 1
        candidate_percentage[candidate] = (candidate_votes[candidate]/total_votes)*100

        # Find the winner by max number of votes
        if candidate_votes[candidate] > max_votes:
            max_votes = candidate_votes[candidate]
            winner = candidate

# Print out the results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")
print("Votes per Candidate")
for (key, value) in candidate_votes.items(): 
    print (key, value) 
print("--------------------------")
print("Percentage of Votes per Candidate")
for (key, value) in candidate_percentage.items(): 
    print (key, value) 
print("--------------------------")
print(f"Winner: {winner}")
print("--------------------------")

# Export results to a text file
with open("ElectionResults.txt","w") as text:
    text.write("Election Results \n")
    text.write("--------------------------\n")
    text.write(f"Total Votes: {str(total_votes)} \n")
    text.write("-------------------------- \n")
    text.write("Votes per Candidate \n")
    for (key, value) in candidate_votes.items(): 
        text.write(key) 
        text.write(f" {value} \n") 
    text.write("-------------------------- \n")
    text.write("Percentage of Votes per Candidate \n")
    for (key, value) in candidate_percentage.items(): 
        text.write(key) 
        text.write(f" {value} \n") 
    text.write("-------------------------- \n")
    text.write(f"Winner: {winner} \n")
    text.write("-------------------------- \n")
