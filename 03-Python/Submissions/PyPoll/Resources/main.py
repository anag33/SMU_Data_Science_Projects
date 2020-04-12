# Modules
import csv

# Set path for file
csvpath = r"PyPoll\Resources\election_data.csv"

# Counter for the votes
totalVotes = 0

# Declare variables

votesKhan = 0
votesCorrey = 0
votesLi = 0
votesOtooley = 0 

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip CSV header
    csv_header = next(csvreader)
    

    # Loop through rows
    for row in csvreader:
        #Increment total votes
        totalVotes += 1
    

        #Calculate number of votes per candidates
        if row[2] == "Khan": 
            votesKhan +=1
        elif row[2] == "Correy":
            votesCorrey +=1
        elif row[2] == "Li": 
            votesLi +=1
        elif row[2] == "O'Tooley":
            votesOtooley +=1

        
            
#Create a List of candidates and votes 
candidates = ["Khan", "Correy", "Li", "O'Tooley"]
votes = [votesKhan, votesCorrey, votesLi, votesOtooley]

        
#Convert the two lists into dictionaries to get the key and value 
dict_candidates_and_votes = dict(zip(candidates, votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)
            
#Calculate percent of votes per candidates
khanPercent = (votesKhan/totalVotes) * 100
correyPercent = (votesCorrey/totalVotes) * 100
liPercent = (votesLi/totalVotes) * 100
otooleyPercent = (votesOtooley/totalVotes) * 100
            

# Print Results

print("Election Results" + "\n")

print("..............................."  + "\n" )

print("Total Votes: " + str(totalVotes) + "\n")

print("..............................."  + "\n" )

print(f"Khan:  {khanPercent:.3f}%  ({votesKhan})")

print(f"Correy:  {correyPercent:.3f}%  ({votesCorrey})")
 
print(f"Li:  {liPercent:.3f}%  ({votesLi})")

print(f"O'Tooley:  {otooleyPercent:.3f}%  ({votesOtooley})")

print("..............................."  + "\n" )

print(f"Winner: {key}")

#Output to a text file

file = open("output.PyPolltext", "w")

file.write("Election Results" + "\n")

file.write("..............................."  + "\n" )

file.write("Total Votes: " + str(totalVotes) + "\n")

file.write("..............................."  + "\n" )

file.write(f"Khan:  {khanPercent:.3f}%  ({votesKhan}) \n")

file.write(f"Correy:  {correyPercent:.3f}%  ({votesCorrey}) \n")
 
file.write(f"Li:  {liPercent:.3f}%  ({votesLi}) \n")

file.write(f"O'Tooley:  {otooleyPercent:.3f}%  ({votesOtooley}) \n")

file.write("..............................."  + "\n")

file.write(f"Winner: {key} \n")

file.write("..............................."  + "\n")

file.close()