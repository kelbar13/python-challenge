# Dependencies
import csv

# Path to collect data from folder and define results file
budgetCSV = ("budget_data_1.csv")

# Empty lists to store data
total_months = []
total_revenue = []
average_revenue = []
greatest_increase = []
greatest_decrease = []

revenue = int(0)
months = 0 
avgRevenue = int(0)
revIncrease = int(0)
revDecrease = int(0)
revChange = int(0)
preRev = int(0)
value = int(0)
revIncreaseDate = ""
revDecreaseDate = ""
# Read in the CSV file
with open(budgetCSV, newline="") as csvfile:
    csvreader= csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
            
        # Total number of months
        months += 1
        total_months.append(months)
    
        # Total revenue over period           
        value = int(row[1])
        revenue = revenue + value
        revChange = value - preRev
        preRev = value
        total_revenue.append(revenue)
    
        # Average Revenue Change
        avgRevenue = (revenue/months)
        average_revenue.append(avgRevenue)
    
        # Greatest Increase in Revenue
        if revIncrease < revChange:
            revIncrease = revChange
            revIncreaseDate = row[0]
        greatest_increase.append(revIncrease)
    
        #Greatest Decrease in Revenue
        if revChange < revDecrease:
            revDecrease = revChange
            revDecreaseDate = row[0]
        greatest_decrease.append(revDecrease)
    
    # Print Total Months:, Total Revenue:, Average Revenue Change:, Greatest Increase in Revenue:, Greatest Decrease in Revenue
    print("Financial Analysis")  
    print("---------------------------")
    print("Total Months: " + str(months))
    print("Total Revenue: " + str(revenue))
    print("Average Revenue Change: " + str(avgRevenue))
    print("Greatest Increase in Revenue: " + str(revIncreaseDate) + "(" + str(revIncrease) + ")")
    print("Greatest Decrease in Revenue: " + str(revDecreaseDate) + "(" + str(revDecrease) + ")")
    
# Output file
output_file = ("budget_results.txt")
    
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerows(output_file)

  
  


