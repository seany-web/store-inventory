import csv
from datetime import datetime

def read_csv():
    """reads data from csv file"""
    with open("inventory.csv", newline='') as csvfile:
        inventory_reader = csv.reader(csvfile, delimiter=',')
        rows = list(inventory_reader)[1::]
        products = []
        for row in rows:
            product = {}
            product['name'] = row[0]
            product['price'] = int("".join(row[1].strip('$').split('.')))
            product['quantity'] = int(row[2])
            date_time_str = row[3]
            date_time_obj = datetime.strptime(date_time_str, '%m/%d/%Y')
            product['date_updated'] = datetime.strftime(date_time_obj, '%Y-%m-%d')
            products.append(product)
        return products

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


            
