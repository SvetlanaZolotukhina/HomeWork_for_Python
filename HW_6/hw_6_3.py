# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и
# премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
# дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров.
incom = {"wage": 1500, "bonus": 200}
class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._incom = {"Оклад": wage, "Премия": bonus}
class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname
    def get_total_income(self):
        return f'Доход указанного сотрудника составляет: {sum(self._incom.values())} у.е.'
my_worker = Position('Светлана', 'Золотухина', 'Директор', 1500, 200)
print(my_worker.get_full_name())
print(my_worker.position)
print(my_worker._incom)
print(my_worker.get_total_income())
