
# import json
#
#
# class CountryCapital:
#     @staticmethod
#     def load(file_name):
#         try:
#             data = json.load(open(file_name))
#         except FileNotFoundError:
#             data = {}
#         finally:
#             return data
#
#     @staticmethod
#     def add_country(file_name):
#         new_country = input("Введите название страны: ").lower()
#         new_capital = input("Введите название столицы: ").lower()
#
#         # try:
#         #     data = json.load(open(file_name))
#         # except FileNotFoundError:
#         #     data = {}
#
#         data = CountryCapital.load(file_name)
#
#         data[new_country] = new_capital
#
#         with open(file_name, 'w') as f:  # with open(file_name, encoding="utf8", "w") as f:  #
#             json.dump(data, f, ensure_ascii=False, indent=2)  # ensure_ascii=False,
#
#     # @staticmethod
#     # def load_from_file(file_name, encoding="utf8"):
#     #     with open(file_name) as f:
#     #         print({k.title(): v.title() for k, v in json.load(f).items()})
#     #
#     # @staticmethod
#     # def delete_country(file_name):
#     #     del_country = input("Что удалить: ").lower()
#     #
#     #     try:
#     #         data = json.load(open(file_name))
#     #     except FileNotFoundError:
#     #         data = {}
#     #
#     #     if del_country in data:
#     #         del data[del_country]
#     #     else:
#     #         print("такой страны в базе нет")
#     #
#     #     with open(file_name, "w") as f:  # , encoding="utf8"
#     #         json.dump(data, f, ensure_ascii=False, indent=2)  # ensure_ascii=False,
#     #
#     # @staticmethod
#     # def search_data(file_name):
#     #     country = input("Введите название страны").lower()
#     #
#     #     try:
#     #         data = json.load(open(file_name))
#     #     except FileNotFoundError:
#     #         data = {}
#     #
#     #     if country in data:
#     #         print(f"Странфы {country.title()} есть в словаре")
#     #     else:
#     #         print(f"Странфы {country.title()} нет")
#
#
# file = "list_capital.json"
# while True:
#     index = input("Выбор действия:\n1 - добавление данных\n2 - удаление данных\n3 - поиск данных\n"
#                   "4- редактирование данных\n5- просмотр данных\n6 - завершение работы\n"
#                   "Ввод: ")
#     if index == "1":
#         CountryCapital.add_country(file)
#     # elif index == "2":
#     #     CountryCapital.load_from_file(file)
#     # elif index == "3":
#     #     CountryCapital.delete_country(file)
#     elif index == "6":
#         break
#     else:
#         print("Введён некорректный номер")
#
#     print("*" * 50)
