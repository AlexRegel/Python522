# DZ_20. Задание: Выведите на экран имена и размер всех непустых файлов дерева.
# Создайте директорию work/empty_files и переместите в неё всё пустые файлы,
# при этом для каждого перемещённого файла должно быть выведено соответствующее сообщение,
# содержащее имя файла, старый путь к файлу относительно корневой директории и
# новый путь к файлу после перемещения.
import os
from os.path import join, getsize, split, isdir, isfile

dir_name = "Work"  # Наименование директории в рабочем каталоге, присвоено в переменную
a = """1. Выводим имена и размер всех непустых файлов:"""
print(a)
for root, dirs, files in os.walk(dir_name):  # Проход по директории
    if len(files) != 0:  # условие наличия непустого списка файлов
        for f in files:  # Цикл перебора списка файлов []
            path_to_f = join(root, f)  # получение пути к файлу (имени файла)
            size = getsize(path_to_f)  # получение размера файла # print(f"\t\t\tРазмер файла '{f}' - '{size}' bytes")
            with open(path_to_f, "r") as file:  # Чтение файла
                cont_files = file.read()        # с присвоением содержимого в переменную
            if cont_files:  # Условие наличия содержимого в файле для вывода имени и размера
                print(f"'{path_to_f}' - {size} bytes")

b = f"""\n2. Создаём директорию '{dir_name}/empty_files' (если не создана) и перемещаем в неё пустые файлы, 
(если таковые имеются) с уведомлением о начальных и конечных адресах файлов:"""
print(b)
count_empty_files = 0  # Счётчик кол-ва найденных пустых файлов
moved_count_emp_f = 0  # Счётчик кол-ва перемещённых пустых файлов
for root, dirs, files in os.walk(dir_name):  # , topdown=False
    if len(files) != 0:
        for f in files:  # range(len(files))
            path_to_f = join(root, f)  # получение пути к файлу (имени файла)/начальный путь
            size = getsize(path_to_f)  # получение размера файла
            with open(path_to_f, "r") as file:
                cont_files = file.read()  # Чтение файла
            if not cont_files:  # Условие, если файл пустой
                count_empty_files += 1
                if not isdir(dir_name + r"\empty_files"):  # Условие создания папки 'empty_files', т.е. если её нет.
                    os.mkdir(rf"{dir_name}\empty_files")
                    print("Создана директория:", dir_name + r"\empty_files")
                emp_path = join(rf"{dir_name}\empty_files", f)  # Конечный адрес перемещённых пустых файлов
                if isfile(path_to_f) and not isfile(emp_path):
                    os.renames(path_to_f, emp_path)
                    moved_count_emp_f += 1
                if not isfile(path_to_f) and isfile(emp_path):  # Условие уведомления по факту перемещения пустых файлов
                    dir_ish = os.path.split(path_to_f)  # Картеж для извлечения исходного местоположения пустого файла
                    print(f"Файл '{f}' пустой, перемещён из папки '{dir_ish[0]}' по адр.:",
                          fr"'{dir_name}\empty_files\{f}'.")

print("\nКоличество пустых файлов:", count_empty_files)
if moved_count_emp_f != 0:
    print(fr"В каталог '{dir_name}\empty_files' были перемещены файлы в количестве {moved_count_emp_f} шт..")
else:
    print("Кол-во перемещённых пустых файлов:", moved_count_emp_f)
