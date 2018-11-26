import mysql.connector


class INSERTS:
    def __init__(self, user, password):
        self.conn = mysql.connector.connect(host='localhost',
                                            database='dmd',
                                            user=user,
                                            password=password)
        self.cursor = self.conn.cursor(buffered=True)

    def add_provider(self, zip_code, name, phone_number):
        try:
            self.cursor.execute("INSERT INTO provider(pid,zipcode,name,phoneNumber) VALUES "
                                "(null,'" + str(zip_code) + "','" + str(name) + "','" + str(phone_number) + "')")
            self.conn.commit()
            self.cursor.execute("INSERT INTO location(zipcode,Street, Building, City, gps) VALUES "
                                "(" + str(zip_code) + ",null,null,null,null)")
            self.conn.commit()
        except mysql.connector.errors.IntegrityError as inEr:
            if (inEr.errno == 1062):
                print("duplicate data: pid-zipcode")

    def add_provider_parts(self, pid, part, available, cost):
        try:
            self.cursor.execute("INSERT INTO providerparts(pid,part,Available,Cost) VALUES"
                                "('" + str(pid) + "','" + str(part) + "','" + str(available) + "','" + str(cost) + "')")
            self.conn.commit()
        except mysql.connector.errors.IntegrityError as inEr:
            print("error: provider with this id is not found")

    def add_location(self, zipcode, street, building, city, gps):
        # if found - updates,otherwise - nothing
        self.cursor.execute("UPDATE location "
                            "SET Street= '" + str(street) + "', Building=" + str(building) +
                            ", City='" + str(city) + "', gps='" + str(gps) + "' "
                                                                             "WHERE zipcode=" + str(zipcode) + "")
        if (self.cursor.rowcount == 0):
            print("no location with such zipcode")
        self.conn.commit()

    def add_car(self, cid, location, type, charge_level, plug, color):
        try:
            self.cursor.execute("INSERT INTO car(CID, Location, Type, ChargeLevel, Plug, Color) VALUES"
                                "('" + str(cid) + "','" + str(location) + "','" + str(type) +
                                "','" + str(charge_level) + "','" + str(plug) + "','" + str(color) + "')")
            self.conn.commit()
        except mysql.connector.errors.IntegrityError as inEr:
            if (inEr.errno == 1062):
                print("duplicate cid")

    def show(self,table_name):
        print(str(table_name)+" table:")
        self.cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS "
                                "WHERE table_name='"+str(table_name)+"'")
        row = self.cursor.fetchall()
        print(row)
        self.cursor.execute("SELECT * FROM "+str(table_name))
        row = self.cursor.fetchall()
        for x in row:
            print(x)
    def add_car_parts(self, cid, type, is_broken):
        try:
            self.cursor.execute("INSERT INTO carparts(CID, Type, IsBroken) VALUES"
                                "('" + str(cid) + "','" + str(type) + "','" + str(is_broken) + "')")
            self.conn.commit()
        except mysql.connector.errors.IntegrityError as inEr:
            if inEr.errno == 1062:
                print("error: car part of this car is already in database")
            elif inEr.errno == 1452:
                print("no car with given cid is found")

    def add_ride(self, username, cid, is_to_customer, begin_time, end_time, date, origin_point, destination_point,
                 distance, cost):
        try:
            self.cursor.execute("INSERT INTO "
                                "ride(username, CID, IsToCustomer, BeginTime, EndTime, Date, OriginPoint, DestinationPoint, Distance, Cost) VALUES "
                                "('" + str(username) + "','" + str(cid) + "','" + str(is_to_customer) +
                                "','" + str(begin_time) + "','" + str(end_time) + "','" + str(date) + "','" +
                                str(origin_point) + "','" + str(destination_point) + "','" + str(
                distance) + "','" + str(cost) + "')")
            self.conn.commit()
            self.add_payment(date, cost, username, begin_time, begin_time)
        except mysql.connector.errors.IntegrityError as inEr:
            if inEr.errno == 1062:
                print("ride is in database")
            elif inEr.errno == 1452:
                print("username/CID/BeginTime/Date is wrong")

    def add_customer(self, username, name, email, phone_number, credit_card, zipcode):
        try:
            self.cursor.execute("INSERT INTO customer(username, Name, Email, PhoneNumber, CreditCard, zipcode) VALUES"
                                "('" + str(username) + "','" + str(name) + "','" + str(email) +
                                "','" + str(phone_number) + "','" + str(credit_card)
                                + "','" + str(zipcode) + "')")
            self.conn.commit()
        except mysql.connector.errors.IntegrityError as inEr:
            if inEr.errno == 1062:
                print("customer is already in database")

    def add_payment(self, date, cost, username, payment_time, begin_ride_time):
        try:
            self.cursor.execute("INSERT INTO payment(Date, Cost, username, paymenttime, BeginRideTime) VALUES"
                                "('" + str(date) + "','" + str(cost) + "','" + str(username) +
                                "','" + str(payment_time) + "','" + str(begin_ride_time)
                                + "')")
            self.conn.commit()
        except mysql.connector.errors.IntegrityError as inEr:
            if inEr.errno == 1062:
                print("payment is already in database")
            elif inEr.errno == 1452:
                print("date/username/payment are not found in database")

    def add_charging_station(self, zipcode):
        try:
            self.cursor.execute("INSERT INTO chargingstation(ChID,zipcode) VALUES "
                                "(null,'" + str(zipcode)
                                + "')")
            inserted_id = self.cursor.lastrowid
            self.conn.commit()
            self.cursor.execute("INSERT INTO sockets(ChID, Type, Available, TimeToCharge, Cost) VALUES "
                                "(" + str(inserted_id) + ",'-1',null,null,null)")
            self.conn.commit()
            self.cursor.execute("INSERT INTO socketslog(CID, ChID, Type,Date, Time) VALUES "
                                "('-1','" + str(inserted_id) + "','-1','1111-11-11','00:00:00')")
            self.conn.commit()
        except mysql.connector.errors.IntegrityError as inEr:
            if inEr.errno == 1062:
                print("charging station with given zipcode is already in database")

    def add_sockets(self, chid, type, available, time_to_charge, cost):
        try:
            self.cursor.execute("UPDATE sockets "
                                "SET Type= '" + str(type) + "', Available='" + str(available) +
                                "', TimeToCharge='" + str(time_to_charge) + "', cost='" + str(cost) + "' "
                                                                                                      "WHERE CHid='" + str(
                chid) + "' and Type='" + str(type) + "'")
            if (self.cursor.rowcount == 0):
                self.cursor.execute("INSERT INTO sockets(ChID, Type, Available, TimeToCharge, Cost) VALUES "
                                    "('" + str(chid) + "','" + str(type) + "','" + str(available) +
                                    "','" + str(time_to_charge) + "','" + str(cost)
                                    + "')")
            self.conn.commit()
            self.cursor.execute("UPDATE socketslog "
                                "SET Type= '" + str(type) +
                                "' WHERE ChID='" + str(chid) + "'")
            self.conn.commit()
        except mysql.connector.errors.IntegrityError as inEr:
            if inEr.errno == 1062:
                print("socket with given id and type is already in database")
            if inEr.errno == 1452:
                print("no charging stations with such id for sockets")

    def add_sockets_log(self, CID, CHid, Type, Date, Time):
        self.cursor.execute(" UPDATE socketslog"
                            " SET CID= '" + str(CID) + "', Date='" + str(Date) + "', Time='" + str(Time) +
                            "' WHERE ChID='" + str(CHid) + "' and Type='" + str(Type) + "'")
        self.conn.commit()
        if (self.cursor.rowcount == 0):
            print("logs are already in database")

    def add_workshop(self, zipcode):
        try:
            self.cursor.execute("INSERT INTO workshop(WID,zipcode) VALUES "
                                "(null,'" + str(zipcode)
                                + "')")
            inserted_id = self.cursor.lastrowid
            self.conn.commit()
            self.cursor.execute("INSERT INTO wparts(WID, Part, Available, Cost) VALUES "
                                "(" + str(inserted_id) + ",'-1',null,null)")
            self.conn.commit()
            self.cursor.execute("INSERT INTO wshoplog(WID, CID, Part, Date, Cost) VALUES "
                                "(" + str(inserted_id) + ",'-1',-1,'1111-11-11','0')")
            self.conn.commit()
        except mysql.connector.errors.IntegrityError as inEr:
            if inEr.errno == 1062:
                print("workshop with given id is already in database")

    def add_work_parts(self, WID, Part, Available, Cost):
        try:
            self.cursor.execute("UPDATE wparts "
                                " SET Part= '" + str(Part) + "',Available= '" + str(Available) + "',"
                                                                                                 "Cost ='" + str(
                Cost) + "' WHERE WID='" + str(WID) + "' and Part='" + str(Part) + "'")
            if (self.cursor.rowcount == 0):
                self.cursor.execute("INSERT INTO wparts(WID, Part, Available, Cost) VALUES "
                                    "('" + str(WID) + "','" + str(Part) + "','" + str(Available) +
                                    "','" + str(Cost)
                                    + "')")
            self.conn.commit()
            self.cursor.execute("UPDATE wshoplog "
                                " SET Part='" + str(Part) +
                                "',Cost ='" + str(Cost) + "' WHERE WID='" + str(WID) + "'")
            self.conn.commit()
        except mysql.connector.errors.IntegrityError as inEr:
            if inEr.errno == 1062:
                print("work parts are already in database")
            elif inEr.errno == 1452:
                print("no working parts for such id")

    def add_workshop_log(self, WID, CID, Part, Date, Cost):
        self.cursor.execute(" UPDATE wshoplog"
                            " SET CID= '" + str(CID) + "', Date='" + str(Date) + "', Cost='" + str(Cost) +
                            "' WHERE WID='" + str(WID) + "' and Part='" + str(Part) + "'")
        if (self.cursor.rowcount == 0):
            print("logs are already in database")
        self.conn.commit()
