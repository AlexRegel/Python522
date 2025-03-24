# import random
from random import randint


def fl_tpl_int(a_, b_, rng):
    tp_ = tuple(randint(a_, b_) for i in range(rng))
    return tp_


tpl_1 = fl_tpl_int(0, 5, 10)
print(tpl_1)
tpl_2 = fl_tpl_int(-5, 0, 10)
print(tpl_2)
tpl_3 = tpl_1 + tpl_2
print(tpl_3)
print("0 =", tpl_3.count(0))

