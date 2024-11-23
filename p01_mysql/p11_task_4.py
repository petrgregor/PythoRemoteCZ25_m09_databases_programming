"""Task 4
Write a function get_instruments_count which will show
the number of instruments for each category.
The function should take a connection as an argument.
It will return records consisting of dictionaries
with two keys - 'family' and 'count'."""

from mysql.connector import connect, Error
from connection_details import *


def get_instruments_count(connection):
    with connection.cursor(dictionary=True) as cursor:
        sql_statement = """
            SELECT family, count(*) as count
            FROM instruments
            GROUP BY family;
        """
        cursor.execute(sql_statement)
        return cursor.fetchall()


try:
    with connect(host=host, user=user, password=password, database='music') as conn:
        results = get_instruments_count(conn)
        for result in results:
            print(result)

except Error as e:
    print(e)


print('-'*80)
print("END")
