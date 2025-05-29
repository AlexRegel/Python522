# к PR 7 модуль 'string_utils.py'
"""Уровень 2: Средний

#Задача: создайте модуль string_utils.py, который содержит функции для работы со строками:
reverse_string(text) — возвращает перевёрнутую строку. count_vowels(text) — возвращает количество гласных букв в строке. is_palindrome(text) — проверяет, является ли строка палиндромом (читается одинаково в обоих направлениях). Напишите основную программу, которая импортирует этот модуль и предоставляет пользователю выбор функции для работы со строкой."""

# def reverse_string(text) -> str:
#     stroka = reverse(text)
#     return stroka


text = "FRASH"
lst = []
for i in range(len(text)):
    lst.append(text[i])
print(lst)

text.split()
print(text)

a = list(text)
print(a)

# lst1 = lst.copy()
#
# lst.reverse()
# lst2 = lst
# # print(lst)
# print(lst1)
# print(lst2)
#
# p = lst.pop(0)
# print(p)
# print(lst2)

# reversed_s = s[::-1]


# tx = text.split()
# print(tx)

# tg = text.join("")
# print(tg)
