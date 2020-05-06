"""5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce()."""

from functools import reduce

my_list = []

start = 100
stop = 1000
step = 1
stop = stop + step

for itm in range(start, stop, step):
    if itm % 2 == 0:
        my_list.append(itm)

print(my_list)

sum_all = reduce(lambda x, y: x + y, my_list)
print(sum_all)

