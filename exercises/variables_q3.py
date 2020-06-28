#Q3 Write a program that takes a distance in kilometers 
# from the user, and output the distance in meters and centimeters.



print("This program will take input distance in km and convert to m and cm")
distance_km = input("Enter the distance in km: ")

#caclulate distance in metres and print
distance_m = int(float(distance_km)*1000)
print(f"{distance_km}km = {distance_m}m")

#caclulate distance in cm and print
distance_cm = int(float(distance_m)*1000)
print(f"{distance_km}km = {distance_cm}cm")


