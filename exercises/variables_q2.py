#Q2 Write a program that takes two numbers from the user, and outputs the equation representing the
# multiplication of the two numbers.


print("This program will multiply the two values entered")
value_a = input("Enter the first value ")
value_b = input("Enter the second value ")


if (value_a.find('.') > 0):
    value_a = float(value_a)
else:
    value_a = int(value_a)

if (value_b.find('.') > 0):
    value_b = float(value_b)
else:
    value_b = int(value_b)

print(value_a * value_b)


