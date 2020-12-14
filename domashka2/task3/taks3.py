import os
print('Чувак, я ещё не калькулятор, я только учусь, но определенные действия уже могу провернуть. Смотри сам')
print()
print('Введи два числа')
print('Первое')
x = int(input())
print('Второе')
y = int(input())
print('А теперь введи то, что хочешь с ними сделать')
os.system("clear")
while True:
    print()
    print('Можно прибавить, для этого напиши "+", можно разделить, для этого напиши "/", могу и умножить для этого напиши "*" и, конечно же отнять, для этого просто "-"')
    dey = input()
    ans = 0
    if dey == '+':
        ans = x + y
        os.system("clear")
        print(ans)
    if dey == '/':
        if y == 0:
            print('На ноль делить нельзя')
        else:
            ans = x / y
            os.system("clear")
            print(ans)
    if dey == '*':
        ans = x * y
        os.system("clear")
        print(ans)
    if dey == '-':
        ans = x - y
        os.system("clear")
        print(ans)
