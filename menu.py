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
        print('Main Menu')
        print('=' * 9)
        print("\nSelect an option from the menu or press 'q' to quit\n")
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('\nAction: ').lower().strip()

        if choice in menu:
            clear()
            menu[choice]()
        elif choice != 'q':
            print("\n'{}' is not a valid option.".format(choice))
            input('\nPress [enter] to try again.')


def view_product():
    """View a single product's inventory"""
    try:
        dbhandler.search_products(input("Please enter an ID number: "))
    except ValueError:
        print('Input is not valid.')
        view_product()
    


def add_product():
    """Add a new product to the database"""
    name = input("Please enter the product name: ")
    quantity = int(input("Please enter the quantity: "))
    price = input("Please enter the price: $")
    formatted_price = int("".join(price.split('.')))
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    dbhandler.add_product(name, formatted_price, quantity, date)
    print('\nProduct has been added to the database!')
    return_to_menu()


def display_product(product):
    """Displays product(s) to the user"""
    price_as_str = str(product.product_price)
    print('\nProduct Details')
    print('=' * 15)
    print('\nProduct Name: {}'.format(product.product_name))
    print('Price: ${}.{}'.format(price_as_str[0], price_as_str[1::]))
    print('Quantity: {}'.format(int(product.product_quantity)))
    print('Date Updated: {}'.format(datetime.datetime.strftime(
        product.date_updated, '%d/%m/%Y'
        )))
    return_to_menu()


def backup_database():
    """Make a backup of the entire inventory"""
    dbhandler.backup_database()
    print('Database has been backed up!')
    return_to_menu()


def return_to_menu():
    """Prompt user to return to main menu"""
    input('\nPress [enter] to return to the main menu')


menu = OrderedDict([
    ('v', view_product),
    ('a', add_product),
    ('b', backup_database)
])
