from peewee import *
import datetime

import csvhandler
import menu

db = SqliteDatabase('inventory.db')


class Product(Model):
    product_id = AutoField(primary_key=True)
    product_name = CharField(unique=True)
    product_price = IntegerField()
    product_quantity = IntegerField(default=0)
    date_updated = DateField()

    class Meta:
        database = db


def add_product(name, price, quantity, last_updated):
    """Adds a new product to the database"""
    try:
        Product.create(
            product_name=name,
            product_price=price,
            product_quantity=quantity,
            date_updated=last_updated
        )
    except IntegrityError:
        product_record = Product.get(Product.product_name == name)
        last_updated_date_obj = datetime.datetime.strptime(
            last_updated, '%Y-%m-%d'
        ).date()
        if last_updated_date_obj >= product_record.date_updated:
            product_record.product_price = price
            product_record.product_quantity = quantity
            product_record.date_updated = last_updated
            product_record.save()


def backup_database():
    """Gets all products from database and
    converts fields to strings for CSV writing"""
    all_records = Product.select()
    records_backup = []
    for record in all_records:
        product = {
            'name': record.product_name,
            'price': str(record.product_price),
            'quantity': str(record.product_quantity),
            'date_updated': datetime.datetime.strftime(
                record.date_updated, '%Y-%m-%d'
            )}
        records_backup.append(product)
    csvhandler.write_csv(records_backup)


def search_products(search_query):
    """Searches for a product by the product's ID field"""
    try:
        product = Product.get(Product.product_id == search_query)
        menu.display_product(product)
    except DoesNotExist:
        print("Product ID# '{}' does not exist in the database".format(
            search_query
        ))
        menu.return_to_menu()
