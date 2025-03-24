# goods = {
#     "1": ['Core-i3-4330', 9, 4500],
#     "2": ['Core-i5-4670', 3, 8500],
#     "3": ['AMD FX-6300', 6, 3700],
#     "4": ['Pentium G3220', 8, 2100],
#     "5": ['Core-i5-4350', 5, 6500]
# }

# d = {i: input("-> ") for i in ["N", "S", "E", "W"]}
# print(d)
# for i, j in d.items():
#     print(i, ":", int(j))
#     # a = int(j)
#     # print(type(a))

# d = {'N': '3056', 'S': '8463', 'E': '8441', 'W': '2694'}
b_dict = {}
for name in ["John", "Tom"]:    # , "Anne", "Fiona"
    b_dict[name] = {ir: int(input("-> ")) for ir in ["N", "S"]}   # ["N", "S", "E", "W"]
    print(name, end="\n")

    # for i, j in b_dict.items():
    #     print(i, ":", j)
    #     # a = int(j)
    #     print(type(j))

print(b_dict, end="\n\n")
for i, j in b_dict.items():
    print(i, ":", j)
    for r, t in j.items():
        print(r, ":", t)
    # a = int(j)
    # print(type(j))


# d = {1: "one", 2: "two", 3: "three"}
# print(d.items())
# print(d)


# a = {int(input("-> ")) for i in &&&}
# print(a)

# for i in goods:
#     print(i, ")", goods[i][0], " - ", goods[i][1], " по ", goods[i][2], "руб.", sep="")
#
# while True:
#     n = input("№: ")
#     if n == "0":
#         break
#     else:
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input("Количество: "))
#                     goods[n][1] += count
#                     break
#                 except ValueError:
#                     print("Значение не корректно. Введите число")
#         else:
#             print("Такого ключа не существует")
#
# for i in goods:
#     print(i, ")", goods[i][0], " - ", goods[i][1], " по ", goods[i][2], "руб.", sep="")