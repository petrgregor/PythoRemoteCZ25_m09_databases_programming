from mysql.connector import connect, Error
from connection_details import *

"""Task 7
Write an SQL query that will remove the tables from the cinematic database. Make an inquiry.
"""
try:
    with connect(host=host, user=user, password=password, database='cinematic') as conn:
        with conn.cursor() as cursor:
            sql_statement = """DROP TABLE movies;"""
            cursor.execute(sql_statement)
            conn.commit()
            print("Table 'movies' deleted.")
            sql_statement = """DROP TABLE directors;"""
            cursor.execute(sql_statement)
            conn.commit()
            print("Table 'directors' deleted.")

except Error as e:
    print(e)

print("Konec")
