# MySQL using Python

import mysql.connector

mydb = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                password="password"
                              )
                              

# Creating a new database
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE sample_db")


# View Available Databases
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)


# Connecting to the database while making the MySQL connection
mydb = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                password="password",
                                database='sample_db'
                              )



# Creating a new table
mydb = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                password="password",
                                database='sample_db'
                              )
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), age TINYINT(255))")



# # View tables in a database
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)



# Inserting a record to the table

sql = "INSERT INTO customers (name, age) VALUES (%s, %s)"
val = ("Dileep", 31)

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")




# Inserting multiple records at once.

sql = "INSERT INTO customers (name, age) VALUES (%s, %s)"
val = [("Dileep", 31), ("Sajana", 29), ("Trinay", 3)]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "records were inserted.")
