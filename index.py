#import mariadb
import mysql.connector as mariadb

from api.setter import Setter

# mariadb_connection = mariadb.connect(
#     user='lit',
#     password='',
#     database='producten')

Setter().set(504563828929, "Coca")
