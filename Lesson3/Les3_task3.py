import random as ran # Подключаем библиотеку random, сокращаем ее название до ran
speech_1 = ['Коллеги,', 'В то же время,', 'Однако,', 'Тем не менее,', 'Следовательно,', 'Соответственно,', 'Вместе с тем,', 'С другой стороны,']
speech_2 = ['парадигма цифровой экономики', 'контекст геймификации', 'дижитализация бизнес-процессов', 'прагматичный подход к облачным платформам', 'совокупность сквозных технологий', 'программа прорывных исследований', 'ускорение блокчейн-транзакций', 'экспоненциальный рост Big Data']
speech_3 = ['открывает новые возможности для', 'выдвигает новые требования', 'несет в себе риски', 'расширяет горизонты', 'заставляет искать варианты', 'не оставляет шанса для', 'повышает вероятность', 'обостряет проблему']
speech_4 = ['дальнейшего углубления', 'бюджетного финансирования', 'синергетического эффекта', 'компроментации конфиденциальных', 'несанкционированной кастомизации', 'нормативного регулирования', 'практического применения']
speech_5 = ['знаний и компетенций.', 'непроверенных гипотез.', 'волатильных активов.', 'опасных экспериментов.', 'государственно-частных партнеров.', 'цифровых следов граждан.', 'нежелательныхпоследствий.', 'случайных открытий.']
# задаем необходимые переменные
active = True
final_speech = []
chislo_speech = ran.randint(5, 10) # Задаем случайное число готовых речей в диапазое от 5 до 10
chislo = 1
while active:
    if chislo <= chislo_speech:
        # Собирай речь из пяти списков
        final_speech.append(f'{speech_1[ran.randint(0, len(speech_1) - 1)]} {speech_2[ran.randint(0, len(speech_2) - 1)]} {speech_3[ran.randint(0, len(speech_3) - 1)]} {speech_4[ran.randint(0, len(speech_4) - 1)]} {speech_5[ran.randint(0, len(speech_5) - 1)]}')
        chislo += 1
    elif chislo > chislo_speech:
        active = False
for elem in range(len(final_speech)):
    print(final_speech[elem]) # Выводим готовые речи
