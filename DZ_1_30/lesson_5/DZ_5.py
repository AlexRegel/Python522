# Создаём размер диапазона и вводим элементы списка:
lst = [int(input("-> ")) for i in range(int(input("Введите кол-во эл-в списка: n = ")))]
print("Создан следующий список: lst =", lst, end="\n")
SumNegative = 0  # Создана переменная для подсчёта суммы отрицательных элементов
for i in range(len(lst)):
    if lst[i] < 0:
        SumNegative += lst[i]
print("Сумма отрицательных элементов:", SumNegative, end="")
