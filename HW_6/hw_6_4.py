# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
# turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f'{self.name} выехала'
    def stop(self):
        return f'{self.name} остановилась'
    def turn_left (self):
        return f'{self.name} повернула налево'
    def turn_right (self):
        return f'{self.name} повернула направо'
    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость {self.name} превышает допустимую для данного типа транспорта.')
        else:
            print(f'Скорость {self.name} в норме.')
        return f'Текущая скорость {self.name} равна {self.speed}'
class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Текущая скорость городского автомобиля {self.name} равна {self.speed}')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        print(f'Текущая скорость рабочего автомобиля {self.name} равна {self.speed}')
        if self.speed > 40:
            print(f'Скорость {self.name} ПРЕВЫШАЕТ допустимую для данного типа транспорта.')
        else:
            print(f'Скорость {self.name} в норме.')
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        if self.is_police:
            print(f'{self.name} принадлежит депортаменту полиции')
        else:
            print(f'{self.name} НЕпринадлежит депортаменту полиции')
bmv = SportCar(145, 'Red', 'BMV', False)
polic = PoliceCar(90, 'Blue', 'GEELY', True)
ford = TownCar(45, 'Black', 'FORD', False)
opel = WorkCar(75, 'GREEN', 'OPEL', False)
print(opel.go)
print(opel.stop())
print(ford.turn_left())
print(bmv.turn_right())
print(polic.is_police)
print(opel.show_speed())
print(ford.show_speed())
