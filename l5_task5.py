"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

file = open('file_task_5.txt', 'w')
file.write('2 3 4 4 5 7 7')

with open('file_task_5.txt') as file:
    for line in file:
        my_list = line.split(' ')
        print(sum([sum(map(int, i)) for i in my_list]))














