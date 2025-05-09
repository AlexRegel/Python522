res = 1
while True:
    a = int(input("Введите число: "))
    if a != 0:
        res = res * a
    if a == 0:
        print("\tРезультат:", res)
        break  # Цикл работает пока пользователь не введёт 0
