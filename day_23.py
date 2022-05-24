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

qry1 = "SELECT name, age FROM customers WHERE name in ('Dileep', 'Sajana', 'Trinay') ORDER BY 2"

mycursor.execute(qry1)
# mydb.commit()

myresult1 = mycursor.fetchall()

for x in myresult1:
    print(x)



# DELETE statement

qry2 = "DELETE FROM customers WHERE age = 30"

mycursor.execute(qry2)
# mydb.commit()

myresult2 = mycursor.fetchall()

for x in myresult2:
    print(x)