# st = input("Введите строку: ")
st = "I am learning Python. hello, WORLD!"
st1 = st[st.find('h') + 1:st.rfind('h')]  # Вырезали необходимый срез строки

# Первый способ переворота вырезанной строки (перебор по самой строке):
st1_reverse1 = ""  # Переменная для получения перевёрнутой строки
for i in range(len(st1)):
    st1_reverse1 += st1[(len(st1) - 1) - i]

# Второй способ переворота вырезанной строки (через список и метод списка .revers):
st_lst = list(st1)  # преобразуем строку в список
st_lst.reverse()  # переворот списка
st1_reverse2 = "".join(st_lst)  # преобразуем список обратно в строку

# Конкатенация с предварительным выделением первого и последнего срезов:
st0 = st[:st.find('h') + 1]
st2 = st[st.rfind('h'):]
st_result1 = st0 + st1_reverse1 + st2
print("Способ 1:\n", st_result1, sep="")

# Либо сразу в одну строку со способом 2:
st_result2 = st[:st.find('h') + 1] + st1_reverse2 + st[st.rfind('h'):]
print("Способ 2:\n", st_result2, sep="")

# А на уроке 16 разобрали ещё один способ (3-й)
# нужно его проверить

# Третий способ обсудили на след, 16-м занятии (Елена Анатольевна):
s = "I am learning Python. hello, WORLD!"
a = s[:s.find("h")]
b = s[s.find("h"):s.rfind("h") + 1]
c = s[s.rfind("h") + 1:]
print("Способ 3 (через срезы):\n", a + b[::-1] + c, sep="")
# print(a + b[::-1] + c)
