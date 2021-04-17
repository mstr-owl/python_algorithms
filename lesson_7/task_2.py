"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния, попробуйте предложить другой
(придумать или найти)

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
from random import uniform
from timeit import default_timer

def decorator_timer(func):
    def wrapper(*args, **kwargs):
        t1 = default_timer()
        result = func(args[0])
        t2 = default_timer()
        timer_res = '{:.16f}'.format(t2 - t1)
        print(f'Функция - {func.__name__}\nВремя заняло: {timer_res}\n')
        return result
    return wrapper

def merge(left, right):
    my_list = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            my_list.append(left[i])
            i += 1
        else:
            my_list.append(right[j])
            j += 1
    my_list += left[i:] + right[j:]
    return my_list


def merge_sort(left):
    if len(left) <= 1:
        return left
    else:
        Left = left[:len(left) // 2]
        Right = left[len(left) // 2:]
    return merge(merge_sort(Left), merge_sort(Right))

@decorator_timer
def call_func(list_obj):
    return merge_sort(list_obj)

count_elem = int(input("Введите число элементов: "))
list_obj = [uniform(1, 50) for _ in range(count_elem)]

print(f"Исходный массив: {list_obj}")
print(f"Отсортированный массив: {call_func(list_obj)}")

list_obj_10 = [uniform(1, 50) for _ in range(10)]
list_obj_100 = [uniform(1, 50) for _ in range(100)]
list_obj_1000 = [uniform(1, 50) for _ in range(1000)]

print()
print('Замеры для 10 элементов массива\n')
call_func(list_obj_10)
print()
print('Замеры для 100 элементов массива\n')
call_func(list_obj_100)
print()
print('Замеры для 1000 элементов массива\n')
call_func(list_obj_1000)

# Исходный лист - [25.563536518387007, 11.24236882279442, 28.12504277225865, 19.555098311167118, 15.290233657713152]
# Функция - call_func
# Время заняло: 0.0000119000000001

# Отсортированный лист- [11.24236882279442, 15.290233657713152, 19.555098311167118, 25.563536518387007, 28.12504277225865]

# Замеры для 10 элементов массива
# Функция - call_func
# Время заняло: 0.0000310999999997
#
# Замеры для 100 элементов массива
# Функция - call_func
# Время заняло: 0.0003742000000000
#
# Замеры для 1000 элементов массива
# Функция - call_func
# Время заняло: 0.0024202000000000
