def calculate_mean(total_sum, num_items):
    return total_sum/num_items




numbers= []
sum = 0
new_number = input("Enter a number to sum or space to exit: ")


while new_number !=" ":
    sum = sum + int(new_number)
    numbers.append(new_number)
    new_number = input("Enter a numbers for mean average or space to exit: ")

print(calculate_mean(sum, len(numbers)))