import mysql.connector

mydb = mysql.connector.connect(
                            host='localhost',
                            username='root',
                            password='password'
                            )

qry1 = "SHOW DATABASES"
with mydb.cursor() as cursor:
    cursor.execute(qry1)
    for db in cursor:
        print(db)