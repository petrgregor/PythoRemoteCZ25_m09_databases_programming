"""Task 2
Write a script that will create a music database with the table:
instruments: isntrument_id(PK, autoincrement), name, family, difficulty(enum - easy, medium, hard)
"""

from mysql.connector import connect, Error
from connection_details import *

try:
    with connect(host=host, user=user, password=password) as conn:
        with conn.cursor() as cursor:
            sql_statement = """CREATE DATABASE IF NOT EXISTS music;"""
            cursor.execute(sql_statement)
            print("Database 'music' created.")

            sql_statement = """
                CREATE TABLE IF NOT EXISTS music.instruments (
                    instrument_id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                    name VARCHAR(30) NOT NULL,
                    family VARCHAR(30) NOT NULL,
                    difficulty ENUM('easy', 'medium', 'hard') NOT NULL
                );
            """
            cursor.execute(sql_statement)
            print("Table 'instruments' created.")

except Error as e:
    print(e)

print('-'*80)
print("END")
