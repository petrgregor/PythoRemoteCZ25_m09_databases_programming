from mysql.connector import connect, Error
from connection_details import *

"""Task:
Update rating for movie Interstellar to 10.
"""
try:
    with connect(host=host, user=user, password=password, database='cinematic') as conn:
        with conn.cursor() as cursor:
            sql_statement = """
                UPDATE movies SET rating = 10
                WHERE title = 'Interstellar';
            """
            cursor.execute(sql_statement)
            conn.commit()

            sql_statement = """
                SELECT * FROM movies
                WHERE title = 'Interstellar';
            """
            cursor.execute(sql_statement)
            result = cursor.fetchone()
            print(*result)

except Error as e:
    print(e)

print("Konec")
