# Создаём начальный диапазон. Задаём кол-во студентов и вводим данные по ним:
n = range(int(input("Введите кол-во студентов: n = ")))
dict_students = {}  # b_dict = {} Создан пустой словарь
lst_students = []
lst_rating = []
for i in n:  # Цикл создания двух списков [Студентов][Оценок]
    name_and_family = input(f"{i + 1}-й студент: ")  # (lst_students)
    lst_students.append(name_and_family)
    rating = int(input(f"Балл студента {name_and_family}: "))
    lst_rating.append(rating)

dict_students = dict(zip(lst_students, lst_rating))
print()
# print("Создан словарь: \n", dict_students, end="\n\n")

# Создан словарь:
# dict_students = {'Игорь': 12, 'Валентин': 7, 'Виктор': 4, 'Григорий': 9, 'Дмитрий': 6}
s = 0  # Задаём переменную суммы баллов для подсчёта среднего
for key in dict_students:  # Цикл подсчёта среднего балла
    value = dict_students.get(key)
    s += value  # Общая сумма баллов
avr = s / len(n)  # Среднее значение баллов (n = len(dict_students))
print(f"Средний балл: {round(avr)}.", "Студенты с баллом выше среднего:")
for key, value in dict_students.items():  # Цикл для вывода студентов с баллом выше среднего
    if value > round(avr):
        print(key)

# От Зульфии Анвировны вариант решения среднего балла
print()
sr_bal = round(sum(dict_students.values()) / len(n))
print(sr_bal)

