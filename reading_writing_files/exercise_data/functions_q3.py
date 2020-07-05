def read_csv_file(filepath):
    import csv
    with open("colours_20.csv") as csv_file:
    reader = csv.reader(csv_file, delimiter=",")


def format_colour_line(colour_data):
    return