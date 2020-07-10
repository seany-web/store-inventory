import dbhandler
import menu


if __name__ == '__main__':
    dbhandler.db.connect()
    dbhandler.db.create_tables([dbhandler.Product], safe=True)
    dbhandler.add_csv_data()
    menu.menu_loop()