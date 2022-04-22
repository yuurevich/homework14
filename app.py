from flask import Flask, jsonify
from utils import movie_title_search, search_movie_by_year, search_movies_by_genre
from rating.rating import rating_blueprint

app = Flask(__name__)

app.register_blueprint(rating_blueprint)


@app.route('/')
def main():
    return f""" <h1>Netflisk)</h1>
                <p> <strong> <a href='/movie/spider'> Поиск фильма по названию </a> </strong> </p>
                <p> <strong> <a href='/rating'> Поиск фильма по рейтингу </a> </strong> </p>
                <p> <strong> <a href='/genre/Comedies'> Поиск фильма по жанру </a> </strong> </p>
                <p> <strong> <a href='/movie/2015/to/2021'> Поиск фильма по годам </a> </strong> </p> """


@app.route('/movie/<title>')
def about_movie(title):
    try:
        movies = movie_title_search(title)
        if len(movies) > 0:
            return jsonify(movies)
        else:
            return f'<h1>Фильмов не найдено, проверьте вводимый запрос</h1>'
    except:
        return f'<h1>Фильм не найден</h1>'


@app.route('/movie/<starting_year>/to/<end_year>')
def search_by_year(starting_year, end_year):
    try:
        movies = search_movie_by_year(starting_year, end_year)
        if len(movies) > 0:
            return jsonify(movies)
        else:
            return f'<h1>Фильмов не найдено, проверьте условия поиска</h1>'
    except:
        return f'<h1>Проверь вводимый запрос</h1>'


@app.route('/genre/<genre>')
def genre(genre):
    try:
        movies = search_movies_by_genre(genre)
        if len(movies) > 0:
            return jsonify(movies)
        else:
            return f'<h1>Фильмов не найдено, проверьте условия поиска</h1>'
    except:
        return f'<h1>Проверь вводимый запрос</h1>'


if __name__ == '__main__':
    app.run(debug=True)


