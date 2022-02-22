# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму
# наибольших двух аргументов.
def my_sum_max(a, b, c):
    if a < b and a < c:
        return b + c
    if b < a and b < c:
        return a + c
    if c < a and c < b:
        return a + b
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
print('Сумма двух наибельших, из введенных Вами чисел, равна:  ', my_sum_max(a, b, c))
