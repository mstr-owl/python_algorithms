"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1

Предприятия, с прибылью ниже среднего значения: Фирма_2
"""

from collections import namedtuple

count_company = int(input("Введите количество предприятий для расчета прибыли: "))
generalis_count  = 1
new_list_company = []
while generalis_count <= count_company:
    comp = namedtuple('Company', 'name income')
    generalis_count += 1
    company_name = input('Введите название предприятия: ')
    company_profit = input('через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ')
    new_list_company.append(comp(
        name=company_name,
        income=company_profit.split()
    ))

generalis_sum = 0
for i in new_list_company:
    generalis_sum += sum(int(j) for j in i.income)

high_profit = []
low_profit = []

for i in new_list_company:
    if sum([int(j) for j in i.income]) > generalis_sum / count_company:
        high_profit.append(i.name)
    else:
        low_profit.append(i.name)

average_profit = round((generalis_sum / count_company), 2)
print(f'Средняя годовая прибыль всех предприятий: {average_profit}')
print(f'Предприятия, с прибылью выше среднего значения: {high_profit}')
print(f'Предприятия, с прибылью ниже среднего значения: {low_profit}')


