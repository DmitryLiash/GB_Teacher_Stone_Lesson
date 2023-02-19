def RandomCreate():
    import random
    try:
        minValue = int(input("Введите минимальное значение для рандома: "))
        maxValue = int(input("Введите максимальное значение для рандома: "))
        randomValue = random.randint(minValue, maxValue)
        return randomValue
    except:
        print('ошибка')
        return RandomCreate()
        
        
def Serch(randomValue):
    count = 0
    levels = {1: 10, 2: 5, 3 : 3}
    nameUsers = []
    winner = False
    winnerName = None
    enterLvl = int(input("введите уровень 1 - 10 попыток. 2 - 5 попыток. 3 - 3 попытки: "))
    maxCount = levels[enterLvl]
    countOfUsers = int(input('Введите колличесво пользователей: '))
    for i in range(countOfUsers):
        nameUsers.append(str(input('Введите имя пользователя № {} : '.format(i + 1))))
    print("Игра угадайка - введи число от 1 до 100")
    try:
        while not winner:
            count += 1
            if count > maxCount:
                print("Использовано {} попыток. Все проиграли. Ответ был {}".format(maxCount, randomValue))
                break
            for user in nameUsers:
                print('Ход пользователя {}'.format(user))
                enterValue = int(input('попытка {} Введите число: '.format(count)))
                if enterValue == randomValue:
                    winner = True
                    winnerName = user
                    break
                elif enterValue > randomValue:
                    print('Загаданое значение меньше')
                else:
                    print('Загаданное значеник больше')
        else:
            print('Победа {} !!!  Загаданное число было равно {}'.format(winnerName, randomValue))

    except:
        print('ошибка')
        Serch(randomValue)

Serch(RandomCreate())