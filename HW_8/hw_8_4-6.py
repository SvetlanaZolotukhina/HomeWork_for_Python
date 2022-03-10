# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.
#
# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).
#
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
#______________________________________________________________________________
#т.к. вариант с автоматическим счетчиком как Id мы уже проработали на лекции, то здесь для разнообразия возьму
# серийный номер, обычно он из книг учета на предприятиях берется... А вот дату попробую взять автоматически
from datetime import datetime

class Depot: #склад
    def __init__(self, title):
        self.title = title
        self.lists = {} #склад 1
        self.give_lists = {} #склад 2

    def take_to_depot(self, equipment):
# внесение в словарь название оборудования, серийный номер и время передачи на склад1
        t = datetime.now()
        self.lists.update({equipment.serial_number:[equipment.title, self, t]})
        print('На склад '+self.title+' получено оборудование:' + '' +equipment.title+' ,серийный номер - '+ str(equipment.serial_number)+', Дата:'
              + str(t.day)+'.'+str(t.month)+'.'+str(t.year))

    def give_to_depot(self, equipment, other):
# передача оборудование на другой склад2
        t = datetime.now()
        self.give_lists.update({equipment.serial_number: [equipment.title, other, t]})
        print('Передано оборудование:' + '' + equipment.title + ' ,серийный номер - ' + str(
            equipment.serial_number) + ', Дата:'
              + str(t.day) + '.' + str(t.month) + '.' + str(t.year))
        other.take_to_depot(equipment)

    def list_equipments(self): #статистика по складу
        print('На склад '+ self.title + ' получено оборудование:')
        print(self.lists)
        print('Общее количество: ', len(self.lists))
        print('Со склада '+ self.title + ' выдано оборудование:')
        print(self.give_lists)
        print('Общее количество: ', len(self.give_lists))

class Office_equipment: #Оргтехника
    def __init__(self, title, serial_number):
        self.title = title
        self.serial_number = serial_number

    def __str__(self):
        return str(self.title)

class Printer(Office_equipment):
    def __init__(self, title, serial_number, print_velocity):
        Office_equipment.__init__(self, title, serial_number)
        self.print_velocity = print_velocity

    def to_print(self):
        return f'Я принтер {self.title}, я могу распечатать'

    def __str__(self):
        return  'Название модели:'+Office_equipment.__str__(self) + ' ,Параметры: ' +str(self.print_velocity)

class Scanner(Office_equipment):
    def __init__(self, title, serial_number, resolution):
        Office_equipment.__init__(self, title, serial_number)
        self.resolution = resolution

    def to_scan(self):
        return f'Я сканер {self.title}, я могу отсканировать'

    def __str__(self):
        return 'Название модели:'+Office_equipment.__str__(self) + ' ,Параметры: ' + str(self.resolution)

class Copier(Office_equipment):
    def __init__(self, title, serial_number, addit):
        Office_equipment.__init__(self, title, serial_number)
        self.addit = addit

    def to_copier(self):
        return f'Я копир {self.title}, я могу сделать копии документа'

    def __str__(self):
        return 'Название модели:'+Office_equipment.__str__(self) + ' ,Параметры: ' + str(self.addit)

store1 = Depot('Main warehouse')
store2 = Depot('Small warehouse')
a = Printer('HP', 100002, 250)
b = Scanner('Epson', 100258, 400)
c = Copier('Brother', 200298, 500)
d = Printer('HP', 369147, 200)
print(a)
print(b)
print(c)
store1.take_to_depot(a)
store1.take_to_depot(b)
store1.take_to_depot(c)
store1.take_to_depot(d)
store1.give_to_depot(a, store2)
store2.list_equipments()
print(store1.list_equipments())
print(a.to_print())
