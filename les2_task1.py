import random
print('Программа приветсвует Вас в Казино, ваш депозит составляет 10000 рублей')
deposit = 10000
journal = []
while deposit > 0:
    kubik = random.randint(2,12)
    stavka = int(input('Попробуй угадать результат броска двух кубиков: '))
    if stavka <= 12 and stavka >= 2:
        if kubik == stavka:
            deposit += 1000
            print(f'Угадал, игра загадала {kubik}, моя попытка {stavka},на счету {deposit} рублей')
            journal.append(f'Угадал, игра загадала {kubik}, моя попытка {stavka},на счету {deposit} рублей')
        elif kubik != stavka:
            deposit -= 1000
            print(f'Не угадал, игра загадала {kubik}, моя попытка {stavka},на счету {deposit} рублей')
            journal.append(f'Не угадал, игра загадала {kubik}, моя попытка {stavka},на счету {deposit} рублей')
    else:
        print('Введите число от 2 до 12')
print(f'На вашем депозите осталось {deposit} рублей')
for elem in range(len(journal)):
    print(journal[elem])
    elem += 1