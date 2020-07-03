#Q3) Use a while loop to ask the user for three names and append them to a list, then use a for loop to print the

names = []

while len(names) < 3:
    name = input("What's the name? ")
    names.append(name)

for name in names:
    print(name) 