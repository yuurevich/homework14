import sqlite3
import json


def step_five(first_actor,  second_actor):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = f"""SELECT `cast`
                        FROM netflix
                        WHERE `cast` LIKE '%{first_actor}%'
                        AND `cast` LIKE '%{second_actor}%' 
                        """
    cur.execute(sqlite_query)
    data = cur.fetchall()
    oll_actors = []
    result = []
    for cast in data:
        actors = cast[0].split(', ')
        oll_actors.extend(actors)
    for actor in oll_actors:
        if oll_actors.count(actor) >= 2 and actor != first_actor and actor != second_actor:
            result.append(actor)
    return result


def step_six(type, year, genre):
    movies = []
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    sqlite_query = f"""SELECT title, description
                        FROM netflix
                        WHERE type LIKE '%{type}%'
                        AND release_year LIKE '%{year}%' 
                        AND listed_in LIKE '%{genre}%' 
                        ORDER BY release_year DESC
                        LIMIT 5"""
    cur.execute(sqlite_query)
    result = cur.fetchall()
    for title, description in result:
        details = dict()
        details['title'] = title
        details['description'] = description
        movies.append(details)
    movies = json.dumps(movies)
    json_movies = json.loads(movies)
    return json_movies


print(step_five('Jack Black', 'Dustin Hoffman'))
print(step_five('Rose McIver', 'Ben Lamb'))
print(step_six('movie', 2015, 'Action'))


##########################################


def database_query(query):
    con = sqlite3.connect("netflix.db")
    cur = con.cursor()
    cur.execute(query)
    result = cur.fetchall()
    return result


def movie_title_search(arg):
    """Функция возвращает словарь с описанием найденных фильмов по названию"""
    movies = []
    sqlite_query = f"""SELECT title, country, release_year, description, listed_in  
                                    FROM netflix
                                    WHERE title LIKE '%{arg}%'
                                    AND type='Movie'
                                    ORDER BY release_year DESC
                                    LIMIT 10"""
    result = database_query(sqlite_query)

    for title, country, release_year, description, listed_in in result:
        details = dict()
        details['title'] = title
        details['country'] = country
        details['release_year'] = release_year
        details['description'] = description
        details['genre'] = listed_in
        movies.append(details)
    return movies


def search_movie_by_year(starting_year, end_year):
    """Функция возвращает словарь с описанием найденных фильмов отсортированных по указанному периоду даты выхода"""
    movies = []
    sqlite_query = f"""SELECT title,  release_year 
                        FROM netflix
                        WHERE release_year BETWEEN {starting_year} AND {end_year}
                        AND type='Movie'
                        ORDER BY release_year DESC
                        LIMIT 100"""
    result = database_query(sqlite_query)

    for title, release_year in result:
        movies_dict = dict()
        movies_dict['title'] = title
        movies_dict['release_year'] = release_year
        movies.append(movies_dict)
    return movies


def search_movies_by_genre(genre):
    """Функция возвращает словарь с описанием найденных фильмов отсортированных по жанрам"""
    movies = []
    sqlite_query = f"""SELECT title, description, listed_in
                                       FROM netflix
                                       WHERE listed_in LIKE '%{genre}%'
                                       AND type='Movie'
                                       ORDER BY release_year DESC
                                       LIMIT 10"""

    result = database_query(sqlite_query)

    for title, description, listed_in in result:
        movies_dict = dict()
        movies_dict['title'] = title
        movies_dict['description'] = description
        movies_dict['genre'] = listed_in
        movies.append(movies_dict)
    return movies


def movie_rating_search(rating):
    """Функция находит фильмы в базе данных с рейтингом G"""
    sqlite_query = f"""SELECT title, rating, description 
                                       FROM netflix
                                       WHERE rating LIKE '%{rating}%'
                                       AND type='Movie'
                                       ORDER BY release_year DESC
                                       LIMIT 10"""

    result = database_query(sqlite_query)
    return packing_data_into_a_dictionary(result)


def movie_children_search():
    """Функция находит фильмы в базе данных с рейтингом G"""
    sqlite_query = f"""SELECT title, rating, description 
                                       FROM netflix
                                       WHERE rating LIKE '%G%'
                                       AND type='Movie'
                                       ORDER BY release_year DESC
                                       LIMIT 100"""
    result = database_query(sqlite_query)
    return packing_data_into_a_dictionary(result)


def movie_family_search():
    """Функция находит фильмы в базе данных с рейтингом G, PG, PG-13"""
    sqlite_query = f"""SELECT title, rating, description 
                                           FROM netflix
                                           WHERE rating LIKE '%G%'
                                           OR rating LIKE '%PG%'
                                           OR rating LIKE '%PG-13%'
                                           AND type='Movie'
                                           ORDER BY release_year DESC
                                           LIMIT 100"""
    result = database_query(sqlite_query)
    return packing_data_into_a_dictionary(result)


def movie_adult_search():
    """Функция находит фильмы в базе данных с рейтингом R, NC-17"""
    sqlite_query = f"""SELECT title, rating, description 
                                       FROM netflix
                                       WHERE rating LIKE '%NC-17%'
                                       OR rating LIKE '%R%'
                                       AND type='Movie'
                                       ORDER BY release_year DESC
                                       LIMIT 100"""
    result = database_query(sqlite_query)
    return packing_data_into_a_dictionary(result)


def packing_data_into_a_dictionary(data):
    movies = []
    for title, rating, description in data:
        details = dict()
        details['title'] = title
        details['rating'] = rating
        details['description'] = description
        movies.append(details)
    return movies


