"""2. Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой."""


def person_param():
    name = input('enter your name:\n')
    fname = input('enter you first name:\n')
    bd = input('enter you birthday:\n')
    lici = input('enter you live city:\n')
    email = input('enter you email:\n')
    tel = input('enter you tel. number:\n')
    full_info = f'{name},{fname} born {bd},live in city {lici}, {email}, {tel}'
    return full_info


test = person_param()
print(test)
