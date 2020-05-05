"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать
дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц,
год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных."""


class Date:
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def my_method(cls, param):
        day, month, year = map(int, param.split('-'))
        return day, month, year

    @staticmethod
    def valid(date_as_str):
        day, month, year = map(int, date_as_str.split('-'))
        return day <= 31, month <= 12, year <= 2021


my_date = Date.my_method('12-02-2020')
my_valid = Date.valid('12-02-2020')

print(my_date)
print(my_valid)
