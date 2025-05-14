# -- coding: utf8 --.
# DZ_31. Задание:
# Загрузить json-данные с сайта(ниже ссылка для requests) и перевести их в csv-файл.
# URL для DZ_31: requests(https://jsonplaceholder.typicode.com/todos)

import csv
import requests
import json

url = 'https://jsonplaceholder.typicode.com/todos'

response = requests.get(url)
# print(response.text)  # <class 'str'>
todos = json.loads(response.text)
# print(todos)  # <class 'list'>
# print(todos[0].keys())
file_name = "dict_csv_writer.csv"

with open(file_name, "w") as f:
    writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=todos[0].keys())
    writer.writeheader()
    for d in todos:
        writer.writerow(d)
    print("Файл сохранён")

if f.closed:
    print("Файл закрыт")
