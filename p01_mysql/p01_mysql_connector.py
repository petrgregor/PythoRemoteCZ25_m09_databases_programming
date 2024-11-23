from mysql.connector import connect, Error
from connection_details import *

try:
    with connect(host=host, user=user, password=password) as conn:
        print(conn)

except Error as e:
    print(e)

print("Konec")
