# Использовать рекурсию
# Вычислить количество отрицательных чисел в массиве:
# [-2, 3, 8, -11, -4, 6]
# n = 3

# array_ = [-2, 3, 8, -11, -4, 6]
# array_ = [18, -6, 12, 2, -4, 23]


def number_neg_elem(array, count_neg=0, iterate=0):
    iterate += 1  # Можно делать без общего счётчика
    if len(array) == 1:  # Базовый случай
        print(array, "=> array[0]:", array[0])
        if array[0] < 0:  # Если число отрицательное,
            count_neg += 1  # увеличиваем счётчик отрицательных элементов (Базовый случай)
        print(f"Вызов №{iterate}: number_neg_elem({array}, count={count_neg})")
        return array[0], count_neg, iterate
    else:
        print(array, "=> array[0]:", array[0])
        if array[0] < 0:  # Если число отрицательное,
            count_neg += 1  # увеличиваем счётчик отрицательных элементов (в рекурсии)
        print(f"Вызов №{iterate}: number_neg_elem({array}, count={count_neg})")
        return number_neg_elem(array[1:], count_neg, iterate)


# Для удобного анализа
array_ = [45, 1, -16, 5, -23, 14, 16, -74, -9, 21]

elem, n, iter_ = number_neg_elem(array_, count_neg=0, iterate=0)
print("\nn =", n)
print("Длина списка", iter_)
