#homework objective
    #import csv
    #The total number of months included in the dataset
    #The net total amount of "Profit/Losses" over the entire period
    #The average of the changes in "Profit/Losses" over the entire period
    #The greatest increase in profits (date and amount) over the entire period
    #The greatest decrease in losses (date and amount) over the entire period
    #In addition, your final script should both print the analysis to the 
    # # terminal and export a text file with the results.

#import csv file
import csv

#makeing variables
dates = []
profits = []
max(profits)
min(profits)
row = 0


#flag that says whether or not we recorded a first value yet


#reading csv file
with open (r"C:\Users\tamal\Desktop\PyBank\budgetdata.csv") as csvfile:
    csvreader = csv.reader(csvfile)
    
    csvheader = next(csvreader)
    print(f"CSV Header: {csvheader}")
    

    for row in csvheader:
        # The total number of months included in the dataset by using the count_row
        total_months = int(row + 1)
        
        # The greatest increase in profits (date and amount) over the entire period
        greatest_decrease = max(profits)
        greatestprofit = profits.index(max(profits))
        profitdate = dates[greatestprofit]    
   
        # The net total amount of "Profit/Losses" over the entire period
        totalpl = totalpl + int(row[1])

        # The average of the changes in "Profit/Losses" over the entire period. use change list and total months
        avgchange = sum(profits)/len(profits)
    
        # The greatest decrease in losses (date and amount) over the entire period
        greatest_decrease = min(profits)
        greatestloss = profits.index(greatest_decrease)
        lossdate = dates[greatestloss]


# In addition, your final script should both print the analysis to the 
#terminal and export a text file with the results.
