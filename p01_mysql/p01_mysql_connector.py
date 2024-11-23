from mysql.connector import connect, Error
from connection_details import *

try:
    with connect(host=host, user=user, password=password) as conn:
        print(conn)
        with conn.cursor() as cursor:
            cursor.execute("SELECT VERSION();")
            version = cursor.fetchone()
            print(f"Database version {version[0]}")

except Error as e:
    print(e)

print("Konec")
