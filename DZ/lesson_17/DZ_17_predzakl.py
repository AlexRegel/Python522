# Использовать рекурсию
# Вычислить количество отрицательных чисел в массиве:
# [-2, 3, 8, -11, -4, 6]
# n = 3

# array_ = [-2, 3, 8, -11, -4, 6]
array_ = [18, -6, 12, 2, -4, 23]


def number_neg_elem(array, count_neg=0, iterate=0):
    iterate += 1  # Можно делать без общего счётчика
    if len(array) == 1:  # Базовый случай
        print(array, "=> array[0]:", array[0])
        if array[0] < 0:    # Если число отрицательное,
            count_neg += 1  # увеличиваем счётчик отрицательных элементов (Базовый случай)
        print(f"Вызов №{iterate}: number_neg_elem({array}, count={count_neg})")
        return array[0], count_neg, iterate
    else:
        print(array, "=> array[0]:", array[0])
        if array[0] < 0:    # Если число отрицательное,
            count_neg += 1  # увеличиваем счётчик отрицательных элементов (в рекурсии)
        print(f"Вызов №{iterate}: number_neg_elem({array}, count={count_neg})")
        return number_neg_elem(array[1:], count_neg, iterate)


# Для удобного анализа

# print(number_neg_elem(array_)[0])

# print(number_neg_elem(array_, count_neg=0, iterate=0))

# print(type(number_neg_elem(array_, count_neg=0, iterate=0)))
elem, n, iter_ = number_neg_elem(array_, count_neg=0, iterate=0)
print(elem)
print("n =", n)
print("Количество элементов массива:", iter_)
# print(f"Количество итераций рекурсии по массиву {array_} равно {iter_} - это длина массива, \n"
#       f"из них, выявленное количество орицательных элементов: {number_neg_elem(array_)[1]} шт.")
