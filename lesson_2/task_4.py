"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак
"""
def function_recursion(counter, number, number_count, sum_number):
    if counter == number_count:
        print(f"Количество элементов: {number_count}, их сумма - {sum_number}")
    elif counter < number_count:
        return function_recursion(counter + 1, number / 2 * -1, number_count, sum_number+number)

n = int(input("Введите количество элементов: "))
function_recursion(0, 1, n, 0)

