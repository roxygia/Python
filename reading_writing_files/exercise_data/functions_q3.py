import csv

def read_csv_file(filepath):
    import csv
    with open(filepath) as csv_file:
        #make sure you cast the reader into a "list" before returning it if you open csv
        #without casting you returne a generator on the file object - not fully processed.
        # That file was closed when you left the with block in the function.
        reader = list(csv.reader(csv_file, delimiter=","))
    return reader


def format_colour_line(colour_data):
    for line in colour_data:
      print(f"{line[1]:<15} {line[2]:<10} {line[4]:<20}")


colours = read_csv_file("colours_20.csv")
format_colour_line(colours)

colours = read_csv_file("colours_213.csv")
format_colour_line(colours)



