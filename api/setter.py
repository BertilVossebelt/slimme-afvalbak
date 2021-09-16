#!/usr/bin/python3
import mysql.connector as mariadb

# Connect to database
mariadb_connection = mariadb.connect(
    user='lit',
    password='',
    database='producten'
)


class Setter:
    # This function is used to insert data into the database.
    # The data is delivered by Scanner.py
    def set(self, barcode, product):
        # Setup a query with values and execute it.
        sql_select_query = "INSERT INTO producten (barcode, product) VALUES (" + str(barcode) + ", \"" + product + "\")"
        mariadb_connection.cursor().execute(sql_select_query)
        mariadb_connection.commit()
