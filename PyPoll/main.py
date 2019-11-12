# import dependencies
import os
import csv

# Open file and read it
election_data= os.path.join("/Users/omarkreidieh/Documents/GitHub/python-challenge-oct/PyPoll", "election_data.csv")
with open(election_data, newline = "") as electiondata:
    election = csv.reader(electiondata, delimiter = ',')
    electionheader = next(election)
    print(electionheader)
    
# Create a list of votes, voter ID, and Counties. 
    Candidate_Voted= []
    Voter_ID= []
    County_List= []  
    for row in election:
        Candidate_Voted.append(row[2])
        Voter_ID.append(row[0])
        County_List.append(row[1])
    
# Find number of votes 
    Number_votes = len(Voter_ID)

# Create a list of unique candidates receiving votes
    unique_votes = list(set(Candidate_Voted))
# Create a dictionary for each candidate with their vote count and another with their vote percentage   . 
    Candidate_Vote_Count= {}
    Candidate_Vote_Percentage = {}

# Count the number of votes for each candidate: To start select a candidate from the 
# list of unique candidates, then cycle through each row in electiondata and add one 
# to their vote count whenever their name matches the vote for that row. when done assign this vote count to their name 
# in the dictionary
    for x in unique_votes:
        votes = 0
        electiondata.seek(0)
        for row in election:
            if row[2] == x:
                votes= votes +1
        Candidate_Vote_Count[x]=votes 
        Candidate_Vote_Percentage[x]= '%.3f'%round(votes/ Number_votes *100, 5)
# rank candidates by sorting out the keys of the dictionary of number of votes based on their values:
x = sorted(Candidate_Vote_Count, key=(lambda key:Candidate_Vote_Count[key]), reverse=True)


# Print final output: 

print("Election Results")
print("--------------------------")
print(f"Total Votes: {Number_votes}")
print(f"-------------------------")
print(f"{x[0]}: {Candidate_Vote_Percentage[x[0]]}% ({Candidate_Vote_Count[x[0]]})")
print(f"{x[1]}: {Candidate_Vote_Percentage[x[1]]}% ({Candidate_Vote_Count[x[1]]})")
print(f"{x[2]}: {Candidate_Vote_Percentage[x[2]]}% ({Candidate_Vote_Count[x[2]]})")
print(f"{x[3]}: {Candidate_Vote_Percentage[x[3]]}% ({Candidate_Vote_Count[x[3]]})")
print(f"-------------------------")
print(f"Winner: {x[0]}")
print(f"-------------------------")

# Create and export file with the above:
outputtextfile = open("outputtextfile.txt","w") 
writelines= ["Election Results\n","-------------------------- \n", f"Total Votes: {Number_votes} \n", "------------------------- \n", f"{x[0]}: {Candidate_Vote_Percentage[x[0]]}% ({Candidate_Vote_Count[x[0]]}) \n", f"{x[1]}: {Candidate_Vote_Percentage[x[1]]}% ({Candidate_Vote_Count[x[1]]}) \n", f"{x[2]}: {Candidate_Vote_Percentage[x[2]]}% ({Candidate_Vote_Count[x[2]]}) \n",f"{x[3]}: {Candidate_Vote_Percentage[x[3]]}% ({Candidate_Vote_Count[x[3]]}) \n", f"------------------------- \n", f"Winner: {x[0]} \n", f"------------------------- \n"]
outputtextfile.writelines(writelines)

