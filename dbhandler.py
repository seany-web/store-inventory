from peewee import *

import csvhandler

db = SqliteDatabase('products.db')

class Product(Model):
    product_id = AutoField(primary_key=True)
    product_name = CharField()
    product_price = IntegerField()
    product_quantity = IntegerField(default=0)
    date_updated = DateField()

    class Meta:
        database = db

def add_csv_data():
    """Gets CSV data and cleans it before inserting it into the database"""
    raw_data = csvhandler.read_csv()
    for line in raw_data:
        Product.create(product_name=line['name'], product_price=line['price'],
        product_quantity=line['quantity'], date_updated=line['date_updated'])

def view_products(search_query=None):
    """Gets all products from the database"""
    products = Product.select()
    if search_query:
        try:
            product = Product.get(Product.product_id == search_query)
            return product
        except DoesNotExist:
            return None
    return products

def search_products():
    """Search products for by ID"""
    return view_products(input('Please enter an ID number: '))