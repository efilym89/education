# Создаем наш первый декоратор
# Определили назвавние декоратора как my_first_decoration,
# в нее передаем некую функцию, которую нам нужно будет задекорировать.


def my_first_decoration(my_function):
    # Поместили в декоратор функцию обертку, которая будет содержать код до и после
    # выполнения оборачиваемой функции
    def function_inside_decoration():

        print('any code before')

        my_function()

        print('any code after')
    # Вернули функцию обертку без значения, то есть без ()
    return function_inside_decoration


# Вызываем наш декоратор к функции которую хотим обернуть
@my_first_decoration
def my_first_function():
    print('Hello World!')


# Вызываем задекарированную функцию для проверки
print(my_first_function())


# Пробуем делать декотатор с функцией,
# которая будет принимать неопределенное количество аргументов.

def my_second_decoration(function):
    # Делаем функцию обертку, которая принимает неопределенное количество аругументов
    def wrapper_function(*args, **kwargs):
        # Выводим код, который будет выполнятся до выполнения оборачиваемой функции
        print('We accepted', *args, **kwargs)
        # Выполняем оборачиваемую функцию с принятыми аргументами переданную в декоратор
        function(*args)
        # Выводим код, который будет выполнятся после оборачиваемой функции
        print('Code, before function')
    # Возвращаем функию обертку без значений ()
    return wrapper_function


# Тестируем работу декоратора на примере фенкции test_decoration_function
@my_second_decoration
def test_decoration_function(first_arg, second_arg):
    print('Full name', first_arg, second_arg)


print(test_decoration_function('John', 'Smith'))


# Напишем декторатор определяющий затраченное время на выполние функции
import time


def third_decoration(f):
    def wrapper_function(*args, **kwargs):
        # Делаем переменную start_time, которая определяет время начала
        start_time = time.time()
        # Переменная result которая является нашей функцией с принятыми аргументами
        result = f(*args, **kwargs)
        # Переменная tmp высчитывает разницу между временем начала выполнения функии и временем конца
        tmp = time.time() - start_time
        # % это форматированнный вывод который ждет какую то переменную,
        # этой переменной будет tmp. Выводим разницу
        print('time take to complete %f' % tmp)
        # Возвращаем функции оберки значения оборачиваемой функции
        return result
    # Возвращаем функции декоратору, функцию оберки
    return wrapper_function


# Тестируем декоратор, применив его к нашей функции test_decoration
@third_decoration
def test_decoration(x, y, c):
    return x + y * c


print(test_decoration(5, 3, 7))


# Запишем декоратор, который будет вести лог по заданным параметрам

def logger(function):
    def my_logger(*args, **kwargs):
        result = function(*args, **kwargs)
        # Открываем файл на дозапись, когда предыдущий результат не удаляется, а добавляется в конец файла
        with open('log_file.txt', 'a') as f:
            # Делаем запись данных в файл
            f.write(
                # Запись в файл лога производим методом форматирования строки .format,
                # подставляя в нее данные полученные в процессе выполнения программы
                'function name: {function_name} with result = {result}. Start at {start_time}\n'.format(
                    # Определяяем значение переменных в строке.
                    function_name=function.__name__, result=result, start_time=time.ctime(time.time())
                )
            )
            f.close
            return result

    return my_logger


@logger
def test_decoration_two(x, y, c):
    return x + y * c


print(test_decoration_two(4, 7, 9))
