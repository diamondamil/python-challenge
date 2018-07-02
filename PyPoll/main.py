
import os
import csv

file = os.path.join('raw_data', 'election_data_' + str(file_num) + '.csv')

with open(file, 'r') as csvfile:

    csvread = csv.reader(csvfile)

poll = {}
total_votes = 0
candidates = []
num_votes = []


for row in csvread:

    total_votes += 1

    if row[2] in poll.keys():

        poll[row[2]] = poll[row[2]] + 1

    else:

        poll[row[2]] = 1


for key, value in poll.items():

    candidates.append(key)

    num_votes.append(value)

vote_percent = []

for n in num_votes:

    vote_percent.append(round(n/total_votes*100, 1))


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
