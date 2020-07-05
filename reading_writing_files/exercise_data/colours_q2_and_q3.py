import csv

colours = []
red_counter = 0
green_counter = 0
blue_counter = 0

with open("colours_20.csv") as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    
    for line in reader:
        colours.append(line)
        print(f"{line[1]:<15} {line[2]:<10} {line[4]:<20}")
        if "red" in line[4]:
            red_counter += 1
        if "green" in line[4]:
            green_counter += 1
        if "blue" in line[4]:
            blue_counter += 1

print()
print(f"Red: {red_counter} ")
print(f"Green: {green_counter} ")
print(f"Blue: {blue_counter} ")
red_counter = 0
green_counter = 0
blue_counter = 0


print()
with open("colours_213.csv") as csv_file:
    reader = csv.reader(csv_file, delimiter=",")
    
    for line in reader:
        colours.append(line)
        print(f"{line[1]:<15} {line[2]:<10} {line[4]:<20}")
        if "red" in line[4]:
            red_counter += 1
        if "green" in line[4]:
            green_counter += 1
        if "blue" in line[4]:
            blue_counter += 1

print()
print(f"Red: {red_counter} ")
print(f"Green: {green_counter} ")
print(f"Blue: {blue_counter} ")

