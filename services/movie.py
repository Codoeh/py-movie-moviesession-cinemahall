from django.db.models import Q, QuerySet
from db.models import Movie, Genre, Actor


def get_movies(
        genres_ids: list = None,
        actors_ids: list = None) -> QuerySet:
    query = Movie.objects.all()
    if genres_ids and actors_ids:
        query = query.filter(
            Q(genres__id__in=genres_ids)
            & Q(actors__id__in=actors_ids))
    elif genres_ids:
        query = query.filter(genres__id__in=genres_ids)
    elif actors_ids:
        query = query.filter(actors__id__in=actors_ids)
    return query.distinct()


def get_movie_by_id(movie_id: int) -> Movie:
    return Movie.objects.get(id=movie_id)


def create_movie(movie_title: str,
                 movie_description: str,
                 genres_ids: list = None,
                 actors_ids: list = None) -> None:
    movie, created = Movie.objects.get_or_create(
        title=movie_title,
        description=movie_description)
    if genres_ids:
        genres = Genre.objects.filter(id__in=genres_ids)
        movie.genres.set(genres)
    if actors_ids:
        actors = Actor.objects.filter(id__in=actors_ids)
        movie.actors.set(actors)
    movie.save()
