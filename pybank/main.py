# Dependencies
import csv

# Path to collect data from folder
budgetCSV = ("budget_data_1.csv")

# Read in the CSV file
with open(budgetCSV, newline="") as csvfile:
  csvreader= csv.reader(csvfile, delimiter=",")

  # define the function 
  def getTotals(budgetData)

      # Total number of months included in the dataset
      totalMonths = len(set(budgetData[1])

      # Average change in revenue between months over the entire period
      avgRevenue = (int(budgetData[2])/totalMonths)

      # Greatest increase in revenue (date and amount) over the entire period
      increase = (max(budgetData[2]))
      
      # Greatest decrease in revenue (date and amount) over the entire period
      decrease = (min(budgetData[2]))

      # Print Total Months:, Total Revenue:, Average Revenue Change:, Greatest Increase in Revenue:, Greatest Decrease in Revenue
      print("Financial Analysis")  
      print("---------------------------")
      print("Total Months: " + str(totalMonths))
      print("Total Revenue: " + str(avgRevenue))
      print("Greatest Increase in Revenue: " + budgetData[0] + "(" + str(increase) + ")")
      print("Greatest Decrease in Revenue: " + budgetData[0] + "(" + str(decrease) + ")")
  
  # Split the data on commas
  csvreader = csv.reader(csvfile, delimiter=',')
  
  


