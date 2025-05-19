def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f"{title}".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output

        return wrap

    return wrapper


class Interface:
    @add_title(" Редактирование данных каталога фильмов ")
    def wait_user_answer(self):
        # print(" Редактирование данных каталога фильмов ".center(50, "="))
        print("Действия с фильмами:")
        print("1 - добавление фильма"
              "\n2 - каталог фильмов"
              "\n3 - просмотр определённого фильма"
              "\n4 - удаление фильма"
              "\nq - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        # print("=" * 50)
        return user_answer

    @add_title("Добавление фильма")
    def add_film_info(self):
        dict_film = {
            "название": None,
            "жанр": None,
            "режиссёр": None,
            "год выпуска": None,
            "длительность": None,
            "студия": None,
            "актёры": None
        }
        # print(" Добавление фильма ".center(50, "="))
        for key in dict_film:
            dict_film[key] = input(f"Введите {key} фильма: ")
            # print("=" * 50)
        return dict_film

    @add_title("Список фильмов")
    def show_all_films(self, films_information):
        # print(" Список фильмов ".center(50, "="))  # вынесен в декоратор
        for index, film in enumerate(films_information, 1):
            print(f"{index}. {film}")
        # print("=" * 50)  # вынесен в декоратор

    @add_title("Ввод названия фильма")
    def get_user_film(self):
        user_film = input("Введите название фильма: ")
        return user_film

    @add_title("Просмотр определённого фильма")
    def show_single_film(self, film):
        for key in film:
            print(f"{key} фильма - {film[key]}")

    @add_title(" Сообщение об ошибке!!! ")
    def show_incorrect_film_error(self, user_title_films):
        print(f"Фильма с названием \"{user_title_films}\" не существует.")

    @add_title("Сообщение об удалённом фильме")
    def remove_single_film(self, film):
        print(f"Фильм \"{film}\" - был удалён")

    @add_title(" Сообщение об ошибке!!! ")
    def show_incorrect_answer_user_error(self, incorrect_answer):
        print(f"Некорректный ввод: Варианта \"{incorrect_answer}\" - не существует")
