#Q3) Using our colour files from a previous exercise, create a list of colours where each item in the list is a
#dictionary containing the different representations for each colour.

import csv
import pprint

# Function to convert a csv file to a list of dictionaries.takes in filepath
 
def csv_dict_list(filepath):
    # Open variable-based csv, iterate over the rows and map values to a list of dictionaries containing key/value pairs
    reader = csv.DictReader(open(filepath))
    dict_list = []
    for line in reader:
        dict_list.append(line)
    return dict_list
 
# Calls the csv_dict_list function, passing the named csv
colour_values = csv_dict_list('colours_20.csv')
# Prints the results nice and pretty like

print(colour_values)
pprint.pprint(colour_values)
 

