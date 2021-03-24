"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать где какая сложность.

Примечание:
Построить список можно через списковое включение.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""

from random import randint

def min_list_1(lst): # O(n^2)-Квадратичная
    min_num = lst[0]
    for i in lst: # O(n)-Линейная
        for j in lst: # O(n)-Линейная
            if i < j and i < min_num: # О(1)-Константная
                min_num = i
    return min_num

def min_list_2(lst): # O(n)-Линейная
    min_num = lst[0]
    for i in lst: # O(n)-Линейная
        if i < min_num: # О(1)-Константная
            min_num = i
    return min_num

lst_res = [randint(0,100) for i in range(10)]
print(lst_res)
print(min_list_1(lst_res))
print(min_list_2(lst_res))