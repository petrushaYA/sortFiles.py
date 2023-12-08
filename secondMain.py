import csv

with open('new_file.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=';')
    writer.writerow(['row 1 el 1', 'row 1 el 2', 'row 1 el 3'])