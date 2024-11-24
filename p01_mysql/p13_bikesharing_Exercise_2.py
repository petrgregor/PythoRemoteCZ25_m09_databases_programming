"""Exercise 2
● load values from london-bikes.csv and insert it into the database, one by one
● * commit after every 100 inserts, not after every one
"""
import csv
import datetime

from mysql.connector import connect, Error
from connection_details import *


try:
    with connect(host=host, user=user, password=password, database='bikesharing') as conn:
        with open('../files/london-bikes.csv') as f:
            london_bikes = csv.reader(f)
            with conn.cursor() as cursor:
                i = 0
                next(london_bikes)  # skip first line (header)
                for row in london_bikes:
                    sql_statement = f"""
                        INSERT INTO bikesharing (tstamp, cnt, temperature, temperature_feels, humidity,
                            wind_speed, weather_code, is_holiday, is_weekend, season)
                            VALUES ('{row[0]}', '{row[1]}', '{row[2]}', '{row[3]}', '{row[4]}', '{row[5]}', '{row[6]}', '{row[7]}', '{row[8]}', '{row[9]}');
                            
                    """
                    cursor.execute(sql_statement)
                    i += 1
                    if i % 100 == 0:
                        conn.commit()
                conn.commit()
                print(f"Inserted {i} records.")

except Error as e:
    print(e)
except FileNotFoundError as e:
    print(e)


print('-'*80)
print("END")
