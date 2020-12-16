
print('Здравствуйте, я программа, которая умеет выводить каждый элемент вашего списка по отдельности')
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
for row in base:
    for item in row:
        print(item, end=' ')
    print()
