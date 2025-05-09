
st = "I am learning Python. hello, WORLD!"

st1 = st[st.find('h') + 1:st.rfind('h')]  # Вырезали необходимый срез строки
print(st1)
# Первый способ переворота вырезанной строки (перебор по самой строке):
st1_reverse1 = ""  # Переменная для получения перевёрнутой строки
for i in range(len(st1)):
    st1_reverse1 += st1[(len(st1) - 1) - i]
print("Перевёрнутая строка (способ 1):", st1_reverse1)
# Второй способ переворота вырезанной строки (через список и метод списка .revers):
st_lst = list(st1)  # преобразуем строку в список
st_lst.reverse()  # переворот списка
st1_reverse2 = "".join(st_lst)  # преобразуем список обратно в строку
print("Перевёрнутая строка (способ 2):", st1_reverse2)
# Конкатенация с предварительным выделением первого и последнего срезов
st0 = st[:st.find('h') + 1]
print(st0)
st2 = st[st.rfind('h'):]
print(st2)
st_result = st0 + (st1_reverse2 or st1_reverse1) + st2
print(st_result)
