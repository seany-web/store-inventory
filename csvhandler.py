import csv

def read_csv():
    """reads data from csv file"""
    with open("inventory.csv", newline='') as csvfile:
        inventory_reader = csv.reader(csvfile, delimiter=',')
        rows = list(inventory_reader)
        return rows
