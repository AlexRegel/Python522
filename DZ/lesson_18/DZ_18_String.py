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
записать список в файл"""

# st_lst = list(st_f)  # преобразуем строку в список
# print(st_lst)

st_lst_modif1 = st_f.split(";")  # преобразуем стр. в список с разделителем ";"
count = 0
for i in range(len(st_lst_modif1)):
    count += 1
    if "\n" in st_lst_modif1[i]:  # цикл отделения \n
        print("Полная строка", count, st_lst_modif1[i])
        position = st_lst_modif1[i].find("\n")  # позиция лишнего символа \n
        print(position + 1, type(position))  # 1
        t = len(st_lst_modif1[i]) - (len(st_lst_modif1[i]) - (position + 1))
        print("Позиция от которой плясать - t =", t)
        st1_empty_n = st_lst_modif1[i][t:]
        print(f"Строка №{count} без \\n:", st1_empty_n)
        print(f"Длина строки №{count} с \\n = {len(st_lst_modif1[i])}")
        print(f"Длина строки №{count} без \\n = {len(st1_empty_n)}")
        # temp_lst = list(st_lst_modif1[i])
        # print(temp_lst)
        # st1_ = "".join(st_lst)
print("Кол-во итераций (элементов списка):", count)
print(st_lst_modif1)

# q = "изменить строку в списке"
# print(q)
# print(len(q))
# q2 = q[1:]
# print(q2)
# print(len(q2))

# file_dz = "test_dz.txt"
# f = open(file_dz, "w")
# f.write("Замена строки в текстовом файле;\n"
#         "изменить строку в списке;\n"
#         "записать список в файл;\n")
# f.close()

# with open(file_dz, "r") as file:
#     contents = file.readlines()  # Преобразование содержимого в список
#     for i in range(len(contents)):
#         str_ = contents[i]
#         print(f"\tstr_{i+1}: {str_}", end="")
# contents[1], contents[2] = contents[2], contents[1]
# st_lst_modif1 = "\n".join(contents)
# print("для файла:\n", st_lst_modif1)
# print(end="\n\n")
# print(contents)

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
