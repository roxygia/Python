#Q4) Write a program that asks the user for their height, 
# and determine whether or not they are tall enough to
#ride the rollercoaster, which has a height requirement of 120cms.

height = int(input("What is your height in cm? "))

if height >= 120:
    print("Hop on!")
else:
    print("Sorry, not today :(")