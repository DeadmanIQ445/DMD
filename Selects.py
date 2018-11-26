import decimal

import mysql.connector
from datetime import datetime

class SELECT:
    def __init__(self, user, password):
        self.conn = mysql.connector.connect(host='localhost',
                                            database='dmd',
                                            user=user,
                                            password=password)
        self.cursor = self.conn.cursor(buffered=True)

    def select1(self, name):
        print("START SELECT 1")
        # search for current date
        date = datetime.today()
        self.cursor.execute("SELECT c.* FROM ride r INNER JOIN  car c using(CID) "
                            "WHERE c.Color='red'"
                            "AND r.username= '" + str(name) + "'"
                                                              "AND CID LIKE 'AN%'"
                                                              "AND c.type='car'"
                                                              "AND r.Date= '" + str(date) + "'")
        row = self.cursor.fetchall()
        information = ["CID", "Location", "Type", "Charge level", "Plug", "Color"]
        i = 1
        for x in row:
            print("Transport: " + str(i))
            cur = ""
            i = i + 1
            for i in range(0, len(information)):
                cur += str(information[i] + ": ") + str(x[i]) + "\n"
            print(cur)

    def select2(self, date):
        print("START SELECT 2")
        for i in range(24):
            self.cursor.execute("SELECT COUNT(*)"
                                "FROM socketslog log INNER JOIN sockets sock using(ChID)"
                                "WHERE (log.Time >='" + str(i) + ":00:00'"
                                " AND log.Time <='" + str(i) + ":59:59')"
                                "or (TIME_FORMAT(log.Time+ INTERVAL sock.TimeToCharge MINUTE,"
                                "'%H:%i:%s')"
                                ">'" + str(i) + ":00:00' and "
                                "log.Time<'" + str(i) + ":59:59')"
                                "and log.Date='" + str(date) + "'")
            row = self.cursor.fetchall()
            for x in row:
                print(str(i) + "h-" + str(i + 1) + "h:", x[0])
        print()

    def select3(self, date):
        print("START SELECT 3")
        comm = self.conn.cmd_query_iter("SET @ar=(SELECT COUNT(*) "
                                        " FROM ride"
                                        " WHERE Date >= '" + str(date) + "' AND "
                                        " Date <= '" + str(date) + "'+ INTERVAL 1 WEEK);"
                                        "SET @mr=(SELECT COUNT(*)"
                                        "FROM ride"
                                        " WHERE Date >= '" + str(date) + "' AND "
                                        "Date <= '" + str(date) + "'+ INTERVAL 1 WEEK"
                                        " AND TIME_FORMAT(BeginTime,'%H:%i:%s')>= '07:00:00'"
                                        " AND TIME_FORMAT(BeginTime,'%H:%i:%s')<='10:00:00');"
                                        "SET @dr=(SELECT COUNT(*)"
                                        "FROM ride"
                                        " WHERE Date >= '" + str(date) + "' AND "
                                        "Date <= '" + str(date) + "'+ INTERVAL 1 WEEK"
                                        " AND TIME_FORMAT(BeginTime,'%H:%i:%s')<= '14:00:00'"
                                        " AND TIME_FORMAT(EndTime,'%H:%i:%s')>='12:00:00');"
                                        "SET @er=(SELECT COUNT(*)"
                                        "FROM ride"
                                        " WHERE Date >= '" + str(date) + "' AND "
                                        "Date <= '" + str(date) + "'+ INTERVAL 1 WEEK"
                                        " AND TIME_FORMAT(BeginTime,'%H:%i:%s')<= '19:00:00'"
                                        " AND TIME_FORMAT(EndTime,'%H:%i:%s')>='17:00:00');"
                                        "SELECT (@mr/@ar)*100,(@dr/@ar)*100,(@er/@ar)*100"
                                        )
        time = ["Morning", "Afternoon", "Evening"]
        for result in comm:
            try:
                if 'columns' in result:
                    rows = self.conn.get_rows()[0][0]
                    for j, i in zip(rows, range(0, len(time))):
                        cur = time[i] + ": " + j.decode('utf-8') + "%"
                        print(cur)
            except AttributeError:
                print("No taxis for given date")
        print()

    def select4(self, username):
        print("START SELECT 4")
        date = datetime.today()
        month = datetime.today().month
        self.cursor.execute("SELECT CID,DATE FROM ride"
                            " WHERE username = '" + username + "'"
                            " AND (Date>='" + str(date) + "'- INTERVAL 1 MONTH "
                            "and MONTH(Date)=" + str(month) + ")"
                            " AND DATE<='" + str(date) + "'")
        row = self.cursor.fetchall()
        for x in row:
            print("Model: " + x[0], ",Date: " + str(x[1]))
        print()

    def select5(self, date):
        print("START SELECT 5")
        self.cursor.execute("SELECT "
                            "AVG(Distance),"
                            "TIME_FORMAT(AVG(EndTime-BeginTime),'%H:%i:%s'),"
                            "username "
                            " FROM ride "
                            " WHERE Date='" + str(date) + "'"
                            " AND IsToCustomer='1'"
                            "GROUP BY username;")
        row = self.cursor.fetchall()
        for x in row:
            print(decimal.Decimal(x[0]), x[1], "to " + x[2])
        print()

    def select6(self):
        print("START SELECT 6")
        timeslots = [
            ['07:00:00', '10:00:00', 'Morning'],
            ['12:00:00', '14:00:00', 'Afternoon'],
            ['17:00:00', '19:00:00', 'Evening'],
        ]
        for slot in timeslots:
            self.cursor.execute(
                "SELECT OriginPoint, COUNT(*)"
                " FROM ride"
                " WHERE TIME_FORMAT(BeginTime, '%H:%i:%s') >= '" + slot[0] + "'"
                " AND TIME_FORMAT(BeginTime, '%H:%i:%s') < '" +
                slot[1] + "'"
                          " GROUP BY OriginPoint"
                          " ORDER BY COUNT(*) DESC"
                          " LIMIT 3;"
            )
            print(slot[2] + " Pick-up point")
            row = self.cursor.fetchall()
            print(row)
            self.cursor.execute(
                "SELECT DestinationPoint, COUNT(*)"
                " FROM ride"
                " WHERE TIME_FORMAT(BeginTime, '%H:%i:%s') >= '" + slot[0] + "'"
                " AND TIME_FORMAT(BeginTime, '%H:%i:%s') < '" +
                slot[1] + "'"
                          " GROUP BY DestinationPoint"
                          " ORDER BY COUNT(*) DESC"
                          " LIMIT 3;"
            )
            print(slot[2] + " Destination point")
            row = self.cursor.fetchall()
            print(row)

    def select7(self):
        print("START SELECT 7")
        self.cursor.execute(
            "SELECT cid"
            " FROM (SELECT c.cid, COUNT(r.Date)"
            " FROM car c"
            " LEFT OUTER JOIN ride r ON c.CID = r.CID"
            " WHERE DATE_SUB(DATE_FORMAT(r.Date, '%Y-%m-%d'), INTERVAL -3 MONTH) >= '2018-11-23'"
            " OR r.Date IS NULL"
            " GROUP BY c.cid"
            " ORDER BY COUNT(r.Date)) as crc"
        )
        row = self.cursor.fetchall()
        percentage = int(len(row) / 10)
        for x in range(percentage):
            print(row[x])

    def select8(self, date):
        print("START SELECT 8")
        self.cursor.execute(
            "SELECT rtc.username, COUNT(*)"
            " FROM (SELECT DISTINCT username, date, cid"
            " FROM ride"
            " WHERE IsToCustomer = 1 "
            " AND DATE_SUB(DATE_FORMAT(Date, '%Y-%m-%d'), INTERVAL 1 MONTH) <= '" + str(date) + "'"
            " AND DATE_FORMAT(Date, '%Y-%m-%d') > '" + str(date) + "') as rtc, "
            "       (SELECT date, cid"
            "       FROM ride"
            "       WHERE IsToCustomer = 0 AND DATE_SUB(DATE_FORMAT(Date, '%Y-%m-%d'), INTERVAL 1 MONTH) <= '" + str(date) + "'"
            "       AND DATE_FORMAT(Date, '%Y-%m-%d') > '" + str(date) + "') as rtcs"
            "       WHERE rtc.date = rtcs.date AND rtc.cid = rtcs.cid"
            "       GROUP BY rtc.username"
            "       ORDER BY COUNT(*)"
        )
        print(self.cursor.fetchall())

    def select9(self):
        print("START SELECT 9")
        self.cursor.execute(
            "SELECT wid, part, COUNT(*)"
            " FROM wshoplog"
            " GROUP BY wid, Part"
            " ORDER BY COUNT(*) DESC"
        )
        res = self.cursor.fetchall()
        print(res)

    def select10(self):
        print("START SELECT 10")
        self.cursor.execute(
            "SELECT cid, SUM(cost)"
            " FROM wshoplog"
            " GROUP BY CID"
            " ORDER BY SUM(Cost) DESC"
        )
        repairs = self.cursor.fetchall()
        self.cursor.execute(
            "SELECT cid, sum(cost) as spent"
            " FROM "
            " (SELECT cid, ChID, Type"
            " FROM socketslog) as chlog, "
            " (SELECT chid, type, Cost"
            " FROM sockets) as sckts"
            " WHERE chlog.ChID = sckts.ChID AND chlog.Type = sckts.Type"
            " GROUP BY CID"
            " ORDER BY sum(cost) DESC"
        )
        charges = self.cursor.fetchall()
        self.cursor.execute(
            "SELECT cid FROM car"
        )
        cars = self.cursor.fetchall()
        spent = []
        for car in cars:
            spent_for_car = 0
            for repair in repairs:
                if car[0] == repair[0]:
                    spent_for_car += repair[1]
            for charge in charges:
                if car[0] == charge[0]:
                    spent_for_car += charge[1]
            spent.append(spent_for_car)
        max_i = 0
        max_spent = 0
        print(spent)
        for i in range(len(spent)):
            if int(str(spent[i]).split('.')[0]) > max_spent:
                max_i = i
                max_spent = int(str(spent[i]).split('.')[0])
        print(str(cars[max_i][0] + ": " + str(spent[max_i])))
