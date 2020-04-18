"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def my_func():
    try:
        a = int(input('enter first number:\n'))
        b = int(input('enter second number:\n'))
        result = a / b
    except ZeroDivisionError:
        return print('cannot divided by Zero')
    return result


test = my_func()
print(test)



