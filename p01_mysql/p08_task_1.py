"""Task 1
Connect to the mysql server and check out all existing databases.
"""

from mysql.connector import connect, Error
from connection_details import *

try:
    with connect(host=host, user=user, password=password) as conn:
        with conn.cursor() as cursor:
            sql_statement = """SHOW DATABASES;"""
            cursor.execute(sql_statement)
            databases = cursor.fetchall()
            for database in databases:
                print(*database)

except Error as e:
    print(e)

print("-"*80)
print("END")
