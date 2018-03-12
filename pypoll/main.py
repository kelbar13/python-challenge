import csv

# Path to collect data from folder and define results file
electionCSV = ("election_data_1.csv")

# Empty lists to store data
total_votes = []
candidates = []
percent_votes = []
votes_won = []
election_winner = []

# Read in the CSV file
with open(budgetCSV, newline="") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
            
        # Total number of votes
        votes = 0
        votes += 1
        total_votes.append(votes)
    
        # List the candidates 
        candidates_list = list(row[0])
        candidates.append(candidates_list)
    
        # Total number of votes for each candidate
        if row[0] == (candidates_list)
            candidate_votes = sum(row[1])
            votes_won.append(candidate_votes)

        # Percent of votes for each candidate
        percent = round(int(candidate_votes/votes), 2)
        votes_won.append(percent)
              
        # Winner of the election
        winner = max(percent)
        election_winner.append(percent)
    
        # Print Total Months:, Total Revenue:, Average Revenue Change:, Greatest Increase in Revenue:, Greatest Decrease in Revenue
        print("Election Results")  
        print("---------------------------")
        print("Total Votes: " + (votes))
        print("---------------------------")
        print("Candidates: ")
        print((candidates_list + ":  " + (percent) + " (" + (candidate_votes) + ")")
        print("---------------------------")
        print("Winner: " + (winner))
        
    
# Output file
output_file = ("election_results.txt")
    
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerows(output_file)

