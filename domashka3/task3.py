print('Здравствуйте, я программа, которая умеет писать ваш список наоборот')
print()
print('Давайте для начала добавим данные в список. Введите "stop", когда решите остановиться')
base = []
while True:
    x = input()
    base.append(x)
    print(base)
    print('Добавим что-то еще?')
    if x == 'stop':
        break
del base[-1]
print()
print('Это ваша база')
print(base)
print('А это она наоброт')
base.reverse()
print(base)
