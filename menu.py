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
    """View a single product's inventory"""
    dbhandler.search_products(input("Enter an ID number: "))
    

def add_product():
    """Add a new product to the database"""
    name = input("Please enter the product name: ")
    quantity = int(input("Please enter the quantity: "))
    price = input("Please enter the price: $")
    formatted_price = int("".join(price.split('.')))
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    dbhandler.add_product(name, formatted_price, quantity, date)


def display_product(product):
    """Displays product(s) to the user"""
    price_as_str = str(product.product_price)
    print('Product Name: {}'.format(product.product_name))
    print('Price: ${}.{}'.format(price_as_str[0], price_as_str[1::]))
    print('Quantity: {}'.format(int(product.product_quantity)))
    print('Date Updated: {}'.format(datetime.datetime.strftime(
        product.date_updated, '%d/%m/%Y'
        )))
    input('Press enter to return to the main menu')


def backup_database():
    """Make a backup of the entire inventory"""
    dbhandler.backup_database()

menu = OrderedDict([
    ('v', view_product),
    ('a', add_product),
    ('b', backup_database)
])