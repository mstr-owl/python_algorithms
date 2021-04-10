"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from functools import wraps
from memory_profiler import memory_usage, profile
from pympler import asizeof
import copy

@profile
def my_func_1(list_arg):
    original_list = [i * 2 for i in list_arg]
    new_list = original_list
    del original_list
    return new_list


list_arg_2 = list(range(100000))
my_func_1(list_arg_2)


@profile
def my_func_2(list_arg):
    original_list = [i * 2 for i in list_arg]
    new_list = original_list
    del original_list
    del new_list
    new_list = []
    return new_list


my_func_2(list_arg_2)

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
# 29     23.5 MiB     23.5 MiB           1   @profile
# 30                                         def my_func_1(list_arg):
# 31     27.5 MiB      4.0 MiB      100003       original_list = [i * 2 for i in list_arg]
# 32     27.5 MiB      0.0 MiB           1       new_list = original_list
# 33     27.5 MiB      0.0 MiB           1       del original_list
# 34     27.5 MiB      0.0 MiB           1       return new_list
#
# Если использовать my_func_2, то в данном случаи при удалении ссылок на одно и тоже занчение, будет освобождаться память.

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
# 41     24.1 MiB     24.1 MiB           1   @profile
# 42                                         def my_func_2(list_arg):
# 43     27.4 MiB      3.3 MiB      100003       original_list = [i * 2 for i in list_arg]
# 44     27.4 MiB      0.0 MiB           1       new_list = original_list
# 45     27.4 MiB      0.0 MiB           1       del original_list
# 46     24.9 MiB     -2.5 MiB           1       del new_list
# 47     24.9 MiB      0.0 MiB           1       new_list = []
# 48     24.9 MiB      0.0 MiB           1       return new_list


def memory_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        func(*args, **kwargs)
        m2 = memory_usage()
        return m2[0] - m1[0]
    return wrapper


@memory_decorator
def my_list(list_arg):
    new_list = [i ** 2 for i in list_arg]
    return new_list


@memory_decorator
def my_generator(list_arg):
    for i in list_arg:
        yield i ** 2


list_arg_2 = list(range(1000))
print(my_list(list_arg_2))
print(my_generator(list_arg_2))
print()

# Исходя из полученны результатов видно, что функция которая использует генератор, не занимает больше памяти, чем было выделено при старте скрипта,
# в отличии от функции которая генерирует новый список.
# my_list
# 0.00390625
# my_generator
# 0.0

from pympler import asizeof
class Car:
    def __init__(self, mileage, miles):
        self._mileage = mileage
        self._miles = miles

    def res_mileage(self):
        result = self._mileage + self._miles
        print(f"Пробег автомобиля составляет: {result} киллометров.")


car1 = Car(23450, 2000)

print(f"Объект сar1 занимает {asizeof.asizeof(сar1)} в памяти.")


class Car2:
    __slots__ = ['_mileage', '_miles']
    def __init__(self, mileage, miles):
        self._mileage = mileage
        self._miles = miles

    def res_mileage(self):
        result = self._mileage + self._miles
        print(f"Пробег автомобиля составляет: {result} киллометров.")


car2 = Car2(23450, 2000)

print(f"Объект сar2 занимает {asizeof.asizeof(car2)} в пямяти.")

#Объект сar1 занимает 336 в памяти.
#Объект сar2 занимает 112 в пямяти.
#Если как в class Car2  отказаться от использования хэш таблиц для хранения атрибутов класса, можно получить приличную экономию памяти.