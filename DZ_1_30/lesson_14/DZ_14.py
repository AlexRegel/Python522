def arithmetic_mean(*args, **kwargs):  # *args - картеж, *kwargs - словарь
    def my_decorator(fn):
        def wrap(*f_args, **f_kwargs):
            print("Сумма чисел", end=" ")
            for i in range(len(f_args)):  # Цикл вывода (распаковки) картежа через ','
                if i == len(f_args) - 1:  # Условие правильной распаковки (не должно быть крайней запятой)
                    print(f_args[i], sep="", end=" ")
                else:
                    print(f_args[i], ",", sep="", end=" ")
            print("=", fn(*f_args, **f_kwargs))  # Оконечный вывод результата базовой функции
            average_arithmetic = fn(*f_args, **f_kwargs) / len(f_args)
            print('Среднее арифметическое чисел', end=" ")
            for i in range(len(f_args)):  # Цикл вывода (распаковки) картежа через ','
                if i != len(f_args) - 1:  # Условие правильной распаковки (не должно быть крайней ',')
                    print(f_args[i], ",", sep="", end=" ")
                else:
                    print(f_args[i], sep="", end=" ")
            print("=", average_arithmetic)  # Оконечный вывод результата декоратора

        return wrap

    return my_decorator


@arithmetic_mean()
def sum_of_num(*args):
    return sum(args)  # print("Сумма чисел", sum(args), '=')


sum_of_num(2, 3, 3, 4)
# print(sum_of_num(2, 3, 3, 4))

# sum_of_num(5, 2, 3)
