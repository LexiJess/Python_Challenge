import os
import csv
#define pathway of import
PyPoll = os.path.join("Resources", "Python_Homework_PyPoll.csv")


with open(PyPoll, newline='') as csvfile:
    csvreader  = csv.reader(csvfile, delimiter=',',quotechar='|')
    header = next(csvreader)
    row_count=0
    total=0
    candidates=[]
    candidates_and_votes={}


    #the number of votes cast
    for row in csvreader:
        row_count+=1

        if (row[2] not in candidates_and_votes):
            candidates_and_votes[row[2]]=1

        else:
            candidates_and_votes[row[2]]+=1

    
    #naming the number of votes each received
    Khan_votes = candidates_and_votes["Khan"]
    Correy_votes = candidates_and_votes["Correy"]
    Li_votes = candidates_and_votes["Li"]
    Otooley_votes = candidates_and_votes["O'Tooley"]


    #percentage of each candidate's votes
    percentage_Khan=Khan_votes/row_count*100
    percentage_Correy=Correy_votes/row_count*100
    percentage_Li=Li_votes/row_count*100
    percentage_Otooley=Otooley_votes/row_count*100


    print ("Election Results")
    print ("--------------------")
    print ("Total Votes:", row_count)
    print ("------------------------")
    print ("Khan: {:.3f}% ({})".format(percentage_Khan, Khan_votes))
    print ("Correy: {:.3f}% ({})".format(percentage_Correy, Correy_votes))
    print ("Li: {:.3f}% ({})".format( percentage_Li, Li_votes))
    print ("Otooley: {:.3f}% ({})".format(percentage_Otooley, Otooley_votes))
    print ("--------------------------")
    print ("WINNER: ",max(candidates_and_votes, key=candidates_and_votes.get))

    with open("output.txt","w") as outfile:

        outfile.write ("Election Results")
        outfile.write ("--------------------")
        outfile.write ("Total Votes"== int(row_count))
        outfile.write ("------------------------")
        outfile.write ("Khan: {:.3f}% ({})".format(percentage_Khan, Khan_votes))
        outfile.write ("Correy: {:.3f}% ({})".format(percentage_Correy, Correy_votes))
        outfile.write ("Li: {:.3f}% ({})".format( percentage_Li, Li_votes))
        outfile.write ("Otooley: {:.3f}% ({})".format(percentage_Otooley, Otooley_votes))
        outfile.write ("--------------------------")
        outfile.write("WINNER: ",max(candidates_and_votes, key=candidates_and_votes.get))