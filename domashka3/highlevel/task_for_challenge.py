import random
print('Давай сыграем в игру. Я загадаю число, а ты угадаешь. Если угадаешь, то получишь приз, а если нет, то ты умрешь')
print('У тебя 3 попытки. Разумеется я тебе буду подсказывать')
x = random.randint(1, 10)
popitki = 3
a = int(input('Что думаешь? Твой ответ: '))
while True:
    if a > x:
        dif = a - x
    else:
        dif = x - a
    if dif == 0:
        print('Феноменально! Как ты это сделал?')
        print()
        print('Сыграем ещё?')
        ans1 = input('Да или Нет: ')
        if ans1 == 'Да':
            print('Угадай число от 1 до 100')
            f = random.randint(1, 100)
            popitki = 10
            while True:

                if a > f:
                    dif = a - f
                else:
                    dif = f - a
                if dif == 0:
                    print('Феноменально! Как ты это сделал?')
                    print()
                    print('Оцени нашу игру от 1 до 5')
                    stars = int(input())
                    if stars == 5:
                        print('Огромное спасибо')
                        break
                    else:
                        print('Мог бы поставить и больше, жмот')
                        break
                if dif == 1:
                    print('Гориишь, горииишь')
                    popitki = popitki - 1
                    print('У тебя осталось', popitki, 'попытки/ок')
                    a = int(input('Что скажешь теперь? '))
                if 1 < dif < 20:
                    print('Ты очень близок, мой друг')
                    popitki = popitki - 1
                    print('У тебя осталось', popitki, 'попытки/ок')
                    a = int(input('Что скажешь теперь? '))
                if 19 < dif < 50:
                    print('Тепло')
                    popitki = popitki - 1
                    print('У тебя осталось', popitki, 'попытки/ок')
                    a = int(input('Что скажешь теперь? '))
                if 49 < dif < 80:
                    print('Холодно')
                    popitki = popitki - 1
                    print('У тебя осталось', popitki, 'попытки/ок')
                    a = int(input('Что скажешь теперь? '))
                if dif >= 80:
                    print('Очень  холодно')
                    popitki = popitki - 1
                    print('У тебя осталось', popitki, 'попытки/ок')
                    a = int(input('Что скажешь теперь? '))
                if popitki == 0:
                    print('ПОТРАЧЕНО')
                    break
        print('Оцени нашу игру от 1 до 5')
        stars = int(input())
        if stars == 5:
            print('Огромное спасибо')
            break
        else:
            print('Мог бы поставить и больше, жмот')
            break
    if dif == 1:
        print('Гориишь, горииишь')
        popitki = popitki - 1
        print('У тебя осталось', popitki, 'попытки/ок')
        a = int(input('Что скажешь теперь? '))
    if 1 < dif < 4:
        print('Ты очень близок, мой друг')
        popitki = popitki - 1
        print('У тебя осталось', popitki, 'попытки/ок')
        a = int(input('Что скажешь теперь? '))
    if 3 < dif < 6:
        print ('Тепло')
        popitki = popitki - 1
        print('У тебя осталось', popitki, 'попытки/ок')
        a = int(input('Что скажешь теперь? '))
    if 5 < dif < 8:
        print ('Холодно')
        popitki = popitki - 1
        print('У тебя осталось', popitki, 'попытки/ок')
        a = int(input('Что скажешь теперь? '))
    if dif >= 8:
        print('Очень  холодно')
        popitki = popitki - 1
        print('У тебя осталось', popitki, 'попытки/ок')
        a = int(input('Что скажешь теперь? '))
    if popitki == 0:
        print('ПОТРАЧЕНО')
        break
