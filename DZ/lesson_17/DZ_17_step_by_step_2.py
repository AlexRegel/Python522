# Использовать рекурсию
# Вычислить количество отрицательных чисел в массиве:
# [-2, 3, 8, -11, -4, 6]
# n = 3

array_ = [-2, 3, 8, -11, -4, 6]


def number_neg_elem(array, count=0):
    # count = 0
    # lst_negative = []
    # lst_positive = []
    if len(array) == 1:  # Базовый случай
        print(array, "=> array[0]:", array[0])
        if array[0] < 0:  # Если число отрицательное,
            count += 1  # увеличиваем счётчик вызовов
            print("При '-' крайнем элементе array[0]:", array[0])  # lst_negative.append(array[0])
            print(f"Вызов №{count}: number_neg_elem({array}, count={count})")
            return array[0], count
        else:
            print("При '+' крайнем элементе array[0]:", array[0])
            return array[0], count
    else:
        print(array, "=> array[0]:", array[0])
        if array[0] < 0:
            count += 1
            print("При '-' элементе array[0]:", array[0])  # lst_negative.append(array[0])
              # print("Отрицательный список:", lst_negative, count)
            return number_neg_elem(array[1:], count)
        else:
            print("При '+' элементе array[0]:", array[0])  # lst_positive.append(massiv[0])
            return number_neg_elem(array[1:], count)
                                                            #     print("Положительный список:", lst_positive)
                                                            #     return lst_positive

            # return len(lst_negative)


# print(number_neg_elem(array_))
result, calls = number_neg_elem(array_)
print(f"Количество итераций рекурсии по массиву {array_} равно {result}")
print(f"Количесвто {calls} раз(а)")

# result, calls = factorial(n)
# print(f"Факториал числа {n} равен {result}")
# print(f"Функция была вызвана {calls} раз(а)")

# def factorial(n, counter=0):
#     # Увеличиваем счётчик вызовов
#     counter += 1
#     print(f"Вызов №{counter}: factorial({n})")
#
#     # Базовый случай: если n равно 0 или 1, возвращаем 1
#     if n == 0 or n == 1:
#         return 1, counter
#
#     # Рекурсивный случай: вызываем функцию с n-1
#     result, counter = factorial(n - 1, counter)
#
#     # Возвращаем результат и обновлённый счётчик
#     return n * result, counter
#
#
# # Пример использования
# n = 5
# result, calls = factorial(n)
# print(f"Факториал числа {n} равен {result}")
# print(f"Функция была вызвана {calls} раз(а)")
