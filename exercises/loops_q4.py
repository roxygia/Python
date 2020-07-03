#Q4) Below is a list of foods and their prices per unit:

groceries = [
["Baby Spinach", 2.78],
["Hot Chocolate", 3.70],
["Crackers", 2.10],
["Bacon", 9.00],
["Carrots", 0.56],
["Oranges", 3.08]
]

sum = 0

for item in groceries:
    number = int(input(f"How many/much {item[0]} did you buy? "))
    item.append(number)

print()
print("====Roxy's Food Emporium====")

for item in groceries:
    sum = sum + float(item[1]*item[2])
    print(f"{item[0]:<20} ${item[1]*item[2]:.2f}")

print("============================")
symbol ="$"

print(f"{symbol:>22}{sum:.2f}")
