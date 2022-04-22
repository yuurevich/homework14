from flask import Blueprint, jsonify
from utils import movie_children_search, movie_family_search, movie_adult_search, movie_rating_search

rating_blueprint = Blueprint('rating_blueprint', __name__, url_prefix='/rating')


@rating_blueprint.route('/')
def main():
    return f"""<h1>Выбор фильмов по рейтингу</h1>
                <p><a href='/rating/children/'>Фильмы для детей </a></p>
                <p><a href='/rating/family/'>Фильмы для семьи </a></p>
                <p><a href='/rating/adult/'>Фильмы для взрослых </a></p>
                <p><a href='/rating/PG-13/'>Поиск по рейтингу </a></p>"""


@rating_blueprint.route('/<rating>/')
def rating(rating):
    try:
        movies = movie_rating_search(rating)
        if len(movies) > 0:
            return jsonify(movies)
        else:
            return f'<h1>Фильмов не найдено, проверьте вводимый запрос</h1>'
    except:
        return f'<h1>Фильм не найден</h1>'


@rating_blueprint.route('/children/')
def children():
    try:
        movies = movie_children_search()
        if len(movies) > 0:
            return jsonify(movies)
        else:
            return f'<h1>Фильмов не найдено, проверьте вводимый запрос</h1>'
    except:
        return f'<h1>Фильм не найден</h1>'


@rating_blueprint.route('/family/')
def family():
    try:
        movies = movie_family_search()
        if len(movies) > 0:
            return jsonify(movies)
        else:
            return f'<h1>Фильмов не найдено, проверьте вводимый запрос</h1>'
    except:
        return f'<h1>Фильм не найден</h1>'


@rating_blueprint.route('/adult/')
def adult():
    try:
        movies = movie_adult_search()
        if len(movies) > 0:
            return jsonify(movies)
        else:
            return f'<h1>Фильмов не найдено, проверьте вводимый запрос</h1>'
    except:
        return f'<h1>Фильм не найден</h1>'