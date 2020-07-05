#Q2) Given the list of names below, create a dictionary where each key is a name and the value is the number of
#times that name occurs in the list.

names = [
"Maddy", "Bel", "Elnaz", "Gia", "Izzy",
"Joy", "Katie", "Maddie", "Tash", "Nic",
"Rachael", "Bec", "Bec", "Tabitha", "Teagen",
"Viv", "Anna", "Catherine", "Catherine", "Debby",
"Gab", "Megan", "Michelle", "Nic", "Roxy",
"Samara", "Sasha", "Sophie", "Teagen", "Viv"
]

names_dict = {}

for name in names:
    names_dict[name] = names.count(name)
    
print(names_dict)
    