from peewee import *

db = SqliteDatabase('products.db')

class Product(Model):
    product_id = AutoField()
    product_quantity = IntegerField(default=0)
    product_price = IntegerField()
    date_updated = DateTimeField()

    class Meta:
        database = db
