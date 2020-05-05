"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники."""


class Warehouse:
    def __init__(self, city, area, worker):
        self.cite = city
        self.area = area
        self.worker = worker


class Equipment:
    def __init__(self, color, material):
        self.color = color
        self.material = material


class Printer(Equipment):
    name = 'Printer'
    model = 'Sumsung'
    weight = 5


class Scan(Equipment):
    name = 'Scan'
    model = 'Epson'
    weight = 3


class Xerox(Equipment):
    name = 'Xerox'
    name = 'Sumsung'
    weight = 12


def enter(*args, **kwargs):


