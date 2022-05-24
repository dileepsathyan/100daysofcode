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


# Customised SELECT statment
mycursor.execute("SELECT age FROM CUSTOMERS WHERE name = 'Trinay'")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)


# Executing a long sql query using Python

qry = "SELECT name, age FROM customers WHERE name in ('Dileep', 'Sajana', 'Trinay') ORDER BY 2"

mycursor.execute(qry)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)