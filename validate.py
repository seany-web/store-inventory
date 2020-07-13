import re

def validate_name():
    """Prompts user for product name and validates input"""
    name = None
    while True:
        name = input('Please enter the product name: ')
        if len(name) < 1:
            print('Input did not meet the minimum requirements\n')
            print('Product name must be a string of characters with a length greater than zero')
            continue
        break
    return name


def validate_quantity():
    """Prompts user for product quantity and validates input"""
    quantity = None
    while True:
        quantity = input('Please enter the quantity: ')
        try:
            quantity = int(quantity)
            if quantity < 0:
                print('Quantity must be a number greater or equal to zero\n')
                continue
            break
        except:
            print('{} is not a number.'.format(quantity))
            print('Quantity must be a number greater or eqal to zero\n')
            continue
    return quantity


def validate_price():
    """Prompts user for a product prictand validates input"""
    price = None
    while True:
        price_format = '$1.99'
        price = input('Please enter the price in the following format {}: '.format(price_format))
        if re.fullmatch('\$\d+.\d\d', price):
            break
        else:
            print('Input does not match the requested format.\n')
            continue
    return price
