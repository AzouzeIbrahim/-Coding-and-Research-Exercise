from pydriller import Repository
from collections import Counter
import csv
from datetime import datetime

# the project 
repo = Repository('https://github.com/numpy/numpy')
monthly_commits = Counter()
yearly_commits = Counter()

for commit in repo.traverse_commits():
    date = commit.author_date
    month_key = date.strftime('%Y-%m')  # YYYY-MM
    year_key = date.strftime('%Y')      # YYYY

    monthly_commits[month_key] += 1
    yearly_commits[year_key] += 1

#  Monthly  commits

monthly_csv = "monthly_commits.csv"

with open(monthly_csv, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Year", "Month", "Monthly Commits"])

    for month_key, count in sorted(monthly_commits.items()):
        year, month_num = month_key.split("-")
        month_name = datetime.strptime(month_num, "%m").strftime("%B")

        writer.writerow([year, month_name, count])


# Yearly commits 

yearly_csv = "yearly_commits.csv"

with open(yearly_csv, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Year", "Total Commits"])

    for year, count in sorted(yearly_commits.items()):
        writer.writerow([year, count])

print("CSV files successfully created:")
