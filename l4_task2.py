"""2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор."""

my_list = [5, 1, 16, 3, 15, 60]
print(my_list)

# new_list = [itm for itm in my_list]
# print(new_list)

for itm in my_list:
    for itm_2 in my_list:
        # if itm > itm_2:
        #     print(itm)
        #     break
        if itm_2 or itm:
            print(itm_2)
            break

