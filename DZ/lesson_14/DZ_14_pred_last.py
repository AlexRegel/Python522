def arithmetic_mean(*args, **kwargs):
    def my_decorator(fn):
        def wrap(*f_args, **f_kwargs):
            print("Сумма чисел", end=" ")
            print(*f_args, "=", end=" ")  # sep=", ",
            count = 0
            for i in range(len(f_args)):
                count += 1
            print(fn(*f_args, **f_kwargs))
            average_arithmetic = fn(*f_args, **f_kwargs) / count

            print('Среднее арифметическое чисел', f_args, '=', average_arithmetic)  # , end="\n"

        return wrap

    return my_decorator


@arithmetic_mean(int, int, int)
def sum_of_num(*args):
    return sum(args)  # print("Сумма чисел", args, '=', s)


# print(sum_of_num(5, 2, 3))
sum_of_num(5, 2, 3)

# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) is not args[i]:
#                     raise TypeError("Неверный тип данных")  # return "Неверный тип данных"
#             # for k in kwargs:
#             #     if type(f_kwargs) is not kwargs[k]:
#             #         raise TypeError("Неверный тип данных")
#             return fn(*f_args, **f_kwargs)  # raise в отличие от return останавливает прграмму в ош
#
#         return wrap
#
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "Hello"))
# print(typed_fn2("Hello", " World", "!"))
# # print(typed_fn2(3, 4, 5))
# print(typed_fn3("Hello", " World", z=5))
# # print(typed_fn3("Hello", " World", z="!"))
