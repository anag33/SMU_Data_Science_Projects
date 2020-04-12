# Modules
import csv

# Set path for file
csvpath = r"Submissions\PyBank\Resources\budget_data.csv"

# Counter for the months
tMonths = 0

# Set total profit
tProfit = 0

# Set beginning profit
bProfit = 0

# Set row count
rowCount = 0

profitChanges = []

averageChange = 0

greatestIncrease = 0

greatestDecrease = 0

dates = []


# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    

    # Loop through rows
    for row in csvreader:
        #Increment total months
        tMonths += 1
        

        #increment profit
        tProfit += int(row[1])
        dates.append(row[0])

        #skip header and calculate change
        if rowCount == 0:
            lProfit = int(row[1])
        else:
            bProfit = int(row[1])
            change = bProfit - lProfit
            profitChanges.append(change)

            lProfit = bProfit

        # Calculate average change
            averageChange = sum(profitChanges) / len(profitChanges)
            #month_of_change = [month_of_change] + [row["Date"]
            
        # Calculate Greatest Increase
            greatestIncrease = max(profitChanges)
            greatestIndex = profitChanges.index(max(profitChanges)) 
            greatestDate = dates[greatestIndex]

         

        # Calculate Greatest Decrease

            greatestDecrease = min(profitChanges)
            lowestIndex = profitChanges.index(min(profitChanges)) + 1
            lowestDate = dates[lowestIndex]
            

        rowCount += 1
        
       
        

# Print Results

print("Financial Analysis" + "\n")

print("..................................................."  + "\n" )

print("Total Months: " + str(tMonths) + "\n")

print("Total: " + "$" + str(tProfit) + "\n")

print("Average Change: " + "$" + str(round(averageChange, 2)) + "\n")

print("Greatest Increase in Profits: " + (greatestDate)  + " " + "$" + "(" + str(greatestIncrease) + ")" + "\n" )

print("Greatest Decrease in Profits: " + (lowestDate) + " " + "$" + "(" + str(greatestDecrease) + ")" + "\n" )

#Output to a text file

file = open("output.PyBanktext", "w")

file.write("Financial Analysis" + "\n")

file.write("..................................................."  + "\n" )

file.write("Total Months: " + str(tMonths) + "\n")

file.write("Total: " + "$" + str(tProfit) + "\n")

file.write("Average Change: " + "$" + str(round(averageChange, 2)) + "\n")

file.write("Greatest Increase in Profits: " + (greatestDate)  + " " + "$" + "(" + str(greatestIncrease) + ")" + "\n" )

file.write("Greatest Decrease in Profits: " + (lowestDate) + " " + "$" + "(" + str(greatestDecrease) + ")" + "\n" )

file.close()