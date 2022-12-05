import mysql.connector as c
con = c.connect(host='localhost',
                user='root',
                passwd='ankit' )

cursor = con.cursor()

if con.is_connected():
    print("Conneted Successfully")
