# Import dependencies
import os
import csv

# Open my file
budget_data = os.path.join("/Users/omarkreidieh/Documents/GitHub/python-challenge-oct/PyBank/Resources", "budget_data.csv")

with open(budget_data, newline = "") as budgetdata:
    budget= csv.reader(budgetdata, delimiter = ',')
    budgetheader = next(budgetdata)
    print(budgetheader)
# Create a list with the different Dates and Profits/Losses
    Date = []
    Profit_Loss = []
    for row in budget:
        Date.append(row[0])
        Profit_Loss.append(int(row[1]))

 # Calculate the number of months, the Total profits,    
    Total_months = len(Date)
    Profit= sum(Profit_Loss)
    
# Create a list of the change between one month and the month before it
    Change = tuple(Profit_Loss[n]-Profit_Loss[n-1] for n in range(1,len(Profit_Loss)))
# The dates corresponding to those changes will be the dates starting with the second date i.e Date[1]. Create a tuple with those dates
    Change_Date = tuple(Date[n] for n in range(1, len(Change)))
# Calculate The required values. Average change could have also been calculated as the last profit/loss - the first over the number of months -1
    Average_Change= sum(Change)/len(Change)
    Greatest_increase= max(Change)
    Greatest_decrease = min(Change)
# Find out the index of the  change so I can figure out the corresponding month ( Alternative method would have been to create a dictionary and then use the greatest change as the key)
    index_Greatest_increase= Change.index(Greatest_increase)
    Greatest_increase_date= Change_Date[index_Greatest_increase]
    index_Greatest_decrease= Change.index(Greatest_decrease)
    Greatest_decrease_date= Change_Date[index_Greatest_decrease]
# Print out the results to text file!
outputtextfile = open("outputtextfile.txt","w") 
writelines= ["Financial Analysis \n","--------------------- \n", f"Total Months: {Total_months} \n", f"Total: ${Profit} \n", f"Average Change: ${Average_Change} \n", f"Greatest Increase in Profits: {Greatest_increase_date} (${Greatest_increase}) \n", f"Greatest Decrease in Profits: {Greatest_decrease_date} (${Greatest_decrease}) \n" ]
outputtextfile.writelines(writelines)

# Print out the results to terminal!
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {Total_months}")
print(f"Total: ${Profit}")
print(f"Average Change: ${Average_Change}")
print(f"Greatest Increase in Profits: {Greatest_increase_date} (${Greatest_increase})")
print(f"Greatest Decrease in Profits: {Greatest_decrease_date} (${Greatest_decrease})")



 



