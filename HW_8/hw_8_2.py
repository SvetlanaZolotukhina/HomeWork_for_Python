# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и
# не завершиться с ошибкой.

class DivisionByZero(Exception):
    def __init__(self, div, den):
        self.div = div
        self.den = den
    def divide_by_zero(div, den):
        try:
            if den == 0:
                raise MyError('Деление на ноль недопустимо!!!')
        except ValueError:
            print('Вы ввели не число')
        except DivisionByZero as err:
            print(err)
        else:
            print(f'Все хорошо, считаем')
            return div / den

a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))
print(DivisionByZero.divide_by_zero(a, b))
