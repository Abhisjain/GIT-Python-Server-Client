import mysql.connector as mysql

class matchcredentials(object):
    def matchingcredentials(self,userin,passin):
        username=userin   # username passed from the entry window in login.py
        password=passin   # password passed from the password window in password.py
        conn = mysql.connect(user='root', password='Canada', host='127.0.0.1')
        cursor = conn.cursor(buffered=True)
        cursor.execute("use login")
        cursor.execute("SELECT * FROM credentials")

        x = "select password from credentials where username= '%s'" % (username)
        cursor.execute(x)
        x=cursor.fetchall()
        for i in x:     # done because cursor.fetchall return a list with string inside it
            x = i[0]
        if x == password:
            self.onlineusers(username, password)
            return 1
        else:
            return 0
        conn.close()


    def onlineusers(self,username,password):
        conn1 = mysql.connect(user='root', password='Canada', host='127.0.0.1')
        cursor = conn1.cursor(buffered=True)
        cursor.execute("use login")
        x= "INSERT INTO onlineusers (Username, Password) values ('%s', '%s')" % (username,password)
        cursor.execute(x)
        conn1.commit()
        conn1.close()
        self.getonlineusers()
        return


    def getonlineusers(self):
        conn2 = mysql.connect(user='root', password='Canada', host='127.0.0.1')
        cursor = conn2.cursor(buffered=True)
        cursor.execute("use login")
        cursor.execute("select username from onlineusers")
        x=cursor.fetchall()
        print(len(x))
        conn2.close()
# Function to delete users who went offline
    def deleteofflineusers(self,usernamein):
        deleteofflineuser=usernamein
        print(deleteofflineuser)
        conn3 = mysql.connect(user='root', password='Canada', host='127.0.0.1')
        cursor = conn3.cursor(buffered=True)
        cursor.execute("use login")
        print(cursor)
        print(deleteofflineuser)
        x = "Delete from onlineusers where Username = '%s'" % deleteofflineuser
        cursor.execute(x)
        conn3.commit()
        conn3.close()
        return
