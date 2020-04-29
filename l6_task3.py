"""Реализовать базовый класс Worker (работник), в котором определить
атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров)."""


class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = dict(_income)


class Position(Worker):
    def get_full_name(self):
        return print(self.name, self.surname)

    def get_total_income(self):
        result = sum(self._income.values())
        return result


inc = Position(name='Brat', surname='Pitt', position='actor', _income={'wage': 5000, 'bonus': 500})


"""Вариант решения номер 2"""


# class Worker:
#     name = 'Brat'
#     surname = 'Pitt'
#     position = 'actor'
#     _income = {'wage': 5000, 'bonus': 500}
#
#
# class Position(Worker):
#     def get_full_name(self):
#         return print(self.name, self.surname)
#
#     def get_total_income(self):
#         result = sum(self._income.values())
#         return result
#
#
# inc = Position()


print('1')