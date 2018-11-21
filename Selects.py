import decimal

import mysql.connector
import datetime


class SELECT:
    def __init__(self, user, password):
        self.conn = mysql.connector.connect(host='localhost',
                                            database='dmd',
                                            user=user,
                                            password=password)
        self.cursor = self.conn.cursor(buffered=True)

    def select1(self, name):
        # search for current date
        date = datetime.date.today()
        self.cursor.execute("SELECT c.* FROM ride r INNER JOIN  car c using(CID) "
                            "WHERE c.Color='red'"
                            "AND r.username= '" + str(name) + "'"
                                                              "AND CID LIKE 'AN%'"
                                                              "AND c.type='car'"
                                                              "AND r.Date= '" + str(date) + "'")
        row = self.cursor.fetchall()
        information=["CID","Location","Type","Charge level","Plug","Color"]
        i=1
        for x in row:
            print("Transport: "+str(i))
            cur=""
            i=i+1
            for i in range(0,len(information)):
                cur+=str(information[i]+": ")+str(x[i])+"\n"
            print(cur)
    def select2(self, date):
        # TODO: обсудить,я не уверен,что правильно работает
        for i in range(24):
            self.cursor.execute("SELECT COUNT(*)"
                                 "FROM socketslog log INNER JOIN sockets sock using(ChID)"
                                 "WHERE (log.Time >='"+str(i)+":00:00'"
                                     " AND log.Time <='"+str(i)+":59:59')"
                                  "or (TIME_FORMAT(log.Time+ INTERVAL sock.TimeToCharge MINUTE,"
                                    "'%H:%i:%s')"
                                ">'"+str(i)+":00:00' and "
                                "log.Time<'"+str(i)+":59:59')"
                                "and log.Date='"+str(date)+"'")
            row = self.cursor.fetchall()
            for x in row:
                print(str(i)+"h-"+str(i+1)+"h:",x[0])
        print()
    def select3(self,date):
        comm= self.conn.cmd_query_iter("SET @ar=(SELECT COUNT(*)"
                            "FROM ride"
                            " WHERE Date >= '" + str(date)+ "' AND "
                            "Date <= '" + str(date) + "'+ INTERVAL 1 WEEK);"
                                                      
                            "SET @mr=(SELECT COUNT(*)"
                            "FROM ride"
                            " WHERE Date >= '"+str(date)+"' AND "
                            "Date <= '"+str(date)+"'+ INTERVAL 1 WEEK"
                            " AND TIME_FORMAT(BeginTime,'%H:%i:%s')>= '07:00:00'"
                            " AND TIME_FORMAT(BeginTime,'%H:%i:%s')<='10:00:00');"
                                                  
                            "SET @dr=(SELECT COUNT(*)"
                            "FROM ride"
                            " WHERE Date >= '"+str(date)+"' AND "
                            "Date <= '"+str(date)+"'+ INTERVAL 1 WEEK"
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
        time=["Morning","Afternoon","Evening"]
        for result in comm:
            try:
                if 'columns' in result:
                    rows = self.conn.get_rows()[0][0]
                    for j,i in zip(rows,range(0,len(time))):
                        cur=time[i]+": "+j.decode('utf-8')+"%"
                        print(cur)
            except AttributeError:
                print("No taxis for given date")
        print()
    def select4(self,username):
        date=datetime.date.today()
        month = datetime.date.today().month
        self.cursor.execute("SELECT CID,DATE FROM ride"
                            " WHERE username = '"+username+"'"
                            " AND (Date>='"+str(date)+"'- INTERVAL 1 MONTH "
                                                      "and MONTH(Date)="+str(month)+")"
                            " AND DATE<='"+str(date)+"'")
        row = self.cursor.fetchall()
        for x in row:
            print("Model: "+x[0],",Date: "+str(x[1]))
        print()
    def select5(self,date):
        self.cursor.execute("SELECT "
                            "AVG(Distance),"
                            "TIME_FORMAT(AVG(EndTime-BeginTime),'%H:%i:%s'),"
                            "username "
                            " FROM ride "
                            " WHERE Date='"+str(date)+"'"
                            " AND IsToCustomer='1'"
                            "GROUP BY username;")
        row = self.cursor.fetchall()
        for x in row:
                print(decimal.Decimal(x[0]),x[1],"to "+x[2])
        print()
if __name__ == '__main__':
    #временно тут стоит main
    selects = SELECT("root", "170199Dima")
    username='test111'
    selects.select1(username)

    #сделать инпут для второго
    date = datetime.date(2020, 1, 15)
    selects.select2(date)
    selects.select3(date)

    #TODO: в поле ride добавить цену
    selects.select4(username)
    selects.select5(date)