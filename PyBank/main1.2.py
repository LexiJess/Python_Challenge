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
    #csvwriter=csv.writer(f)

    #total number of months
    for row in cvsreader:
        total += float(row[1])
       
        if (row_count== 0):
            previous_revenue= int(row[1])
            
        else: 
            current_revenue= int(row[1])
            total_revenue += (current_revenue-previous_revenue) 
            previous_revenue = current_revenue
            
            current_revenue > previous_revenue
            max_revenue=current_revenue
            max_revenue_date=str(row[0])

            current_revenue < previous_revenue
            min_revenue=current_revenue
            min_revenue_date= str(row[0])

        row_count+=1

    average_change=total_revenue/(row_count-1)

    #for row in cvsreader:
     #   if  current_revenue > previous_revenue
      #      max_revenue=current_revenue
       #     max_revenue_date=str(row[0])
     

    #for row in csvreader:
        #if (float(row[1])) > float((row+1)[1]):
            #max=float(row[1])
            #print (max)
            #print (row[0])
        #I think this will make print both the min value and the column A date that corresponds to the min value's row.
    
        #if float(row[1]) <float((row+1)[1]):
         #   min=float(row[1])
        #these (row+1)[1] lines need to be corrected
          #  print (min)
           # print (row[0])
    #I think this will make it print both the min value and the column A date that corresponds to the min value's row. 
   
    


    print ("Financial Analysis")
    print ("Number of Months", row_count)
    print ("Total Change", total)
    print ("Average Change", average_change)
    print ("Max Revenue", max_revenue)
    print ("Max Revenue Date", max_revenue_date)
    print ("Min Revenue", min_revenue)
    print ("Min Revenue Date", min_revenue_date)
   #this should be writing the results to a csv file...is it? How do I specify the results are what it's supposed to print? 
   #How do I get this to be a file that I can find and push to GitHub?
    #csvwriter.writerow([])

