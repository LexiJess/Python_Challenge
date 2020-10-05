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
            
            if (row_count==1):
                max_revenue_delta=revenue_delta
                min_revenue_delta=revenue_delta

            else:
                    
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
    print ("Greatest Increase in Profits:", max_revenue_date, max_revenue_delta)
    print ("Greatest Decrease in Profits:", min_revenue_date, min_revenue_delta)
   
    with open("output.txt","w") as outfile:

        outfile.write ("Financial Analysis")
        outfile.write ("Number of Months {}".format(row_count))
        outfile.write ("Total Change{}".format(total))
        outfile.write ("Average Change{}".format(average_change))
        outfile.write ("Max Revenue {}".format(max_revenue_delta))
        outfile.write ("Max Revenue Date{}".format(max_revenue_date))
        outfile.write ("Min Revenue{}".format(min_revenue_delta))
        outfile.write("Min Revenue Date{}".format(min_revenue_date))
        

