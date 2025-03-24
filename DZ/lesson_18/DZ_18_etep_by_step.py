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

st_lst = list(st_f)  # преобразуем строку в список
st_lst_modif1 = st_f.split(";")
for i in range(len(st_lst)):
    if "\n" in st_lst[i]:
        position = st_lst[i].find("\n")
        print(position)
print(st_lst_modif1)

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
