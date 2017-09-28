import mysql.connector as mysql
conn=mysql.connect(user='root', password='Canada', host='54.152.237.120', port=3306, database='mysql')


cursor=conn.cursor(buffered=True)
cursor.execute("use mysql")
print(conn)