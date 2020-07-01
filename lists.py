# print("lists yay!")

tea_collection = ["Earl Grey", "Peppermint", "Lemon and Ginger", "Strawberry Cream"]

print (tea_collection)

# print(tea_collection[0])

# print(tea_collection[0:1])
# print(tea_collection[2:4])

# print(tea_collection[-1])

# print(tea_collection[-3:])
# print()

# print(len(tea_collection))

# # add one item with append
tea_collection.append("Chai")
print()

# # add multiple items with extend
# tea_collection.extend(["New York Breakfast","Berry"])
# print(tea_collection)

#remove last item with pop or specified index item
# print(tea_collection.pop(1))

# #remove an item by name - remove
# tea_collection.remove("Chai")
# print(tea_collection)

# #clear the list with - clear
tea_collection.clear()
print(tea_collection)

tea_collection = [
    ["Earl Grey", "Potato"],
    ["flower 1, rose, magenta"],
    ["red", "blue", "chai"]
]

print(tea_collection)

tea_collection.append(["Chamomile", "Green"])
print(tea_collection)

if "Chai" in tea_collection:
    print("Yay we got chai")

