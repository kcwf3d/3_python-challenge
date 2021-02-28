import csv
import os

#files to upload
file = '../resources/budget_data.csv'

#list
months = []
total_profits = []

#open file
with open (file, newline = "") as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')

    csv_header = next(csvfile)
    

    for row in csvreader:
        months.append(row[0])
        total_profits.append(int(row[1]))
        
   
    #number of months
    month_count = len(months)
    
    #loop variables
    xx = 1
    yy = 0
    
    #placeholders
    avechange = (total_profits[1]-total_profits[0])
    changes = []
    
    #month loop
    for month in range(month_count-1):
        avechange = (total_profits[xx] - total_profits[yy])
        changes.append(int(avechange))
        xx+=1
        yy+=1
      
    avMonchange = round(sum(changes)/(month_count -1),2)

    #min and max
    min_change = min(changes)
    max_change = max(changes)

    #min and max months
    chng_i_min = changes.index(min_change)
    chng_i_max = changes.index(max_change)
    
    min_chng_month = months[chng_i_min + 1]
    max_chng_month = months[chng_i_max + 1]
  

#print
print("Financial Analysis")
print("-----------------------")
print(f"Months: {len(months)}")
print(f"Total: ${sum(total_profits)}")
print(f"Average Monthly Change: {avMonchange}")
print(f"Greatest Increase in Profits: {max_chng_month} (${max_change})")
print(f"Greatest Decrease in Profits: {min_chng_month} (${min_change})")

#tex file write
textfile = open("Financial_Analysis.txt","w")

textfile.write("Financial Analysis\n")
textfile.write("----------------------------\n")
textfile.write(f"Months: {len(months)}\n")
textfile.write(f"Total: ${sum(total_profits)}\n")
textfile.write(f"Average Monthly Change: {avMonchange}\n")
textfile.write(f"Greatest Increase in Profits: {max_chng_month} (${max_change})\n")
textfile.write(f"Greatest Decrease in Profits: {min_chng_month} (${min_change})\n")