# Обмен местами двух строк в файле
# Текст
"""
Замена строки в текстовом файле;
изменить строку в списке;
записать список в файл
"""
# st_f = ("Замена строки в текстовом файле;"
#         "изменить строку в списке;"
#         "записать список в файл;")
st_f = """Замена строки в текстовом файле;
изменить строку в списке;
записать список в файл;
"""

# q = "изменить строку в списке"
# print(q)
# print(len(q))
# q2 = q[1:]
# print(q2)
# print(len(q2))

# st_lst_modif1 = st_f.split(";")  # преобразуем стр. в список с разделителем ";"

file_dz = "test_dz.txt"
f = open(file_dz, "w")
# f.write("Замена строки в текстовом файле;\n"
#         "изменить строку в списке;\n"
#         "записать список в файл;\n")
f.write(st_f)
f.close()

with open(file_dz, "r") as file:
    contents = file.readlines()  # Преобразование содержимого файла в список
    for i in range(len(contents)):
        str_ = contents[i]
        print(f"\tstr_{i + 1}: {str_}", end="")
print("Исходный список (содержимое):", contents)
contents[1], contents[2] = contents[2], contents[1]  # Обмен местами двух элементов списка
print("Список после обмена местами:", contents)
st_lst_modif1 = "".join(contents)  # преобразуем список обратно в строку (\n)
print("Тип данных после преобразования в строки:", type(st_lst_modif1))
print("Для файла подготовлена переменная (строки):\n", st_lst_modif1, sep="")
# Перезапись файла:
with open(file_dz, "w") as file:
    file.write(st_lst_modif1)

# a = """Замена строки в текстовом файле;
# изменить строку в списке;
# записать список в файл;"""
# f = open(file_dz, "w")
# f.write(a)
# f.close()

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
