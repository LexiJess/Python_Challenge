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
    #csvwriter=csv.writer(f)

    #the number of votes cast
    #this currently works
    for row in csvreader:
        row_count+=1

    #list of candidates, unique names
    #for row in csvreader:
       # if (row_count== 0):
       #     candidate_name=str(row[2])
    #print (candidate_name)
        #else:
         #   current_revenue= str(row[2])
          #  total_revenue += (current_revenue-previous_revenue) 
           # previous_revenue = current_revenue""
               
    
    #this spells out O'Tooley (if I use x variable) which is not a complete list OR it returns an empty set of brackets if I use row[2] 
    #candidates=[]
    for row in csvreader:
        if x not in candidates:
            candidates.append(row[2])
print (candidates)

     #set up a loop to run through the file, looking for each candidate's votes and adding one to the Khan_count every time it sees one. 
   # for row in csvreader:
       # Khan_count=0
       # if row[3]==["Khan"]
        #    Khan_count=Khan_count+1

   # for row in csvreader:
    #    Otooley_count=0
     #   if row[3]==["O'Tooley"]
     #       Otooley_count=Otooley_count +1

   # for row in csvreader:
  #      Correy_count=0
     #   if row[3]==["Correy"]
         #   Correy_count=Correy_count+1

  #  for row in csvreader:
     #   Li_count=0
      #  if row[3]==["Li"]
         #   Li_count=Li_Count+1

   # print (Khan_count)
   # print (Correy_count)
   # print (Li_count)
  #  print (Otooley_count)

    #make a list of the candidates' counts
  #  winner_picker=[Khan_count, Correy_count, Li_count, Otooley_count]
    #use max() to find the max value and therefore the winner
   # print ("Winner", max(winner_picker) )   

    #this should be writing the results to a csv file...is it? How do I specify the results are what it's supposed to print?
   # csvwriter.writerow([])

print ("ElEction Results")

print ("Total Votes:", row_count)
#print (candidate_name)