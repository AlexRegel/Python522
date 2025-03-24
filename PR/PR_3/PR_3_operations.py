# fruits = []  # Пустой список
# fruits.append("apple")
# fruits.append("banana")
# fruits.append("cherry")
# print(fruits)
# other_fruits = ["date", "elderberry"]
# fruits.extend(other_fruits)  # Теперь fruits содержит пять элементов
# print(fruits)
# fruits.remove("banana")  # Удаляет первый 'banana' из списка
# print(fruits)
# removed_fruit = fruits.pop(1)  # Удаляет и возвращает элемент на позиции 1
# print(fruits)
# print(removed_fruit)
# print(type(removed_fruit))
# fruits[0] = "blueberry"  # Заменяет элемент на позиции 0 на 'blueberry'
# print(fruits)
#
# numbers = [3, 1, 4, 1, 5]
# numbers.sort()  # Теперь numbers отсортирован
# print(numbers)
# numbers.reverse()  # Теперь numbers перевернут
# print(numbers)
#
#
# numbers = [10, 20, 30, 40, 50]
# # Срез от второго до последнего элемента
# print(numbers[1:len(numbers)-1])  # Вывод: [20, 30, 40]
# # Последний элемент через отрицательный индекс
# print(numbers[-1])  # Вывод: 50
# print(numbers[1:])  # Вывод: [20, 30, 40]
#
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(matrix)
# first_row = matrix[0]  # Получаем первую строку матрицы
# print(first_row)
# element = matrix[1][2]  # Доступ к элементу на второй строке, третьем столбце
# print(element)

# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)
#
# for i in range(len(fruits)):
#     print(f"Индекс: {i}, Элемент: {fruits[i]}")

# my_list = [10, 20, 30]
# print(my_list[3])  # IndexError: list index out of range
# if len(my_list) > 3:
#     print(my_list[3])
# else:
#     print("Индекс вне диапазона")

# fruits = ["apple", "banana", "cherry"]
# print(fruits)
# for fruit in fruits:
#     if fruit == "banana":
#         fruits.remove(fruit)  # Небезопасное изменение списка во время итерации
# print(fruits)
#
# fruits = ["apple", "banana", "cherry"]
# print(fruits)
# for fruit in fruits[:]:  # Итерация по копии списка
#     if fruit == "banana":
#         fruits.remove(fruit)
# print(fruits)