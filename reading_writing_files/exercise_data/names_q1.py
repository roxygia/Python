#q1) For each name in names.txt, output the name and line number

names = []

with open("names.txt") as txt_file:
    for counter, line in enumerate(txt_file):
        line = line.strip()
        print(f"{counter}. {line}")

