#import
import os
import csv 

#files to import 
file = '../resources/election_data.csv'


candidates= {} 

with open (file, newline = "") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    
    for row in csvreader:
        if row[2] in candidates.keys():
            candidates[row[2]]+=1
        else:
            candidates[row[2]] = 1

        total = candidates.values()
        totalVotes = sum(total)

            
        list_candidates = candidates.keys()
            
        votes_per = [f'{(x/totalVotes)*100:.3f}%' for x in candidates.values()]
            

        winner = list(candidates.keys())[list(candidates.values()).index(max(candidates.values()))]
        winner
        
#print

print("Election results")
print("--------------------------------")
print(f" Total votes: {int(totalVotes)}")
print("---------------------------------")
i = 0
for candidate, vote in candidates.items():
    print(f'{candidate}, {vote} , {votes_per[i]}') 
    i+=1
print("------------------------------")
print(f" Winner: {winner}")
print("------------------------------")


#Write
textfile = open("Election Results.txt","w")
textfile.write("Election results\n")
textfile.write("--------------------------------\n")
textfile.write(f" Total votes: {int(totalVotes)}\n")
textfile.write("---------------------------------\n")
i = 0
for candidate, vote in candidates.items():
    textfile.write(f'{candidate}, {vote} , {votes_per[i]}\n') 
    i+=1
textfile.write("------------------------------\n")
textfile.write(f" Winner: {winner}\n")
textfile.write("------------------------------\n")
