# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся
# пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть
# обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Cloth(ABC):
    @abstractmethod
    def consumption(self):
        pass

class Coat(Cloth):
    def __init__(self, width):
        self.width = width

    @property
    def consumption(self):
        return self.width / 6.5 + 0.5

    def sum_cosumption(self, all_c):
        n = 0
        for coat in all_c:
            n += coat.consumption
        return n

class Jacket(Cloth):
    def __init__(self, high):
        self.high = high

    @property
    def consumption(self):
        return self.high * 2 + 0.3

    def sum_cosumption(self, all_j):
        n = 0
        for jacket in all_j:
            n += jacket.consumption
        return n

coat = Coat(48)
coat_red = Coat(54)
jacket = Jacket(1.8)
jacket_green = Jacket(1.65)
all_coat = [coat, coat_red]
all_jacket = [jacket_green, jacket]
# Не люблю числа с плавающей точкой, поэтому использую int (личная неприязнь :) )
print(f'Для пошива красного пальто нужно ткани : {int(coat_red.consumption)} Метров')
print(f'Для пошива розового пальто нужно ткани : {int(coat.consumption)} Метров')
print(f'Для пошива зеленого кастюма нужно ткани : {int(jacket_green.consumption)} Метров')
print(f'Для пошива кастюма нужно ткани : {int(jacket.consumption)} метров')
print(f'Для пошива двух (в данном случае) пальто нужно ткани : {int(coat.sum_cosumption(all_coat))} метров')
print(f'Для пошива двух кастюмов нужно ткани : {int(jacket.sum_cosumption(all_jacket))} Метров')
