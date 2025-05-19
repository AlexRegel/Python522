import pickle
from os import path


class Film:
    def __init__(self, title_film, genre, director, year, duration, studio, actors):
        self.title_film = title_film
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors

    def __str__(self):
        return f"{self.title_film} ({self.genre}, {self.director})"  # {self.duration},


class ModelFilm:
    def __init__(self):
        self.db_film = "db_film.txt"
        self.film = self.load_data_films()  # {}

    def add_film(self, dict_film):
        film = Film(*dict_film.values())  # * - распаковка списка, полученного методом *.values()
        self.film[film.title_film] = film

    def get_all_films(self):
        return self.film.values()

    def get_single_film(self, user_film_information):
        film = self.film[user_film_information]
        dict_film = {
            "название": film.title_film,
            "жанр": film.genre,
            "режиссёр": film.director,
            "год выпуска": film.year,
            "длительность": film.duration,
            "студия": film.studio,
            "актёры": film.actors
        }
        return dict_film

    def remove_film(self, deleted_film):
        return self.film.pop(deleted_film)

    def save_data(self):
        with open(self.db_film, "wb") as fw:
            pickle.dump(self.film, fw)

    def load_data_films(self):
        if path.exists(self.db_film):
            with open(self.db_film, "rb") as fr:  # self.film =
                return pickle.load(fr)
        else:
            return dict()
