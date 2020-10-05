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
    #csvwriter=csv.writer(f)

    #the number of votes cast
    #this currently works
    for row in csvreader:
        row_count+=1

        if (row[2] not in candidates_and_votes):
            candidates_and_votes[row[2]]=1

        else:
            candidates_and_votes[row[2]]+=1

    print ("WINNER: ",max(candidates_and_votes, key=candidates_and_votes.get))
    print (candidates_and_votes)

    Khan_votes = candidates_and_votes["Khan"]
    Correy_votes = candidates_and_votes["Correy"]
    Li_votes = candidates_and_votes["Li"]
    Otooley_votes = candidates_and_votes["O'Tooley"]

    print (Khan_votes)



    #make a list of the candidates' counts
  #  winner_picker=[Khan_count, Correy_count, Li_count, Otooley_count]
  #use max() to find the max value and therefore the winner
   # print ("Winner", max(winner_picker) )   

    #percentage of each candidate's votes
  # percentage_Khan=Khan_count/row_count*100
  # percentage Correy=Correy_count/row_count*100
  # percentage_Li=Li_count/row_count*100
   #percentage_Otooley=Otooley_count/row_count*100

    #this should be writing the results to a csv file...is it? How do I specify the results are what it's supposed to print?
   # csvwriter.writerow([])

print ("ElEction Results")

print ("Total Votes:", row_count)

print (candidates_and_votes["Khan"])
#print ("Khan:", Khan_count)
#print ("Correy:", Correy_count)
#print ("Li:", "Li_Count")
#print ("Otooley:", Otooley_count)
#print ("winner:", max(winner_picker))
#print (candidate_name)