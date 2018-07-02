
import os
import csv

ElectData = os.path.join("Resources", "election_data.csv")

totalnumber = 0

canvote = 0

candidatelist = {}


with open(ElectData, newline="") as ElectData:

    csvreader = csv.reader(ElectData, delimiter=",")

    header = next(ElectData)



    for pypoll in csvreader:

        totalnumber = totalnumber +1  

        

        if pypoll[2] in candidatelist:

           candidatelist[pypoll[2]] += 1

        else:

           candidatelist[pypoll[2]] = 1



    print("------------------------------------------------------------------")    

    print("Total Votes: " + str(totalnumber))

    print("------------------------------------------------------------------")

    

    maxvote = max(candidatelist.values())

    for canvote in candidatelist:

        voterate = candidatelist[canvote] / totalnumber * 100

        if candidatelist[canvote] == maxvote:

           x = canvote

        print(canvote + ": " + "{0:.3f}".format(voterate) + "% " + "(" + str(candidatelist[canvote]) + ")")

    print("------------------------------------------------------------------") 

    print("Winner: " + x)


for name in clean_data:

    if max(num_votes) == name[1]:

        winners_list.append(name[0])

output_file = os.path.join('Output', 'election_results_' + str(file_num) +'.txt')


print("Election Results")

print("--------------------------")

print("Total Votes: " + str(total_votes))

print("--------------------------")





print("Winner: " + winner)



with open(output_file, 'r') as readfile:

    print(readfile.read())
