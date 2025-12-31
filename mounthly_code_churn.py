from pydriller import Repository
from collections import defaultdict
import csv
from datetime import datetime

repo = Repository('https://github.com/numpy/numpy')

churn_per_month = defaultdict(lambda: {'added': 0, 'deleted': 0})
churn_per_year = defaultdict(lambda: {'added': 0, 'deleted': 0})


for commit in repo.traverse_commits():
    date = commit.author_date
    month_key = date.strftime('%Y-%m')  # YYYY-MM
    year_key = date.strftime('%Y')      # YYYY

    for f in commit.modified_files:
        churn_per_month[month_key]['added'] += f.added_lines
        churn_per_month[month_key]['deleted'] += f.deleted_lines
        churn_per_year[year_key]['added'] += f.added_lines
        churn_per_year[year_key]['deleted'] += f.deleted_lines


#  Monthly  churn 

monthly_csv = "monthly_code_churn.csv"

with open(monthly_csv, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Year",
        "Month",
        "Lines Added",
        "Lines Deleted"
    ])

    for month_key, churn in sorted(churn_per_month.items()):
        year, month_num = month_key.split("-")
        month_name = datetime.strptime(month_num, "%m").strftime("%B")

        writer.writerow([
            year,
            month_name,
            churn['added'],
            churn['deleted']
        ])


#  Yearly  churn 

yearly_csv = "yearly_code_churn.csv"

with open(yearly_csv, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([
        "Year",
        "Lines Added",
        "Lines Deleted"
    ])

    for year, churn in sorted(churn_per_year.items()):
        writer.writerow([
            year,
            churn['added'],
            churn['deleted']
        ])

print("CSV files successfully created:")

