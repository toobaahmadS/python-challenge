import csv
import os

#path to collect data
csvpath = os.path.join("Resources", "budget_data.csv")
csvpath_output = os.path.join("analysis", "text_path.txt")
# Variables to Track
total_months = 0
total_profit_loss = 0

prev_profit_loss = 0
profit_loss_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999]

profit_loss_changes = []
# Read Files
with open(csvpath) as csvfile:
    reader = csv.DictReader(csvfile)

        #loop through rows and add up the total months and profit losses 
    for row in reader:


        total_months = total_months + 1
        total_profit_loss = total_profit_loss + int(row["Profit/Losses"])
        print(row)

            # Keep track of changes
        profit_loss_change = int(row["Profit/Losses"]) - prev_profit_loss
        print(profit_loss_change)

            # Reset the value of prev_profit_loss to the complete row 
        prev_profit_loss = int(row["Profit/Losses"])
        print(prev_profit_loss)

            # Determine the greatest increase
        if (profit_loss_change > greatest_increase[1]):
                greatest_increase[1] = profit_loss_change
                greatest_increase[0] = row["Date"]

        if (profit_loss_change < greatest_decrease[1]):
                greatest_decrease[1] = profit_loss_change
                greatest_decrease[0] = row["Date"]
                    # Add to the profit_loss_changes list
        profit_loss_changes.append(int(row["Profit/Losses"]))

        # create the profit loss average
        profit_loss_avg = sum(profit_loss_changes) / len(profit_loss_changes) 

    # Show Output
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(total_months))
    print("Total : " + "$" + str(total_profit_loss))
    print("Average Change: " + "$" + str(round(sum(profit_loss_changes) / len(profit_loss_changes),2)))
    print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
    print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")
    # Output Files
with open(csvpath_output, "w") as txt_file:
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total: " + "$" + str(total_profit_loss))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(sum(profit_loss_changes) / len(profit_loss_changes),2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")