# Создаём размер диапазона и вводим элементы списка:
lst = [int(input("-> ")) for i in range(int(input("Введите кол-во эл-в списка: n = ")))]
print("Создан следующий список: lst =", lst, end="\n")
SumNegative = 0  # Создана переменная для подсчёта суммы отрицательных элементов
for i in range(len(lst)):
    print(end="\t")
    print(lst[i], end="\n")
    if lst[i] < 0:
        SumNegative += lst[i]
    print("index i =", i, end="\n")
    if i == len(lst)-1:
        print("Завершение: SumNegative =", SumNegative, end="\n")
        print()
    else:
        print("SumNegative =", SumNegative, end="\n")

print("Сумма отрицательных элементов:", SumNegative, end="")

# for i in range(len(lst)):  # 0 1 2 3
#     print(lst[i], end=" ")
