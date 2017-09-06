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
            return 1
        else:
            return 0

        conn.close()


