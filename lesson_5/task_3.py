"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

Операции равные по семантике (по смыслу)
Но разные по используемым ф-циям

И добавить аналитику, так ли это или нет.!
"""
from timeit import timeit
from random import randint
from collections import deque

my_list = [randint(1, 100000) for i in range(1000000)]
my_deque = deque(my_list)

def list_insert_left(my_lst):
    my_lst.insert(0, 10)
    return my_lst


def deque_insert_left(my_deq):
    my_deq.appendleft(10)
    return my_deq


def list_pop_left(my_lst):
    my_lst.pop(0)
    return my_lst


def deque_pop_left(my_deq):
    my_deq.popleft()
    return my_deq


def list_get(my_lst):
    return my_lst[999000]


def deque_get(my_deq):
    return my_deq[999000]


print(timeit('list_insert_left(my_list)', 'from __main__ import list_insert_left, my_list', number=100000))

print(timeit('deque_insert_left(my_deque)', 'from __main__ import deque_insert_left, my_deque', number=100000))

print(timeit('list_pop_left(my_list)', 'from __main__ import list_pop_left, my_list', number=100000))

print(timeit('deque_pop_left(my_deque)', 'from __main__ import deque_pop_left, my_deque', number=100000))

print(timeit('list_get(my_list)', 'from __main__ import list_get, my_list', number=100000))

print(timeit('deque_get(my_deque)', 'from __main__ import deque_get, my_deque', number=100000))
# Добавление элемента
# 90.1917588
# 0.007334000000000174
# Удаление элемента
# 71.2818929
# 0.006705299999993031
# Получение элемента
# 0.00659930000000486
# 0.00745200000000068

# Как мы видим из полученных результатов, теория в документациях python полностью потверждается на практике.
# Добавление и удаление в deque происходит значительно быстрее, чем в list. А вот получение элементов в list работает незначительно, но все таки быстрее, чем в deque.