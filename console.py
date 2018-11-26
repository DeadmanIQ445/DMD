import mysql.connector
from mysql.connector import ProgrammingError, InterfaceError
import Selects
import datetime
import INSERTS


def main(username, password):
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='',
                                       user=username,
                                       password=password)
        if (conn.is_connected()):
            dump("Dump20181126.sql", conn)
            print("to quit: enter -1\n"
                  "to show all information: enter 0\n"
                  "to insert data: enter 1\n"
                  "to run selects: enter 2")
            work_with_db(str(input()), username, password)
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


def choose_insert(username, password):
    try:
        inserts = INSERTS.INSERTS(username, password)
        print("to finish inserting: enter -1\n"
              "to insert car: enter 1\n"
              "to insert car parts: enter 2\n"
              "to insert ride: enter 3\n"
              "to insert customer: enter 4\n"
              "to insert payment: enter 5\n"
              "to insert provider: enter 6\n"
              "to insert provider parts: enter 7\n"
              "to insert provider location: enter 8\n"
              "to insert charging station: enter 9\n"
              "to insert sockets: enter 10\n"
              "to insert socket logs: enter 11\n"
              "to insert workshop: enter 12\n"
              "to insert work parts: enter 13\n"
              "to insert workshop logs: enter 14")
        insert = str(input())
        if (int(insert) == 1):
            inserts.show("car")
            print("Enter CID,Location,Type,integer ChargeLevel,Plug and Color")
            inserts.add_car(str(input()), str(input()), str(input()),
                            int(input()), str(input()), str(input()))
            inserts.show("car")
            choose_insert(username, password)
        elif (int(insert) == 2):
            inserts.show("carparts")
            print("Enter CID,Type,isBroken or not(0 or 1)")
            inserts.add_car_parts(str(input()), str(input()), str(input()))
            inserts.show("carparts")
            choose_insert(username, password)
        elif (int(insert) == 3):
            inserts.show("ride")
            print("Enter username,isToCustomer(0 or 1),begin time,end time,date,origin point,"
                  "destination point,distance,cost")
            inserts.add_ride(str(input()), str(input()), str(input()), str(input()),
                             str(input()), str(input()), str(input()), str(input()), str(input()), str(input()))
            inserts.show("ride")
            choose_insert(username, password)
        elif (int(insert) == 4):
            inserts.show("customer")
            print("Enter username,name,email,phone number,credit card,zipcode")
            inserts.add_customer(str(input()), str(input()), str(input()), str(input()),
                                 str(input()), str(input()))
            inserts.show("customer")
            choose_insert(username, password)
        elif (int(insert) == 5):
            inserts.show("payment")
            print("Enter Date,cost,username,payment time,begin ride time")
            inserts.add_payment(str(input()), str(input()), str(input()), str(input()),
                                str(input()))
            inserts.show("payment")
            choose_insert(username, password)
        elif (int(insert) == 6):
            inserts.show("provider")
            print("Enter zipcode,name,phone number")
            inserts.add_provider(str(input()), str(input()), str(input()))
            inserts.show("provider")
            choose_insert(username, password)
        elif (int(insert) == 7):
            inserts.show("providerparts")
            print("Enter pid, part, available, cost")
            inserts.add_provider_parts(str(input()), str(input()), str(input()), str(input()))
            inserts.show("providerparts")
            choose_insert(username, password)
        elif (int(insert) == 8):
            inserts.show("location")
            print("Enter zipcode, street, building, city, gps")
            inserts.add_location(str(input()), str(input()), str(input()), str(input()), str(input()))
            inserts.show("location")
            choose_insert(username, password)
        elif (int(insert) == 9):
            inserts.show("chargingstation")
            print("Enter zipcode")
            inserts.add_charging_station(str(input()))
            inserts.show("chargingstation")
            choose_insert(username, password)
        elif (int(insert) == 10):
            inserts.show("sockets")
            print("Enter chid, type, available, time_to_charge, cost")
            inserts.add_sockets(str(input()), str(input()), str(input()), str(input()), str(input()))
            inserts.show("sockets")
            choose_insert(username, password)
        elif (int(insert) == 11):
            inserts.show("socketslog")
            print("Enter CID, CHid, Type, Date, Time")
            inserts.add_sockets_log(str(input()), str(input()), str(input()), str(input()), str(input()))
            inserts.show("socketslog")
            choose_insert(username, password)
        elif (int(insert) == 12):
            inserts.show("workshop")
            print("Enter zipcode")
            inserts.add_workshop(str(input()))
            inserts.show("workshop")
            choose_insert(username, password)
        elif (int(insert) == 13):
            inserts.show("wparts")
            print("Enter WID, Part, Available, Cost")
            inserts.add_work_parts(str(input()), str(input()), str(input()), str(input()))
            inserts.show("wparts")
            choose_insert(username, password)
        elif (int(insert) == 14):
            inserts.show("wshoplog")
            print("Enter WID, CID, Part, Date, Cost")
            inserts.add_workshop_log(str(input()), str(input()), str(input()), str(input()), str(input()))
            inserts.show("wshoplog")
            choose_insert(username, password)
        elif (int(insert) == -1):
            print("to quit: enter -1\n"
                  "to show all information: enter 0\n"
                  "to insert data: enter 1\n"
                  "to run selects: enter 2")
            work_with_db(str(input()), username, password)
        else:
            print("wrong input,try again")
            choose_insert(username, password)
    except mysql.connector.errors.DataError as inEr:
        print("wrong input data")
        choose_insert(username, password)


def work_with_db(num, username, password):
    selects = Selects.SELECT(username, password)
    if (int(num) == 0):
        selects.show_all_tables()
        print("to quit: enter -1\n"
              "to show all information: enter 0\n"
              "to insert data: enter 1\n"
              "to run selects: enter 2")
        work_with_db(str(input()), username, password)
    elif (int(num) == 1):
        choose_insert(username, password)
        print("to quit: enter -1\n"
              "to show all information: enter 0\n"
              "to insert data: enter 1\n"
              "to run selects: enter 2")
        work_with_db(str(input()), username, password)
    elif (int(num) == 2):
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
        date = datetime.date(2018, 9, 10)
        selects.select8(date)
        selects.select9()
        selects.select10()
        print("to quit: enter -1\n"
              "to show all information: enter 0\n"
              "to insert data: enter 1\n"
              "to run selects: enter 2")
        work_with_db(str(input()), username, password)
    elif (int(num) == -1):
        quit()
    else:
        print("wrong input,try again")
        work_with_db(str(input()), username, password)


