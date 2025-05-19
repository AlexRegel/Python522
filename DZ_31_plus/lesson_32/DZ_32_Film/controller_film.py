# DZ_31_plus.lesson_32.DZ_32_Film.view_film
# from DZ_31_plus.lesson_32.DZ_32_Film.model_film import ModelFilm
from view_film import Interface
from model_film import ModelFilm


class ControllerFilm:
    def __init__(self):
        self.model_film = ModelFilm()
        self.user_interface = Interface()

    def run(self):
        answer = None
        while answer != 'q':
            answer = self.user_interface.wait_user_answer()
            self.check_user_answer(answer)

    def check_user_answer(self, answer):
        if answer == "1":
            film_info = self.user_interface.add_film_info()
            self.model_film.add_film(film_info)
        elif answer == "2":
            films_information = self.model_film.get_all_films()
            self.user_interface.show_all_films(films_information)
        elif answer == "3":
            film_information = self.user_interface.get_user_film()
            try:
                film = self.model_film.get_single_film(film_information)
            except KeyError:
                self.user_interface.show_incorrect_film_error(film_information)
            else:
                self.user_interface.show_single_film(film)
        elif answer == "4":
            film_information = self.user_interface.get_user_film()
            try:
                removed_film = self.model_film.remove_film(film_information)
            except KeyError:
                self.user_interface.show_incorrect_film_error(film_information)
            else:
                self.user_interface.remove_single_film(removed_film)

        elif answer == "q":
            self.model_film.save_data()
        else:
            self.user_interface.show_incorrect_answer_user_error(answer)
