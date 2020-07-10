import csv
from datetime import datetime

def read_csv():
    """reads data from csv file"""
    with open("inventory.csv", newline='') as csvfile:
        inventory_reader = csv.reader(csvfile, delimiter=',')
        rows = list(inventory_reader)[1::]
        # return rows
        products = []
        for row in rows:
            # create dictionary
            product = {}
            # add name
            product['name'] = row[0]
            # convert price and add price
            product['price'] = int("".join(row[1].strip('$').split('.')))
            # convert quantity and add quantity
            product['quantity'] = int(row[2])
            # convert string to datetime and back to properly formatted string
            date_time_str = row[3]
            date_time_obj = datetime.strptime(date_time_str, '%m/%d/%Y')
            product['date_updated'] = datetime.strftime(date_time_obj, '%Y-%m-%d')
            # add dictionary to data
            products.append(product)
        return products
            
