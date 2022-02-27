# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать
# данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма
# получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней
# прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.
import json
profit = {} #прибыль = выручка - издержки
pr = {}
prof = 0 #сумма прибылей всех компаний
prof_over = 0 #Средняя прибыль всех компаний
end_list = []
i = 0
with open('file_7.txt', 'r') as file:
    for line in file:
        name, own, debet, kredit = line.split() #склеим в словарик
        profit[name] = int(debet) - int(kredit) #словарь фирма-прибыль
        if profit.setdefault(name) >= 0: #если больше нуля, то прибыль есть и суммируем ко всем
            prof = prof + profit.setdefault(name) #собираем прибыли компаний
            i += 1
    if i != 0:
        prof_over = prof / i #средняя прибыль сумма всех прибылей/на кол-во компаний
        print(f'Средняя прибыль по всем компаниям составила {prof_over:.2f} рублей')
    else:
        print('Прибыли нет!!! Все фирмы отработали с убытком')
    pr = {'OVER:': round(prof_over)} #словарь со средней прибылью по всем (вместо средняя прибыль в ключе изменила
    # на англ OVER т.к. при создании JSON не читабельно выход, не красиво)
    print(pr)
    end_list.append(profit)
    end_list.append(pr)
    print('Прибыль каждой компании за отчетный период составила: ', end_list)

with open('file_7.json', 'w') as file_js:
    json.dump(end_list, file_js)
    js_str = json.dumps(end_list)
    print(f'Создан json файл в котором информация вида: \n {js_str}')
