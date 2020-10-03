import os
import csv
#define pathway of import
PyBank = os.path.join("..", "python-challenge", "Python_Homework_PyBank.csv")


with open('Python_Homework_PyBank.csv', newline='') as csvfile:
    cvsreader  = csv.reader(csvfile, delimiter=',',quotechar='|')
    header = next(cvsreader)
    row_count=0
    total=0
  
    for row in cvsreader:
       total += float(row[1])
       row_count+=1

    previous_revenue= int(row[1])
    averagechange= int(row[1])- previous_revenue/row_count
    #the math is wrong on this. How do I make int(row[1]) reference the previous row instead of itself?

    for row in csvreader:
        if float(row[1]) > float((row+1)[1]) then
            max=float(row[1])
        print max
        print row[0]
        #I think this will make print both the min value and the column A date that corresponds to the min value's row.
    
    if float(row[1]) <float((row+1)[1]) then
            min=float(row[1])
        #these (row+1)[1] lines need to be corrected
        print min
        print row[0]
    #I think this will make it print both the min value and the column A date that corresponds to the min value's row. 

        
    


print ("Financial Analysis")
print ("Number of Months", row_count)
print ("Total Change", total)
print ("Average Change", averagechange)



