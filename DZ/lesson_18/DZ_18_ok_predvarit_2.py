# Задание: Обмен местами двух строк в файле
# Текст (сразу присвоен в переменную, подготовленную для файла):
st_f = """Замена строки в текстовом файле;
изменить строку в списке;
записать список в файл;
"""
file_dz = "test_dz.txt"  # переменная имени файла
# Фрагмент кода, создающий исходный файл (если он не создан)
# Можно закомментировать после создания файла
# f = open(file_dz, "w")
# f.write(st_f)  # Запись содержимого строки "st_f" в файл "test_dz.txt"
# f.close()
# ------------------

# Чтение файла для его редактирования
with open(file_dz, "r") as file:
    contents = file.readlines()  # Преобразование содержимого файла в список
    print("Файл прочитан. Вот построчный результат:")
    for i in range(len(contents)):  # Распаковка содержимого в консоль построчно
        print(f"\tСтрока {i + 1}: {contents[i]}", end="")  # str_ =
# print("Исходный список (содержимое):", contents)
print(f"Введите номера взаимозаменяющих\nстрок (в пределах диапазона"
      f" от 1 до {len(contents)} включительно):")
try:
    pos1 = int(input("pos1 = "))  # 2
    pos2 = int(input("pos2 = "))  # 3
    if 0 <= (pos1 and pos2) <= len(contents):
        contents[pos1-1], contents[pos2-1] = contents[pos2-1], contents[pos1-1]  # Обмен местами двух элементов списка
    else:
        print(f"строки должны быть в пределах диапазона"
              f" от 1 до {len(contents)} включительно. Замена не произведена")

except ValueError:
    print("Ошибка! Перезапустите ПО и введите число")
    print("Завершение программы")

# print("Список после обмена местами:", contents)
st_lst_modif1 = "".join(contents)  # преобразуем список обратно в строку (\n)
# print("Тип данных после преобразования в строки:", type(st_lst_modif1))
print("Для файла подготовлена переменная (строки):\n", st_lst_modif1, sep="")

# Перезапись файла:
with open(file_dz, "w") as file:
    file.write(st_lst_modif1)
if file.closed:
    print("Файл закрыт")

print(file.closed)


# with open(file_dz, "w+") as file:
#     contents = file.readlines()  # Преобразование содержимого в список
#     for i in range(len(contents)):
#         str_ = contents[i]
#         print(f"\tstr_{i + 1}: {str_}", end="")
#
#     file.write(st_lst_modif1)
#     print(contents, end="\n\n")


# number_row_file_dz = len(contents)
# print(number_row_file_dz)
