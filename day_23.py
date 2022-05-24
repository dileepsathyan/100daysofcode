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
myresult1 = mycursor.fetchall()

for x in myresult1:
    print(x)


# Customised SELECT statment
mycursor.execute("SELECT age FROM CUSTOMERS WHERE name = 'Trinay'")
myresult2 = mycursor.fetchall()

for x in myresult2:
    print(x)


# Executing a long sql query using Python

qry1 = "SELECT name, age FROM customers WHERE name in ('Dileep', 'Sajana', 'Trinay') ORDER BY 2"

mycursor.execute(qry1)

myresult3 = mycursor.fetchall()

for x in myresult3:
    print(x)



# DELETE statement

qry2 = "DELETE FROM customers WHERE age = 30"

mycursor.execute(qry2)
myresult4 = mycursor.fetchall()

for i in myresult4:
    print(i)