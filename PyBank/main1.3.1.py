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
    current_revenue=0
    previous_revenue=0
    revenue_delta=0.0
    max_revenue_delta=0.0
    min_revenue_delta=0.0
    #csvwriter=csv.writer(f)

    #total number of months
    for row in cvsreader:
        total += float(row[1])
        current_revenue=int(row[1])   
       
        if (row_count== 0):
            previous_revenue= int(row[1])
            
        else: 
            #current_revenue= int(row[1])
            revenue_delta=(current_revenue-previous_revenue)
            total_revenue +=revenue_delta
            #previous_revenue = current_revenue
            
            if (revenue_delta > max_revenue_delta):
                max_revenue_delta=revenue_delta
                max_revenue_date=str(row[0])

            if (revenue_delta < min_revenue_delta):
                min_revenue_delta=revenue_delta
                min_revenue_date= str(row[0])
            
            previous_revenue = current_revenue
        row_count+=1

    average_change=total_revenue/(row_count-1)



   
   
    


    print ("Financial Analysis")
    print ("Number of Months", row_count)
    print ("Total Change", total)
    print ("Average Change", average_change)
    print ("Max Revenue", max_revenue_delta)
    print ("Max Revenue Date", max_revenue_date)
    print ("Min Revenue", min_revenue_delta)
    print ("Min Revenue Date", min_revenue_date)
   #this should be writing the results to a csv file...is it? How do I specify the results are what it's supposed to print? 
   #How do I get this to be a file that I can find and push to GitHub?
    #csvwriter.writerow([])

