import mysql.connector

""" Get Started """
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="2133"
# )
# print(mydb)


""" Create Database """
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabase")


" Check if Database exists "
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="2133",
  database="mydatabase"
)
mycursor = mydb.cursor()


""" Create Table """
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

" Check if Table exists "
# mycursor.execute("SHOW TABLES")
# [ print(x) for x in mycursor ]


" Primary Key "
#AUTO_INCREMENT does a ++ per record, and PRIMARY KEY defines that column as Primary
#mycursor.execute("CREATE TABLE customers_with_primarykey (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")


""" #Insert into Table """
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")


" #Insert Multiple Rows "
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "was inserted.")


" Get ID of inserted element "
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("Michelle", "Blue Village")
# mycursor.execute(sql, val)
# mydb.commit()
# print("1 record inserted, ID:", mycursor.lastrowid)


""" Select From a Table """
# mycursor.execute("SELECT * FROM customers")
# myresult = mycursor.fetchall()
# [print(x) for x in myresult]

" Selecting Columns "
# mycursor.execute("SELECT name FROM customers")
# myresult = mycursor.fetchall()
# [print(x) for x in myresult]

" Using fetchone() to fetch one row "
# mycursor.execute("SELECT * FROM customers")
# myresult = mycursor.fetchone()
# print(myresult)

""" Selecting with a Filter: WHERE """
# sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# [print(x) for x in myresult]


" Wildcard Characters "
# sql = "SELECT * FROM customers WHERE address LIKE '%way%'"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# [print(x) for x in myresult]


" Prevent SQL Injection "  # TODO: Read up more
# sql = "SELECT * FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )
# mycursor.execute(sql, adr)
# myresult = mycursor.fetchall()
# [print(x) for x in myresult]


""" Order By """
# sql = "SELECT * FROM customers ORDER BY name"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# [print(x) for x in myresult]

""" Order By Desc"""
# sql = "SELECT * FROM customers ORDER BY name DESC"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# [print(x) for x in myresult]


""" Delete """
# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")


""" Prevent SQL Injection """  # TODO: Read up more
# sql = "DELETE FROM customers WHERE address = %s"
# adr = ("Yellow Garden 2", )
# mycursor.execute(sql, adr)
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")


""" Delete a Table """
# sql = "DROP TABLE customers"
# mycursor.execute(sql)


""" Delete only if exists """
# sql = "DROP TABLE IF EXISTS customers"
# mycursor.execute(sql)


""" Update Table """
# sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected")


" Prevent SQL Injection "  # TODO: Read up more
# sql = "UPDATE customers SET address = %s WHERE address = %s"
# val = ("Valley 345", "Canyon 123")
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record(s) affected")


""" Limit Results """
# mycursor.execute("SELECT * FROM customers LIMIT 5")
# myresult = mycursor.fetchall()
# [ print(x) for x in myresult ]


" Start From Another Position "
# mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
# myresult = mycursor.fetchall()
# [ print(x) for x in myresult ]


""" Join Two or More Tables """
" Init "
# mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), fav INT)")
# mycursor.execute("CREATE TABLE products (id INT PRIMARY KEY, name VARCHAR(255))")
#
# sql = "INSERT INTO users (name, fav) VALUES (%s, %s)"
# val = [
#     ('John', 154),
#     ('Peter', 154),
#     ('Amy', 155),
#     ('Hannah', None),
#     ('Michael', None)
# ]
# mycursor.executemany(sql, val)
# mydb.commit()
#
# sql = "INSERT INTO products (id, name) VALUES (%s, %s)"
# val = [
#   ('154', 'Chocolate'),
#   ('155', 'Lemon'),
#   ('156', 'Vanilla')
# ]
# mycursor.executemany(sql, val)
# mydb.commit()

" Inner Join "
# sql = "SELECT \
#   users.name AS user, \
#   products.name AS favorite \
#   FROM users \
#   INNER JOIN products ON users.fav = products.id"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# [print(x) for x in myresult]

" Left Join "
# sql = "SELECT \
#   users.name AS user, \
#   products.name AS favorite \
#   FROM users \
#   LEFT JOIN products ON users.fav = products.id"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# [print(x) for x in myresult]

" Right Join "
# sql = "SELECT \
#   users.name AS user, \
#   products.name AS favorite \
#   FROM users \
#   RIGHT JOIN products ON users.fav = products.id"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# [print(x) for x in myresult]