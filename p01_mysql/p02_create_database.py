from mysql.connector import connect, Error
from connection_details import *

try:
    """Task 1
    From python, connect to the mysql server. Then create the cinematic database."""
    with connect(host=host, user=user, password=password) as conn:
        with conn.cursor() as cursor:
            cursor.execute("CREATE DATABASE IF NOT EXISTS cinematic;")
        print("Database 'cinematic' created.")

except Error as e:
    print(e)


try:
    """Task 2
    Connect to the mysql server by setting the cinematic base as the home / default base."""
    with connect(host=host, user=user, password=password, database='cinematic') as conn:
        print(conn)

except Error as e:
    print(e)


try:
    """Task 3
    Write an SQL query that will create the following tables in the cinematic database:

    directors: director_id(PK), name, surname, rating
    movies: movie_id(PK), title, year, category, director_id(FK), rating"""
    create_table_directors = """
        CREATE TABLE IF NOT EXISTS directors (
            director_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
            name VARCHAR(30),
            surname VARCHAR(30) NOT NULL,
            rating INT
        ) DEFAULT CHARACTER SET utf8;
    """
    create_table_movies = """
        CREATE TABLE IF NOT EXISTS movies (
            movie_id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
            title VARCHAR(50) NOT NULL,
            year SMALLINT,
            category VARCHAR(30),
            director_id INT NOT NULL,
            rating INT,
            CONSTRAINT `movies_director` FOREIGN KEY (`director_id`) REFERENCES `directors` (director_id)
        ) DEFAULT CHARACTER SET utf8;
    """

    with connect(host=host, user=user, password=password, database='cinematic') as conn:
        """Task 4
        Execute the query you wrote earlier creating the tables in the cinematic database."""
        with conn.cursor() as cursor:
            cursor.execute(create_table_directors)
            print("Table 'directors' created.")
            cursor.execute(create_table_movies)
            print("Table 'movies' created.")

except Error as e:
    print(e)

print("Konec")
