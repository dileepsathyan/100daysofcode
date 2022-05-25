import mysql.connector

mydb1 = mysql.connector.connect(
                            host='localhost',
                            username='root',
                            password='password'
                            )

# qry1 = "SHOW DATABASES"

# with mydb1.cursor() as cursor:
#     cursor.execute(qry1)
#     for db in cursor:
#         print(db)


# Connecting to an existing database
mydb2 = mysql.connector.connect(
                            host='localhost',
                            username='root',
                            password='password',
                            database='sample_db'
                        )
qry2 = "SHOW TABLES"

# with mydb2.cursor() as cursor:
#     cursor.execute(qry2)
#     for tbl_name in cursor:
#         print(tbl_name)


# Describing a table
qry3 = "DESCRIBE relation"

with mydb2.cursor() as cursor:
    cursor.execute(qry3)
    result2 = cursor.fetchall()
    for field in result2:
        print(field)