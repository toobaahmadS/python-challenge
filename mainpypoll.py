# import libraries
import os
import csv
# Setting the file path for input and output
csv_path=os.path.join("Resources", "election_data.csv")
text_output_path=os.path.join("analysispypoll", "text_output.txt")
total_vote= 0
candidates= []
candidates_vote= {}
winner_count= 0
winner = ""
with open(csv_path, 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    # lopp for counting votes
    for row in csvreader:
        total_vote += 1
        candidate = row["Candidate"]
        # if statement to get the name of candidates
        if candidate not in candidates:
            candidates.append(candidate)
            candidates_vote[candidate] = 0
        candidates_vote[candidate] = candidates_vote[candidate] + 1
    #print(candidates)
    #print(total_vote)
with open(text_output_path, 'w') as text_file:
    election_header = (f"Election Result\n"
                            f"________________\n")
    text_file.write(election_header)
    print("Total Votes " + str(total_vote))
    print("_________________\n")
    for candidate in candidates_vote:
        votes = candidates_vote.get(candidate)
        #print(votes)
        vote_percentage = float(votes)/float(total_vote)*100
        #print(vote_percentage)
        if (votes > winner_count):
            winner_count = votes
            winner = candidate
        voter_output = f"{candidate}: %{vote_percentage:.3f}({votes})\n\n"
        print(voter_output)
        text_file.write(voter_output)
    winning_summary = (
        f"Winner: {winner}"
    )
    print(winning_summary)
    text_file.write(winning_summary)