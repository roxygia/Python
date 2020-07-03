#Q1) Continuously ask the user to enter a number 
# until they provide a blank input. 
# Output the sum of all the numbers.

sum = 0

new_number = input("Enter a number to sum or space to exit: ")


while new_number !=" ":
    sum = sum + int(new_number)
    new_number = input("Enter a number to sum or space to exit: ")

print(sum) 