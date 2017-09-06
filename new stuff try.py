import mysql.connector as mysql

conn=mysql.connect(user='root', password='Canada', host='127.0.0.1')
cursor=conn.cursor(buffered=True)
cursor.execute("use login")
cursor.execute("SELECT * FROM credentials")

username=input("Enter username:\n")
password=input("Enter Password:\n")
x="select password from credentials where username= '%s'" %(username)
cursor.execute(x)
x=cursor.fetchall()
for i in x:
    x=i[0]
if x==password:
    print("Password matched\n")
else:
    print("password not matched\n")
conn.close()