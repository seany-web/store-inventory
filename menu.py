from collections import OrderedDict
import datetime
import os

import dbhandler

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
    requested_id = input("Please enter the ID number you wish to search for: ")
    returned_product = dbhandler.get_product(requested_id)
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
    pass

def backup_database():
    """Backup the database"""
    pass

menu = OrderedDict([
    ('v', view_product),
    ('a', add_product),
    ('b', backup_database)
])