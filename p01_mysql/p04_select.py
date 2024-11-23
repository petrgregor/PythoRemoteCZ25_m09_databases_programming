from mysql.connector import connect, Error
from connection_details import *

try:
    with connect(host=host, user=user, password=password, database='cinematic') as conn:
        with conn.cursor() as cursor:
            sql_statement = """SELECT * FROM movies;"""
            cursor.execute(sql_statement)
            movies = cursor.fetchall()
            print("=================== MOVIES ===================")
            print("id\ttitle\tyear\tcategory\tdirector_id\trating")
            for movie in movies:
                print(f"{movie[0]}\t{movie[1]}\t{movie[2]}\t{movie[3]}\t{movie[4]}\t{movie[5]}")

            sql_statement = """SELECT * FROM directors;"""
            cursor.execute(sql_statement)
            directors = cursor.fetchall()
            print("=================== DIRECTORS ===================")
            for director in directors:
                print(*director)

            taks = """Task 6
Write an SQL query that will return all movies from 2002. Make an inquiry."""
            print("=================== MOVIES (year = 2002) ===================")
            sql_statement = """SELECT * FROM movies WHERE year = 2002;"""
            cursor.execute(sql_statement)
            movies = cursor.fetchall()
            for movie in movies:
                print(*movie)

            print("=================== MOVIES (year = 1994) ===================")
            sql_statement = """SELECT * FROM movies WHERE year = 1994;"""
            cursor.execute(sql_statement)
            movies = cursor.fetchall()
            for movie in movies:
                print(*movie)

            print("=================== MOVIES (year = 1994) with director name + surname ===================")
            sql_statement = """
            SELECT * FROM movies 
                LEFT JOIN cinematic.directors d on movies.director_id = d.director_id 
                WHERE year = 1994;
            """
            cursor.execute(sql_statement)
            movies = cursor.fetchall()
            for movie in movies:
                print(f"Movie '{movie[1]}' directed by '{movie[7]} {movie[8]}'.")

            print("=================== MOVIES CATEGORY COUNT ===================")
            sql_statement = """
                SELECT category, COUNT(category) FROM movies GROUP BY category;
            """
            cursor.execute(sql_statement)
            results = cursor.fetchall()
            for result in results:
                print(*result)

            print("=================== 5 MOVIES WITH HIGHEST RATING ===================")
            sql_statement = """
                SELECT * FROM movies
                ORDER BY rating DESC
                LIMIT 5;
            """
            cursor.execute(sql_statement)
            results = cursor.fetchall()
            for result in results:
                print(*result)

            print("=================== n MOVIES WITH HIGHEST RATING ===================")
            n = int(input("How many results do you want? "))
            sql_statement = f"""
                            SELECT * FROM movies
                            ORDER BY rating DESC
                            LIMIT {n};
                        """
            cursor.execute(sql_statement)
            results = cursor.fetchall()
            for result in results:
                print(*result)

except Error as e:
    print(e)

print("Konec")
