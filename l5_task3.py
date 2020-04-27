"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

with open('file_task_3.txt') as file:
    lines = file.readlines()
    result_1, result_2 = [], []
    for itm in lines:
        my_list = itm.split(' ')
        result_1.append(my_list[0])
        result_2.append(int(my_list[1]))

    my_dict = dict(zip(result_1, result_2))

    for key, values in my_dict.items():
        if values <= 20000:
            print(key)

    average = sum(result_2)/len(result_1)
    print('average earnings per employee', average, '$')













# file = open('file_task_3.txt', 'r')
# lines = file.readlines()
#
# for itm in lines:
#     print(itm.split(' '))
#
# list_1 = itm[0]
# list_2 = itm[1]
#
# print(list_1)
#
# file.close()


