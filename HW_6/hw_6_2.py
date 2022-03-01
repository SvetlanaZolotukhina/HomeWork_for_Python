# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.
class Road:
    def __init__(self, _length, _width): #длина и ширина дороги
        self._length = _length
        self._width = _width
    def square(self):
        return self._length * self._width #площадь дорожного полотна
class MassaCount(Road):
    def __init__(self, _length, _width, _volume, _high):
        super().__init__(_length, _width)
        self._volume = _volume
        self._high = _high
    def massa(self):
        return (self._length * self._width * self._volume * self._high) / 1000  # Масса асфальта в тоннах
r = MassaCount(20, 5000, 25, 5) #  длина в М * ширина в М * масса в КГ * высота в СМ
print(f'По заданным вами параметрам вам потребуется {r.massa()} тонн асфальта')
