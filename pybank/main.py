# Dependencies
import csv

# Path to collect data from folder and define results file
budgetCSV = ("budget_data_2.csv")

# Empty lists to store data
total_months = []
total_revenue = []
average_revenue = []
greatest_increase = []
greatest_decrease = []

# Read in the CSV file
with open(budgetCSV, newline="") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
            
        # Total number of months
        months = 0
        months += 1
        total_months.append(months)
    
        # Total revenue over period 
        revenue = 0              
        revenue = sum(int(row[1]))
        total_revenue.append(revenue)
    
        # Average Revenue Change
        avgRevenue = (revenue/months)
        average_revenue.append(avgRevenue)
    
        # Greatest Increase in Revenue
        revIncrease = max(int(row[1]))
        greatest_increase.append(revIncrease)
    
        #Greatest Decrease in Revenue
        revDecrease = min(int(row[1]))
        greatest_decrease.append(revDecrease)
    
        # Print Total Months:, Total Revenue:, Average Revenue Change:, Greatest Increase in Revenue:, Greatest Decrease in Revenue
        print("Financial Analysis")  
        print("---------------------------")
        print("Total Months: " + (months))
        print("Total Revenue: " + (revenue))
        print("Average Revenue Change: " + (avgRevenue))
        print("Greatest Increase in Revenue: " + row[0] + "(" + (revIncrease) + ")")
        print("Greatest Decrease in Revenue: " + row[0] + "(" + (revDecrease) + ")")
    
# Output file
output_file = ("budget_results.txt")
    
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerows(output_file)

  
  


