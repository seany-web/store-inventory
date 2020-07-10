from collections import OrderedDict
import os


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
    pass

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