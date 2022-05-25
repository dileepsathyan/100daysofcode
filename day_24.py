import mysql.connector

mydb = mysql.connector.connect(
                            host='localhost',
                            username='root',
                            password='password',
                            database='sample_db'
                            )

mycursor = mydb.cursor()

