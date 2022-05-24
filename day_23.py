import mysql.connector

mydb = mysql.connector.connect(
                            host='localhost',
                            user= 'root',
                            password='password',
                            database='sample_db'
                            )

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM CUSTOMERS")

for x in mycursor:
    print(x)