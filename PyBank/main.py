

# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

print(os.path.dirname(__file__))
os.chdir(os.path.dirname(__file__))

csvpath = os.path.join("..", "Resources", "budget_data.csv")

print("Financial Analysis")
print("-----------------------------------")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    months = []
    for row in csvreader:
        months.append(row[0])

    print(f"Total Months: {len(months)}")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    profits_losses = []
    for row in csvreader:
      profits_losses.append(int(row[1]))

    print(f"Total Net Amount: ${sum(profits_losses)}")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    revenue = []
    date = []
    rev_change = [0]

    for row in csvreader:

        revenue.append(float(row[1]))
        date.append(row[0])


    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])   
        avg_rev_change = sum(rev_change)/(len(rev_change)-1)

        max_rev_change = max(rev_change)

        min_rev_change = min(rev_change)

        max_rev_change_date = str(date[rev_change.index(max(rev_change))])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))])


    print("Avereage Change: $", round(avg_rev_change))
    print("Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_change,")")
    print("Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_change,")")

    