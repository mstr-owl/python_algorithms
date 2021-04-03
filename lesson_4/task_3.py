"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему!!!

И можете предложить еще свой вариант решения!
Без аналитики задание считается не принятым
"""
import cProfile
import timeit

def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

def revers_4(enter_num):
    revers_list = list(reversed(str(enter_num)))
    return ''.join(revers_list)

enter_num = 1234567890

print('№1- ', timeit.timeit('revers_1(enter_num)', 'from __main__ import revers_1, enter_num', number=1000))
print('№2- ', timeit.timeit('revers_2(enter_num)', 'from __main__ import revers_2, enter_num', number=1000))
print('№3- ', timeit.timeit('revers_3(enter_num)', 'from __main__ import revers_3, enter_num', number=1000))
print('№4- ', timeit.timeit('revers_4(enter_num)', 'from __main__ import revers_4, enter_num', number=1000))
print('reverse_1')
cProfile.run('revers_1(enter_num)')
print('reverse_2')
cProfile.run('revers_2(enter_num)')
print('reverse_3')
cProfile.run('revers_3(enter_num)')
print('reverse_4')
cProfile.run('revers_4(enter_num)')

# cProfile не показал разницы между функциями, везде по нулям.
# А вот timeit показывает разницу во времени выпоненения между функциями, самая эффективная получается функция №3, где используется срез.
# На втором месте идет функция №4 с реверсом списка, на 3 и 4 месте соответсвенно идут функция №2 с циклом и функция №1 с рекурсией.
# Функция №1 с рекурсией наименее эффективный способ.
# №1-  0.0018559000000000006
# №2-  0.001243499999999998
# №3-  0.0002682999999999991
# №4-  0.0005600000000000015