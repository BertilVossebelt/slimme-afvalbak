import mysql.connector as mariadb

data = []

mariadb_connection = mariadb.connect(
    user='lit',
    password='',
    database='producten')

sql_select_Query = "SELECT * FROM producten"
cursor = mariadb_connection.cursor()
cursor.execute(sql_select_Query)

get = cursor.fetchall()
print("Aantal rijen in het tabel: ", cursor.rowcount)

print("\nElke rij: ")
for row in get:
    print("Id = ", row[0], )
    print("Barcode = ", row[1])
    print("Product = ", row[2])
