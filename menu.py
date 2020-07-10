from collections import OrderedDict
import datetime
import os

import dbhandler
import csvhandler

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_loop():
    """Shows the menu to the user"""
    choice = None

    while choice != 'q':
        clear()
        print("Enter 'q' to quit.")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Action: ').lower().strip()

        if choice in menu:
            clear()
            menu[choice]()
        elif choice != 'q':
            input('Input is not valid, press return to try again.')

def view_product():
    """Search for product by ID number"""
    returned_product = dbhandler.search_products()
    if returned_product:
        name = returned_product.product_name
        price_as_str = str(returned_product.product_price)
        formatted_price = '${}.{}'.format(price_as_str[0], price_as_str[1::])
        quantity = returned_product.product_quantity
        date = returned_product.date_updated
        date_as_string = datetime.datetime.strftime(date, "%d/%m/%Y")
        print('Product Name: {}\n'.format(name))
        print('Price: {}\n'.format(formatted_price))
        print('Quantity: {}\n'.format(quantity))
        print('Date Updated: {}'.format(date_as_string))
        input()
    else:
        input("No match found for that requested ID. Press enter to return to the main menu")
    

def add_product():
    """Add a new product to the database"""
    name = input("Please enter the product name: ")
    clear()
    price = input("Please enter the price: $")
    formatted_price = int("".join(price.split('.')))
    clear()
    quantity = int(input("Please enter the quantity: "))
    clear()
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    dbhandler.Product.create(product_name = name, product_price = formatted_price,
    product_quantity = quantity, date_updated = date)


def backup_database():
    """Backup the database"""
    all_products = dbhandler.view_products()
    product_dictionaries = []
    for item in all_products:
        price_as_str = str(item.product_price)
        formatted_price = '${}.{}'.format(price_as_str[0], price_as_str[1::])
        product = {
            'name': item.product_name,
            'price': formatted_price,
            'quantity': str(item.product_quantity),
            'date_updated': datetime.datetime.strftime(item.date_updated, "%d/%m/%Y")
        }
        product_dictionaries.append(product)
    csvhandler.write_csv(product_dictionaries)

menu = OrderedDict([
    ('v', view_product),
    ('a', add_product),
    ('b', backup_database)
])