import os
import csv
#define pathway of import
PyBank = os.path.join("Resources", "Python_Homework_PyBank.csv")


with open(PyBank, newline='') as csvfile:
    cvsreader  = csv.reader(csvfile, delimiter=',',quotechar='|')
    header = next(cvsreader)
    row_count=0
    total=0
    change=0
    average_change=0
    total_revenue=0
    max_revenue=0
    max_revenue_date=""
    min_revenue=0
    min_revenue_date=""
    csvwriter=csv.writer(f)
    current_revenue=0
    #total number of months
    for row in cvsreader:
        total += float(row[1])
       
        if (row_count== 0):
            previous_revenue= int(row[1])
            
        else: 
            current_revenue= int(row[1])
            total_revenue += (current_revenue-previous_revenue) 
            previous_revenue = current_revenue
            
            
        if (current_revenue > previous_revenue):
            max_revenue=current_revenue
            max_revenue_date=str(row[0]
            
        #if (current_revenue < previous_revenue):
          #  min_revenue=current_revenue
          #  min_revenue_date= str(row[0])
            
    row_count+=1

    average_change=total_revenue/(row_count-1)





   #this should be writing the results to a csv file...is it? How do I specify the results are what it's supposed to print? 
   #How do I get this to be a file that I can find and push to GitHub?
    #csvwriter.writerow([])

#I need to figure out how to get the min/max revenues to comapare to the previous cell and not to itself,
#which is what's happening in line 31, when the previous_revenue resets to the current_revenue. 
#Also need to figure out how to write to a csv file. 


    print ("Financial Analysis")
    print ("Number of Months:", row_count)
    print ("Total Change:", total)
    print ("Average Change:", average_change)
    print ("Greatest Increase in Profits:", max_revenue_date, max_revenue)
    print ("Greatest Decrease in Profits:", min_revenue_date, min_revenue)