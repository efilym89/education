"""1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка."""

file = open('my_file.txt', 'w')
file.write(input())
file.close()
