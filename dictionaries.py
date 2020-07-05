groceries = {
    "Baby Spinach": 2.78,
    "Hot Chocolate": 3.70,
    "Crackers": 2.1
}

print(groceries)

cohorts = {
    "perth": ["Anna", "Viv", "Nic", "Teagen"],
    "brisbane": ["Teagan", "Vivian", "Nic", "Joy"]
}
print(cohorts)
for cohort, peeps in cohorts.items():
    print(cohort)
    for peep in peeps:
        print(peep)
    print()


all_cohorts = {
    2019: {
        "perth": ["Anna", "Sarah", "Nina", "Ellie"]
    },
    2020: {
        "perth": ["Anna", "Viv", "Nic", "Teagen"],
        "brisbane": ["Teagan", "Vivian", "Nic", "Joy"]
    }
}

# for year, cohorts in all_cohorts.items():
#     print(year)
#     for city, cohort in cohort.items():
#         print(city, cohort)
#         for peep in cohort:
#             print(peep)

print(all_cohorts[2020]["perth"][0])

#

import csv

with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')

import csv

with open('employee_birthday.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')