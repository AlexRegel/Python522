# Создаём начальный список. Задаём кол-во студентов и вводим имена пользователей:
# lst_students = [input(f"{i + 1}-й студент: ") for i in range(int(input("Введите кол-во студентов: n = ")))]
# print("Создан список студентов: lst_students =", lst_students, end="\n")

# dict_students = {ir: int(input(f"Оценка {ir}: ")) for ir in [input(f"{i + 1}-й студент: ") for i in range(int(input("Введите кол-во студентов: n = ")))]}   #
# Создан список студентов: lst_students = ['Лапушин Миша', 'Гребнев Олег', 'Вернадская Анна']
# print("Создание словаря.")
n = range(int(input("Введите кол-во студентов: n = ")))
dict_students = {}  # b_dict = {} Создан пустой словарь
lst_students = []
lst_rating = []
for i in n:  # lst = ["John", "Tom", "Anne", "Fiona"]
    name_and_family = input(f"{i + 1}-й студент: ")  # (lst_students)
    lst_students.append(name_and_family)
    rating = int(input(f"Балл студента {name_and_family}: "))
    lst_rating.append(rating)

dict_students = dict(zip(lst_students, lst_rating))
print()
print("Создан словарь: \n", dict_students, end="\n\n")

# Создан словарь:
# dict_students = {'Лапушин Миша': 7, 'Гребнев Олег': 11, 'Вернадская Анна': 10}
s = 0  # Задаём переменную суммы баллов для подсчёта среднего
for key in dict_students:  # .items() # , value
    value = dict_students.get(key)
    s += value  # Сумма баллов
    # print(value)
avr = s / len(dict_students)  # Среднее значение баллов
print(f"Средний балл: {round(avr)}.", "Студенты с баллом выше среднего:")
for key, value in dict_students.items():
    if value > round(avr):
        print(key)
