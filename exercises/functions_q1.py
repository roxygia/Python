#q1

def convert_temp_celsius(temp):
    return int(temp)*1.8 +32

temp = input(" What is the temp in Celsius? ")

print(f"In Fahrenheit is {convert_temp_celsius(temp)}")

