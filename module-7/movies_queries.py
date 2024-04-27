#Melissa Lawrence, CSD 310, Assignment 7.2, 04/27/2024

import mysql.connector
from mysql.connector import errorcode


config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
    }


try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\n Press any key to continue...")
    cursor = db.cursor()

#Query 1: Select all fields from the studio table
    cursor.execute("SELECT * FROM studio")
    studio_results = cursor.fetchall()
    print("\n\n-- DISPLAYING Studio RECORDS --")
    for studio in studio_results:
        print("Studio ID: {} \nStudio Name: {}\n".format(studio[0], studio[1]))

#Query 2: Select all fields from the genre table
    cursor.execute("SELECT * FROM genre")
    genre_results = cursor.fetchall()
    print("\n\n-- DISPLAYING Genre RECORDS --")
    for genre in genre_results:
        print("Genre ID: {} \nGenre Name: {}\n".format(genre[0], genre[1]))
        
#Query 3: Select movie names with a run time of less than two hours
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    film_results = cursor.fetchall()
    print("\n\n--  DISPLAY Short Film RECORD  --")
    for film in film_results:
        print("Film Name: {}\nRuntime: {}\n".format(film[0], film[1]))

#Query 4: Get a list of film names and directors grouped by director newest to oldest
    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_releaseDate DESC")
    film_results = cursor.fetchall()
    print("\n\n--  DISPLAY Director RECORD in Order  --")
    for information in film_results:
        print("Film Name: {}\nDirector: {}\n".format(information[0], information[1]))


except mysql.connector.Error as err:
    
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")
        
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")
        
    else:
        print(err)

finally:
    db.close()
