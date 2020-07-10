import csvhandler
import dbhandler
import menu


if __name__ == '__main__':
    dbhandler.db.connect()
    dbhandler.db.create_tables([dbhandler.Product], safe=True)
    csvhandler.read_csv()
    menu.menu_loop()
