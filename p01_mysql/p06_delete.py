from mysql.connector import connect, Error
from connection_details import *

"""Task:
Delete movie with title 'Zodiac'.
"""
try:
    with connect(host=host, user=user, password=password, database='cinematic') as conn:
        with conn.cursor() as cursor:
            sql_statement = """
                DELETE FROM movies 
                WHERE title = 'Zodiac';
            """
            cursor.execute(sql_statement)
            conn.commit()

except Error as e:
    print(e)

print("Konec")
