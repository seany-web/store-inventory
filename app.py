from peewee import *

import csvhandler
import menu

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


if __name__ == '__main__':
    db.connect()
    db.create_tables([Product], safe=True)
    add_csv_data()
    menu.menu_loop()