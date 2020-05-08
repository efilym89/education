"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

with open('file_task_4.txt') as file:
    lines = file.readlines()
    result_1, result_2 = [], []
    for itm in lines:
        my_list = itm.split(' ')
        result_1.append(my_list[0])
        result_2.append(int(my_list[2]))

    my_dict = dict(zip(result_1, result_2))













