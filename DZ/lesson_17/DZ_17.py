# Использовать рекурсию
# Вычислить количество отрицательных чисел в массиве:
# [-2, 3, 8, -11, -4, 6]


def number_neg_elem(array, count_neg=0):  # В качестве аргументов - список (массив) и счётчик отрицательных чисел
    if len(array) == 1:  # Базовый случай
        if array[0] < 0:  # Если число отрицательное,
            count_neg += 1  # увеличиваем счётчик отрицательных элементов (Базовый случай)
        return array[0], count_neg
    else:  # Рекурсивный случай
        if array[0] < 0:  # Если число отрицательное,
            count_neg += 1  # увеличиваем счётчик отрицательных элементов (в рекурсии)
        return number_neg_elem(array[1:], count_neg)


array_ = [45, 1, -16, 5, -23, 14, 16, -74, -9, 21]
# array_ = [-2, 3, 8, -11, -4, 6]

last_elem, n = number_neg_elem(array_, 0)
print("В массиве (списке):\n", array_, sep="")
print("Количество отрицательных чисел:\nn =", n)


# Второй вариант выполнения (рассмотрели на уроке)


# def negative_numbers(n):
#     if not n:
#         return 0
#     count = 0
#     if n[0] < 0:
#         count += 1
#     return count + negative_numbers(n[1:])
#
#
# lst = [-2, 3, 8, -11, -4, 6]
# print(negative_numbers(lst))
