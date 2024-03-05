import csv

with open('path/to/your/file.csv', 'r') as dosya:
    csv_reader = csv.reader(dosya)
    for satir in csv_reader:
        print(satir)
