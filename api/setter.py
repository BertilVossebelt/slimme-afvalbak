import mysql.connector as mariadb

data = []

mariadb_connection = mariadb.connect(
    user='lit',
    password='',
    database='producten')
#cursor = mariadb_connection.cursor()


class Setter:
    def set(self, barcode, product):
        print(barcode, product)
        sql_select_query = "INSERT INTO producten (barcode, product) VALUES (" + str(barcode) + ", \"" + product + "\")"
        # print(sql_select_query)
        cursor = mariadb_connection.cursor()
        cursor.execute(sql_select_query)
        mariadb_connection.commit()
        print("end")
