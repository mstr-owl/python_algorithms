"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from timeit import timeit
from collections import OrderedDict


def dict_fill(my_dict):
    my_dict = {k: k**2 for k in range(100000)}
    return my_dict


def dict_search(my_dict):
    return my_dict[9000]


def dict_delete(my_dict):
    my_dict = {k: k ** 2 for k in range(100000)}
    for i in range(1000, 90000):
        my_dict.pop(i)
    return my_dict


my_dict = {}
ord_dict = OrderedDict()

print(timeit('dict_fill(my_dict)', 'from __main__ import dict_fill, my_dict', number=100))
print(timeit('dict_fill(ord_dict)', 'from __main__ import dict_fill, ord_dict', number=100))

my_dict = dict_fill(my_dict)
ord_dict = dict_fill(ord_dict)

assert list(my_dict.items()) == list(ord_dict.items())

print('{:.16f}'.format(timeit('dict_search(my_dict)', 'from __main__ import dict_search, my_dict', number=100,)))
print('{:.16f}'.format(timeit('dict_search(ord_dict)', 'from __main__ import dict_search, ord_dict', number=100,)))

print(timeit('dict_delete(my_dict)', 'from __main__ import dict_delete, my_dict', number=100))
print(timeit('dict_delete(ord_dict)', 'from __main__ import dict_delete, ord_dict', number=100))

# Использование OrderedDict в версиях 3.6 и старше смысла не имеет смысла, обычный dict уже сохраняет начальный порядок элементов в словаре.
# Исходя из полученных реззультатов видно, что по скорости работы OrderedDict ни чем не лучше обычного dict, а иногда даже уступает dict.
# 2.6438192
# 2.650942
# 0.0000109999999998
# 0.0000095000000000
# 3.481204
# 3.4244700000000012
