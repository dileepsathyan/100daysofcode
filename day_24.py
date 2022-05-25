import mysql.connector

mydb1 = mysql.connector.connect(
                            host='localhost',
                            username='root',
                            password='password'
                            )

qry1 = "SHOW DATABASES"
# with mydb1.cursor() as cursor:
#     cursor.execute(qry1)
#     for db in cursor:
#         print(db)``


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
# with mydb2.cursor() as cursor:
#     cursor.execute(qry3)
#     result2 = cursor.fetchall()
#     for field in result2:
#         print(field)


qry4 = """
        SELECT CONCAT(c.name, ' ', c.age, ' ', r.relationship)
        FROM customers c
        JOIN relation r
        ON c.age = r.age
        """
# with mydb2.cursor() as cursor:
#     cursor.execute(qry4)
#     for x in cursor:
#         print(x)


# Difference between execute() and executemany()

# .execute(): is used when we the values are small and can be written in the same SQL query.
# Note: I am not using .commit() so that these changes are temporary and wont be reflected in the db.
qry5 = """
        INSERT INTO relation
        VALUES  (65, 'Grand Father'),
                (58, 'Grand Mother'),
                (45, 'Uncle')
        """
# with mydb2.cursor() as cursor:
#     cursor.execute(qry5)

#     cursor.execute("SELECT * FROM relation")
#     result5 = cursor.fetchall()
#     for x in result5:
#         print(x)



# .executemany(): is used when the list is huge and cant be put together in 1 query.

qry6 = """
        INSERT INTO relation 
        (age, relationship)
        VALUES  (%s, %s)
        """

vals = [(65, 'Grand Father'),
        (58, 'Grand Mother'),
        (45, 'Uncle'),
        (40, 'Aunt'),
        (15, 'Brother'),
        (18, 'Sister'),
        (21, 'Cousin Brother'),
        (19, 'Cousing Sister')]

with mydb2.cursor() as cursor:
    cursor.executemany(qry6, vals)

    cursor.execute("SELECT * FROM relation")
    result6 = cursor.fetchall()
    for x in result6:
        print(x)