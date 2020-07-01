# Q1 
print("Q1 Answers:")
foods = [
    "orange",
    "apple",
    "banana",
    "strawberry",
    "grape","blueberry",
    ["carrot", "cauliflower", "pumpkin"],
    "passionfruit",
    "mango",
    "kiwifruit"
]

print(foods[0])
print(foods[2])
print(foods[-1])
print(foods[0:3])
print(foods[-3:])
print(foods[-4][2])
print()

# Q2 Format and print the following list:

print("Q2 Answers: print the list of emails")
mailing_list = [
["Roary", "roary@moth.catchers"],
["Remus", "remus@kapers.dog"],
["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
["Biscuit", "biscuit@whippies.park"],
["Rory", "rory@whippies.park"],
]

for contact in mailing_list:
    print(contact[0],":", contact[1])

print()

# Q3 Format and print the following list:

print("Q3 Answers: enter 3 names and print them as a list")

names = []
while len(names) < 3:
    name = input("Enter name: ")
    names.append(name)
print(names)

print()

# Q4
# 1. Ask the user to enter a string.
# 2. Split the string into a list, divided by spaces (hint: yourlist.split() will be useful).
# 3. Convert the string to a list, where each character is an item in the list (hint: list(yourlist) will be
# useful).
# 4. For each list: output the length of the list, and the list itself

print("Q4 Answers: split a string in words and characters")

string = input("Enter string: ")
words = string.split()

print(len(words), list(words))
print(len(string), list(string))
    

    




