"""Exercise 1
Create bikesharing table in bikesharing database with the following columns:
● tstamp timestamp
● cnt integer
● temperature decimal(5, 2)
● temperature_feels decimal(5, 2)
● humidity decimal(4, 1)
● wind_speed decimal(5,2)
● weather_code integer
● is_holiday boolean
● is_weekend boolean
● season integer
"""

from mysql.connector import connect, Error
from connection_details import *


try:
    with connect(host=host, user=user, password=password) as conn:
        with conn.cursor() as cursor:
            sql_statement = """CREATE DATABASE IF NOT EXISTS bikesharing;"""
            cursor.execute(sql_statement)
            print("Database 'bikesharing' created.")

            sql_statement = """
                CREATE TABLE IF NOT EXISTS bikesharing.bikesharing (
                    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
                    tstamp TIMESTAMP NOT NULL,
                    cnt INT,
                    temperature DECIMAL(5, 2),
                    temperature_feels DECIMAL(5, 2),
                    humidity DECIMAL(4, 1),
                    wind_speed DECIMAL(5, 2),
                    weather_code INT,
                    is_holiday BOOLEAN,
                    is_weekend BOOLEAN,
                    season INT
                );
            """
            cursor.execute(sql_statement)
            print("Table 'bikesharing' created.")

except Error as e:
    print(e)

print('-'*80)
print("END")
