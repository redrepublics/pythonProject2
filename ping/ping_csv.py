import csv
from ping_params import hostname


def csv_read():
    with open('ping.csv', newline='') as File:
        reader = csv.reader(File)
        for row in reader:
            x = ",".join(row)
            hostname.append(x)
    return hostname

