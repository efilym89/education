# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

season = {'winter': (12, 1, 2),
          'spring': (3, 4, 5),
          'summer': (6, 7, 8),
          'autumn': (9, 10, 11),
          }

push = int(input('enter month number:\n'))

for key, value in season.items():
    if push in value:
        print(key)
        break


push = int(input('enter month number:\n'))

seas_list = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

while True:
    if push in seas_list[0:3]:
        print('winter')
        break
    elif push in seas_list[3:6]:
        print('spring')
        break
    elif push in seas_list[6:9]:
        print('summer')
        break
    elif push in seas_list[9:12]:
        print('autumn')
        break
    else:
        print('enter again')
        break