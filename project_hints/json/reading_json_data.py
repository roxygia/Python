import json
import pprint

with open("data/quiz.json") as json_file:
    json_data = json.load(json_file)
pprint.pprint(json_data)

for row in json_data:
    line_count = 0
    if line_count == 0:
        print(f'Column names are {", ".join(row)}')
        line_count += 1
    print(f'\t{row["question"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
    line_count += 1