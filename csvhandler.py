import csv
from datetime import datetime

import dbhandler

def read_csv():
    """reads data from csv file and calls method to add to the database"""
    with open("inventory.csv", newline='') as csvfile:
        inventory_reader = csv.reader(csvfile, delimiter=',')
        rows = list(inventory_reader)[1::]
        for row in rows:
            name = row[0]
            price = int("".join(row[1].strip('$').split('.')))
            quantity = int(row[2])
            date_updated = datetime.strptime(row[3], '%m/%d/%Y').strftime('%Y-%m-%d')
            dbhandler.add_product(name, price, quantity, date_updated)
        

def write_csv(products):
    """writes data to csv file"""
    with open('backup.csv', 'w', newline='') as backup:
        fieldnames = ['product_name', 'price', 'quantity', 'date_updated']
        productwriter = csv.DictWriter(backup, fieldnames=fieldnames)
        productwriter.writeheader()
        
        for product in products:
            productwriter.writerow({
                'product_name': product['name'],
                'price': product['price'],
                'quantity': product['quantity'],
                'date_updated': product['date_updated']
            })


            
