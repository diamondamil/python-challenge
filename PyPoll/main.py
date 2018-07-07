
import os

import csv



## Use the os module to read file path

csv_Path = os.path.join("Resources", "election_data.csv")

# print(csv_Path)



# Total Votes counter

TotalVotes = 0

WinningVoteCount = 0

WinningCandidate = ""

WinningPercent = 0.00



# Create lists 

CandidatesWithVotes = []

CandidateVotes = {}





## Open the CSV

with open(csv_Path, newline = "") as csv_File:



  # Initiate csv reader

  csv_Reader = csv.reader(csv_File, delimiter = ",")

  # print(csv_Reader)



  # Read Header row

  csv_Header = next(csv_File)

  # print(f'\nHeader: {csv_Header}')



  # Read each row of data

  for x in csv_Reader:



    # Add to the total votes

    TotalVotes = TotalVotes + 1



    # Extract candidate name 

    CandidateName = x[2]

   

    # If Candidate not in existing Candidate With Votes list...

    if CandidateName not in CandidatesWithVotes:



      # Add Candidate to the list

      CandidatesWithVotes.append(CandidateName)



      # Track Candidate votes

      CandidateVotes[CandidateName] = 0

    

    # Add a vote to the Candidates count

    CandidateVotes[CandidateName] = CandidateVotes[CandidateName] + 1





    # Loop through the candidates to determine winner

    for y in CandidateVotes:

      

      # Determine vote counts and percentages

      Votes = CandidateVotes.get(CandidateName)

      VotePercent = (float(Votes) / float(TotalVotes)) * 100



      # Determine the Winner

      if Votes > WinningVoteCount:

        WinningVoteCount = Votes

        WinningCandidate = CandidateName

        WinningPercent = round((WinningVoteCount / TotalVotes) * 100 , 2)



  # Loop through candidates and print votes and percentage

  for k, v in CandidateVotes.items():

    Percent = (v / TotalVotes) * 100

    print(k , v , str(round(Percent,2)) + "%")

    



# Print Output  

print(f'\nTotal Votes: {TotalVotes}')

print(f'\nWinner: {WinningCandidate} with {WinningVoteCount} votes ({WinningPercent}%).')





# Use os module to specify output file to WRITE to

csv_Output_Path = os.path.join("PyPollResults.txt")



# Open the output file using WRITE mode

with open(csv_Output_Path, "w", newline = "") as csv_File_Out:



    # Initialize csv.writer

    csv_Writer = csv.writer(csv_File_Out)



    # Write results to text file

    csv_Writer.writerow(["Results"])

    csv_Writer.writerow(["----------"])

    csv_Writer.writerow(["Total Votes: " + str(TotalVotes)])

    csv_Writer.writerow(["----------"])



    # Loop through candidates and print votes and percentage

    for k, v in CandidateVotes.items():

      Percent = (v / TotalVotes) * 100

      csv_Writer.writerow([k , v, str(round(Percent,2)) + "%"]) 



    # Output winner

    csv_Writer.writerow(["----------"])

    csv_Writer.writerow(["Winner: " + WinningCandidate + " with " + 

                          str(WinningVoteCount) + " votes (" + str(WinningPercent) + "%)."])
