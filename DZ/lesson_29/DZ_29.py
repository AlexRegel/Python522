# DZ_29. Задание:
# Вывести в файл 'persons.json' альтернативным способом функции с урока
# "gen_person()"(стр. 5890 'main') и "write_json(...)"(стр. 5913), таким образом,
# чтобы в базовом виде получился словарь (dict), а не список (list),
# как типы данных Python. Т.е. модифицировать соответствующие функции с урока.

# -- coding: utf8 --.
import json
from random import choice


def gen_person():
    name = ''
    tel = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'k', 'l', 'm', 'n']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letters)
    # print(name)

    while len(tel) != 10:
        tel += choice(nums)
    # print(tel)

    person = {
        'name': name,
        'tel': tel
    }

    return tel, person  # Результат вывода - tuple


def write_json(tuple_person):  # person_dict
    try:
        data_dict = json.load(open("persons.json"))
    except FileNotFoundError:
        data_dict = dict()

    data_dict[tuple_person[0]] = tuple_person[1]
    # print(f"Проверочный вывод в консоль словаря: {data_dict}")
    with open('persons.json', 'w') as f:
        json.dump(data_dict, f, indent=4)


for i in range(5):
    write_json(gen_person())
