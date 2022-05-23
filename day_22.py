# MySQL using Python

import mysql.connector

mydb = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                password="password"
                              )
                              

# Creating a new database
mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE sample_db")


# View Available Databases
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)


# Connecting to the database while making the MySQL connection
# mydb = mysql.connector.connect(
#                                 host="localhost",
#                                 user="root",
#                                 password="password",
#                                 database='sample_db'
#                               )



