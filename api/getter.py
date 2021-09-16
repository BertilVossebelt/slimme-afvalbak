#!/usr/bin/env python3
print('Content-type: text/html\r\n\r')

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

products = []

for row in get:
    products.append({'id': row[0], 'barcode': row[1], 'product': row[2]})

print(products)
