"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна
корректно обработать эту ситуацию и не завершиться с ошибкой."""


class OwnError(Exception):
    def __init__(self, text):
        self.text = text


try:
    a = int(input('num_1:\n'))
    b = int(input('num_2\n'))
    if b == 0:
        raise OwnError('На 0 делить нельзя!')
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Результат деления: {a / b}")
