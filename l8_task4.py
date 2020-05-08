"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники."""


class Warehouse:
    rack = []


class Equipment:
    color = 'grey'
    material = 'plastic'


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
    model = 'Sony'
    weight = 12
