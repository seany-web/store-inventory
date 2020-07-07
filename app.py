from peewee import *

db = SqliteDatabase('products.db')

class Product(Model):
    product_id = AutoField()
    product_quantity = IntegerField(default=0)
    product_price = IntegerField()
    date_updated = DateTimeField()

    class Meta:
        database = db

def add_csv_data():
    """Gets CSV data and cleans it before inserting it into the database"""
    pass

if __name__ == '__main__':
    db.connect()
    db.create_tables([Product], safe=True)
    # read csv data into table