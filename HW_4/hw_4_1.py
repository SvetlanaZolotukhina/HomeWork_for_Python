# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во время выполнения расчёта для конкретных
# значений необходимо запускать скрипт с параметрами.
from sys import argv
print(argv)
worker_name = argv[1]
work_time = float(argv[2])
price_time = float(argv[3])
bonus = float(argv[4])
pay = work_time * price_time + bonus
print(f'ФИО сотрудника: {worker_name}')
print(f'Отработана часов за месяц: {work_time}')
print(f'Ставка в USD за один час работы: {price_time}')
print(f'Премия за месяц для данного сотрудника: {bonus}')
print(f'В этом месяце {worker_name} получит заработную плату в размере {pay} у.е.')
