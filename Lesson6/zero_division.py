try:
    print(7/0)
except ZeroDivisionError:
    print('Ошибка')


while True:
    first = input('Введи число: ')
    if first == 'q':
        break
    second = input('Введи число: ')
    if second == 'q':
        break
    try:
        answer = int(first) / int(second)
    except ZeroDivisionError:
        print('Ошибка деления на ноль')
    except ValueError:
        print('Вы ввели не число')
    except TypeError:
        print('Вы ввели не целое число')
    else:
        print(answer)