"""5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить
сумму этих чисел к полученной ранее сумме и после этого завершить программу."""


def insetr_sum(*args):
    result = 0
    exit_flag = False
    try:
        for itm in args:
            result += float(itm) if itm else 0
    except ValueError:
        exit_flag = not exit_flag
    return result, exit_flag


user_sum = 0
while True:
    user_input = input('enter numbers:\n').split(' ')
    result_sum, user_exit = insetr_sum(*user_input)
    user_sum += result_sum
    print(f'sum: {user_sum}')

    if user_exit:
        print('good buy')
        break
