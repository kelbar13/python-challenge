# Enter import modules
import csv
from datetime import datetime

# Path to collect data from folder
budgetCSV = ("budget_data_1.csv")

# Read in the CSV file
with open(budgetCSV, newline="") as csvfile:
  csvreader= csv.reader(csvfile, delimiter=",")
  for row in csvreader:
    # Total number of months included in the dataset
    
    # Total amount of revenue gained over the entire period
    # Average change in revenue between months over the entire period
    # Greatest increase in revenue (date and amount) over the entire period
    # Greatest decrease in revenue (date and amount) over the entire period
    # Print Total Months:, Total Revenue:, Average Revenue Change:, Greatest Increase in Revenue:, Greatest Decrease in Revenue:


  
  # Split the data on commas
  csvreader = csv.reader(csvfile, delimiter=',')
  
  


