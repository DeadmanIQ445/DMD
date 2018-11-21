import mysql.connector
from mysql.connector import ProgrammingError, InterfaceError


def main(username, password):
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='',
                                       user=username,
                                       password=password)
        if (conn.is_connected()):
            dump("Dump20181119.sql", conn)
    except ProgrammingError:
        print("Something is wrong\nRe-enter user name")
        name = str(input())
        print("Enter password")
        passw = str(input())
        main(name, passw)
    except InterfaceError:
        pass


def dump(filename, connection):
    file = open(filename, 'r')
    sql = ' '.join(file.readlines())
    cursor = connection.cursor(buffered=True)
    cursor.execute(sql)
    connection.commit()
    connection.cursor().close()
    connection.close()


if __name__ == '__main__':
    print("Enter user name")
    username = str(input())
    print("Enter password")
    password = str(input())
    main(username, password)
