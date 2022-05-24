import mysql.connector

mydb = mysql.connector.connect(
                            host='localhost',
                            user= 'root',
                            password='password',
                            database='sample_db'
                            )

mycursor = mydb.cursor()


# SELECT statment
mycursor.execute("SELECT * FROM CUSTOMERS")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)





