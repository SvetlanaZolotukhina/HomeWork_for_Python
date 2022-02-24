# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы). Нужно получить результат вычисления произведения
# всех элементов списка.
# Подсказка: использовать функцию reduce().
from functools import reduce
#первый вариант с прописанной заранее новой функцией
def new_func(x, y):
    return x * y
my_list = [i for i in range(100, 1001) if i % 2 == 0]
print(my_list)
increase = reduce(new_func, my_list)
print(increase)
#Второй вариант с Lambda функцией
increase_lambda = reduce(lambda a, b: a * b, my_list)
print(increase_lambda)
