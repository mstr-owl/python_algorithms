"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в
виде функции.

Обязательно доработайте алгоритм (сделайте его умнее)!

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
from random import randint
from timeit import default_timer

def decorator_timer(func):
    def wrapper(*args, **kwargs):
        t1 = default_timer()
        res = func(args[0])
        t2 = default_timer()
        timer_res = '{:.16f}'.format(t2 - t1)
        print(f'Функция - {func.__name__}\nВремя заняло: {timer_res}\n')
        return res
    return wrapper

@decorator_timer
def bubble_original(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] > lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj

@decorator_timer
def bubble_reverse(lst_obj):
    n = len(lst_obj)
    while n > 1:
        for i in range(len(lst_obj) - 1, len(lst_obj) - n, -1):
            if lst_obj[i] < lst_obj[i - 1]:
                lst_obj[i], lst_obj[i - 1] = lst_obj[i - 1], lst_obj[i]
        n -= 1
    return lst_obj

@decorator_timer
def bubble_reverse_mod(lst_obj):
    n = len(lst_obj)
    while n > 1:
        flag = 0
        for i in range(n - 1):
            if lst_obj[i] > lst_obj[i + 1]:
                flag = 1
        if flag == 0:
            break
        for i in range(len(lst_obj) - 1, len(lst_obj) - n, -1):
            if lst_obj[i] < lst_obj[i - 1]:
                lst_obj[i], lst_obj[i - 1] = lst_obj[i - 1], lst_obj[i]
        n -= 1
    return lst_obj


print('Замеры для 10 элементов массива\n')
my_list = [randint(-100, 100) for _ in range(10)]
print(f'Исходный массив: {my_list}')
print(f'Отсортированный массив: {bubble_reverse(my_list)}')
bubble_original(my_list[:])
bubble_reverse(my_list[:])
bubble_reverse_mod(my_list)[:]
print()
print('Замеры для 100 элементов массива\n')
my_list2 = [randint(-100, 100) for _ in range(100)]
bubble_original(my_list2[:])
bubble_reverse(my_list2[:])
bubble_reverse_mod(my_list2[:])
print()
print('Замеры для 1000 элементов массива\n')
my_list3 = [randint(-100, 100) for _ in range(1000)]
bubble_original(my_list3[:])
bubble_reverse(my_list3[:])
bubble_reverse_mod(my_list3[:])

# Замеры для 10 элементов массива
# Исходный массив: [-13, 57, -31, -46, 65, 39, -50, 87, 27, 68]
# Отсортированный массив: [-50, -46, -31, -13, 27, 39, 57, 65, 68, 87]
#
# Функция - bubble_original
# Время заняло: 0.0000155000000000
# Функция - bubble_reverse
# Время заняло: 0.0000140000000000
# Функция - bubble_reverse_mod
# Время заняло: 0.0000036000000000
#
#
# Замеры для 100 элементов массива
# Функция - bubble_original
# Время заняло: 0.0011425000000000
# Функция - bubble_reverse
# Время заняло: 0.0011194000000000
# Функция - bubble_reverse_mod
# Время заняло: 0.0019032000000000
#
#
# Замеры для 1000 элементов массива
# Функция - bubble_original
# Время заняло: 0.0757831000000000
# Функция - bubble_reverse
# Время заняло: 0.0779659000000000
# Функция - bubble_reverse_mod
# Время заняло: 0.1009599000000000
#
# Модификация заключается в добавление флага равного нулю, если в массиве происходит хотя бы одна перестановка, то тогда значение флага переходит в значение 1,
# если флаг остается в позиции 0, тогда значит массив уже отсортирован.
# Из полученных результатов видно, что данная модификация не дает каких-либо преймуществ по времени в не отсортированном массиве.