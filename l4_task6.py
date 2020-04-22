"""6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools."""

from itertools import count, cycle

for itm in count(10):
    if itm > 100:
        break
    print(itm)

c = 0
for per in cycle('A1B2C3'):
    if c > 50:
        break
    print(per)
    c += 1
