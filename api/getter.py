#!/usr/bin/python3

# This file cannot be included as a function into the Setter class
# because it needs to be accessible from the web.
print('Content-type: text/html\r\n\r')

import mysql.connector as mariadb

# Connect to database
mariadb_connection = mariadb.connect(
    user='lit',
    password='',
    database='producten')


# Setup a query and execute it
sql_select_Query = "SELECT * FROM producten"
cursor = mariadb_connection.cursor()
cursor.execute(sql_select_Query)

# Get the results and prepare empty array
get = cursor.fetchall()
products = []

# Loop over all the results and add them as an object to the products array
for row in get:
    products.append({'id': row[0], 'barcode': row[1], 'product': row[2]})

# Dump results in object format so it can be easily used
# in the JavaScript part of the application.
print(products)
