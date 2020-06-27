# is_raining = True
# is_cold = False

# if is_raining:
#     print("You will need an umbrella today!")

# if is_cold:
#     print("You will need a jumper today!")

# temperature = 16

# if temperature < 12:
#     print("OMG is cold")
# else:
#     print("ugh is still warm")

temperature = 16
windchill = 4
is_cold = (temperature - windchill) <16

print(is_cold)

if (is_cold):
    print("You need a jumper")
else:
    print("No need for jumpers")

is_raining = False 

if is_cold and is_raining:
    print("Just stay home")
else:
    if is_raining:
        print("Take an umbrella")
    if is_cold:
        print("bring a jumper")