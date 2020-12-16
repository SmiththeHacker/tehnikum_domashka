print('Я начинающий калькултор, щя посчитаю тебе чего-нибудь')
print('Можно посчитать сумму разных чисел через списки. Для этого нажмите 1. Для остального 2')
ansx = int(input())
if ansx == 1:
    numbers = []
    options = ['0', '+', '-', '/', '*']
    print('Давай вводить числа')
    print('Чтобы остановиться, напишите "0"')
    while True:
        c = int(input())
        numbers.append(c)
        print(numbers)
        print('Добавим что-то еще?')
        if c == 0:
            break
    del numbers[-1]
    print(numbers)
    print('Давайте выберем действие, которое будет совершено между элементами списка. +, -, *, /, и 0, чтобы завершить программу')
    dey = input()
    while dey !='+':
        print('Так нельзя. Остальной функционал отдельно')
        dey = input()

    print(sum(numbers))
elif ansx == 2:
    print('Введи два числа')
    print('Первое')
    x = int(input())
    print('Второе')
    y = int(input())
    print('А теперь введи то, что хочешь с ними сделать')
    while True:
        print()
        print(
            'Можно прибавить, для этого напиши "+", можно разделить, для этого напиши "/", могу и умножить для этого напиши "*" и, конечно же отнять, для этого просто "-". Чтобы заврешить 0')
        dey = input()
        ans = 0
        if dey == '+':
            ans = x + y

            print(ans)
        if dey == '/':
            if y == 0:
                print('На ноль делить нельзя')
            else:
                ans = x / y

                print(ans)
        if dey == '*':
            ans = x * y

            print(ans)
        if dey == '-':
            ans = x - y
            print(ans)
        if dey == '0':
            break
raise SystemExit
