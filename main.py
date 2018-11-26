import mysql.connector
from mysql.connector import ProgrammingError, InterfaceError
import Selects
import datetime
import time
import INSERTS
def main(username, password):
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='',
                                       user=username,
                                       password=password)
        if (conn.is_connected()):
            dump("Dump20181126.sql", conn)
            time.sleep(5)
            selects = Selects.SELECT(username, password)
            name = 'test111'
            date = datetime.date(2020, 1, 15)
            # TODO: в поле ride добавить цену
            selects.select1(name)
            selects.select2(date)
            selects.select3(date)
            selects.select4(name)
            selects.select5(date)
            selects.select6()
            selects.select7()
            date=datetime.date(2018,9,10)
            selects.select8(date)
            selects.select9()
            selects.select10()
    except ProgrammingError:
        print("Something is wrong\nRe-enter user name")
        name = str(input())
        print("Enter password")
        passw = str(input())
        main(name, passw)
    except InterfaceError:
        pass


def dump(filename, connection):
    try:
        file = open(filename, 'r')
        sql = ' '.join(file.readlines())
        cursor = connection.cursor(buffered=True)
        cursor.execute(sql)
        connection.commit()
    except InterfaceError:
        pass


if __name__ == '__main__':
    print("Enter user name")
    username = str(input())
    print("Enter password")
    password = str(input())
    main(username, password)
